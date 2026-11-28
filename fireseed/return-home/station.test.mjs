import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {plan} from './planner.mjs';
const c=JSON.parse(await readFile(new URL('./catalog.json',import.meta.url),'utf8'));
test('known prior version has an update',()=>assert.equal(plan(c,'V0.1').status,'UPDATE_AVAILABLE'));
test('current version does not imply install',()=>{const p=plan(c,'0.1.1');assert.equal(p.status,'CURRENT_REPORTED');assert.equal(p.host_installation,'NOT_VERIFIED');});
test('unknown or newer version holds',()=>{for(const v of [null,'0.2','invalid'])assert.equal(plan(c,v).status,'HOLD_UNKNOWN_VERSION');});
test('missing release holds',()=>assert.equal(plan({...c,equipment:[]},'0.1').status,'HOLD_NO_COMPATIBLE_RELEASE'));
test('no private or unreleased skills',()=>assert.deepEqual(plan(c,'0.1').available_additional_skills,[]));
test('catalog digest and size match existing release bytes',async()=>{const item=c.equipment[0];const data=await readFile(new URL('../dist/LIHUO_FIRESEED_BABY_V0.1.1.zip',import.meta.url));assert.equal(data.length,item.bytes);assert.equal(createHash('sha256').update(data).digest('hex'),item.sha256);});

import { spawnSync } from 'node:child_process';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
const cli=fileURLToPath(new URL('./station.mjs',import.meta.url));
function call(...args){const r=spawnSync(process.execPath,[cli,...args],{encoding:'utf8',timeout:40000});return {code:r.status,output:JSON.parse(r.stdout)};}
test('CLI verifies real ZIP and rejects corrupt input',async()=>{
  const dir=await mkdtemp(join(tmpdir(),'fireseed-'));
  try {
    const actual=call('verify',fileURLToPath(new URL('../dist/LIHUO_FIRESEED_BABY_V0.1.1.zip',import.meta.url)));
    assert.equal(actual.code,0);assert.equal(actual.output.status,'ARTIFACT_VERIFIED');
    const bad=join(dir,'bad.zip');await writeFile(bad,'not a release');
    const rejected=call('verify',bad);assert.equal(rejected.code,2);assert.equal(rejected.output.status,'CHECKSUM_OR_SIZE_MISMATCH');
  } finally {await rm(dir,{recursive:true,force:true});}
});
test('CLI acquisition refuses unknown and current versions without writing',async()=>{
  const dir=await mkdtemp(join(tmpdir(),'fireseed-'));
  try {
    for(const v of ['0.2','0.1.1']){const result=call('acquire',v,join(dir,'never.zip'));assert.equal(result.code,2);}
    await assert.rejects(readFile(join(dir,'never.zip')),{code:'ENOENT'});
  } finally {await rm(dir,{recursive:true,force:true});}
});
test('live pinned acquisition and no overwrite', {skip:process.env.FIRESEED_LIVE_TEST!=='1'},async()=>{
  const dir=await mkdtemp(join(tmpdir(),'fireseed-live-'));
  try {
    const dest=join(dir,'new.zip');
    const got=call('acquire','0.1',dest);assert.equal(got.code,0,JSON.stringify(got.output));assert.equal(got.output.status,'ARTIFACT_ACQUIRED_AND_VERIFIED');assert.equal(got.output.host_installation,'NOT_VERIFIED');
    const old=await readFile(dest);const repeat=call('acquire','0.1',dest);assert.equal(repeat.code,2);assert.deepEqual(await readFile(dest),old);
  } finally {await rm(dir,{recursive:true,force:true});}
});
