export function plan(c, input) {
  const known=["0.1","0.1.1"];
  const v=typeof input==="string"?input.replace(/^LIHUO_FIRESEED_BABY_/,"").replace(/^V/i,""):null;
  const out={station:c.station_version,reported_version:v,inventory_basis:"USER_REPORTED_NOT_VERIFIED",available_additional_skills:[],host_installation:"NOT_VERIFIED",effect:"NOT_TESTED",authority:"UNCHANGED"};
  if(!known.includes(v)) return {...out,status:"HOLD_UNKNOWN_VERSION",next:"Identify actual package version; do not downgrade or infer compatibility."};
  if(v===c.current_fireseed) return {...out,status:"CURRENT_REPORTED",next:"No base update indicated. Check actual installed material if uncertain."};
  const item=c.equipment.find(x=>x.id==="fireseed-base"&&x.status==="AVAILABLE_FOR_PUBLIC_EVALUATION"&&x.compatible_from.includes(v)&&x.version===c.current_fireseed);
  if(!item) return {...out,status:"HOLD_NO_COMPATIBLE_RELEASE",next:"No compatible public update."};
  return {...out,status:"UPDATE_AVAILABLE",candidate:item,next:"Acquire only with user approval; verify checksum before loading; run independent behavior test."};
}
