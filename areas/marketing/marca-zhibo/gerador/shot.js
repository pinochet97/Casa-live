const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+process.argv[4]||1400,height:900},deviceScaleFactor:1});
await p.goto('file://'+process.argv[2],{waitUntil:'networkidle'});await p.screenshot({path:process.argv[3],fullPage:true});await b.close();})();
