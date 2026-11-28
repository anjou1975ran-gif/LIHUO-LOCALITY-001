import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { basename, resolve } from 'node:path';
import { plan } from './planner.mjs';
const catalog=JSON.parse(await readFile(new URL('./catalog.json',import.meta.url),'utf8'));
const [action, version, file] = process.argv.slice(2);
const emit = x => console.log(JSON.stringify(x,null,2));
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const item=catalog.equipment.find(x=>x.id==='fireseed-base');
try {
 if(action==='plan' && !file) { emit(plan(catalog,version)); }
 else if(action==='verify' && version && !file) {
   const data=await readFile(version);
   const digest=hash(data);
   const ok=data.length===item.bytes && digest===item.sha256;
   emit({action:'VERIFY_LOCAL_FILE',file:basename(version),sha256:digest,expected_sha256:item.sha256,bytes:data.length,status:ok?'ARTIFACT_VERIFIED':'CHECKSUM_OR_SIZE_MISMATCH',host_installation:'NOT_VERIFIED',effect:'NOT_TESTED',authority:'UNCHANGED'});
   if(!ok)process.exitCode=2;
 } else if(action==='acquire' && version && file) {
   const p=plan(catalog,version);
   if(p.status!=='UPDATE_AVAILABLE') {emit(p);process.exitCode=2;}
   else {
     const u=new URL(p.candidate.url);
     if(u.protocol!=='https:'||u.hostname!=='raw.githubusercontent.com'||u.pathname!== '/anjou1975ran-gif/LIHUO-LOCALITY-001/494341a123d1f09e52e6d4e7fdf659960a8eea5c/fireseed/dist/LIHUO_FIRESEED_BABY_V0.1.1.zip') throw Error('Source not allowlisted');
     const response=await fetch(u,{redirect:'error',signal:AbortSignal.timeout(30000)});
     if(!response.ok)throw Error('HTTP '+response.status);
     const chunks=[];let count=0;
     if(!response.body)throw Error('Empty body');
     for await(const chunk of response.body){count+=chunk.length;if(count>p.candidate.bytes)throw Error('Size exceeds expected');chunks.push(Buffer.from(chunk));}
     const data=Buffer.concat(chunks),digest=hash(data);
     if(data.length!==p.candidate.bytes||digest!==p.candidate.sha256)throw Error('Artifact verification failed');
     await writeFile(resolve(file),data,{flag:'wx'});
     emit({action:'ACQUIRE',status:'ARTIFACT_ACQUIRED_AND_VERIFIED',file:basename(file),source:u.href,sha256:digest,bytes:data.length,host_installation:'NOT_VERIFIED',effect:'NOT_TESTED',authority:'UNCHANGED',next:'User loads approved contents into Host and tests behavior.'});
   }
 } else {console.error('Usage: node station.mjs plan VERSION | verify ZIP | acquire VERSION NEW_ZIP_PATH');process.exitCode=2;}
} catch(error){emit({action:action||'UNKNOWN',status:'HOLD',reason:String(error.message),host_installation:'NOT_VERIFIED',effect:'NOT_TESTED',authority:'UNCHANGED'});process.exitCode=2;}
