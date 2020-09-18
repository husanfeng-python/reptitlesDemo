# hw-project
```
 if (oSession.fullUrl.Contains("openh5/poi/food"))
        {
            oSession.utilDecodeResponse();//消除保存的请求可能存在乱码的情况
            var fso;
            var file;
            fso = new ActiveXObject("Scripting.FileSystemObject");
            //文件保存路径，可自定义
            file = fso.OpenTextFile("D:/githubPythonProject/hw-project/美团爬虫/meituandata/meituanData1.txt",8 ,true, true);
            // file.writeLine("Response code: " + oSession.responseCode);
            file.writeLine(oSession.GetResponseBodyAsString());
            // file.writeLine("\n");
            file.close();
        }
        
        //过滤无关请求，只关注特定请求
        if (oSession.fullUrl.Contains("/menuproducts"))
        {
            oSession.utilDecodeResponse();//消除保存的请求可能存在乱码的情况
            var fso;
            var file;
            fso = new ActiveXObject("Scripting.FileSystemObject");
            //文件保存路径，可自定义
            file = fso.OpenTextFile("D:/githubPythonProject/hw-project/美团爬虫/meituandata/meituanData2.txt",8 ,true, true);
            // file.writeLine("Response code: " + oSession.responseCode);
            file.writeLine(oSession.GetResponseBodyAsString());
            // file.writeLine("\n");
            file.close();
        }
```
mitmdump -s analysis_response.py -p 8887
