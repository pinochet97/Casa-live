// Render HTML jobs to PNG (and optional PDF). jobs: [{html,w,h,out,pdf?,scale?}]
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const jobs=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
(async()=>{const b=await chromium.launch();
for(const [i,j] of jobs.entries()){const tmp=path.join(path.dirname(j.out),'.tmp_'+i+'.html');fs.mkdirSync(path.dirname(j.out),{recursive:true});fs.writeFileSync(tmp,j.html);
 const p=await b.newPage({viewport:{width:j.w,height:j.h},deviceScaleFactor:j.scale||1});await p.goto('file://'+tmp,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:j.out,clip:{x:0,y:0,width:j.w,height:j.h},omitBackground:!!j.transparent});
 if(j.pdf){await p.pdf({path:j.pdf,width:(j.pdfW||j.w+'px'),height:(j.pdfH||j.h+'px'),printBackground:true,pageRanges:'1'});}
 await p.close();fs.unlinkSync(tmp);}
await b.close();console.log('rendered',jobs.length);})();
