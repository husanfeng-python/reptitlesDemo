# 饿了么爬虫
在Fiddler抓包工具下进行如下配置：
```
        // 饿了么截取response
        if (oSession.fullUrl.Contains("h5/mtop.venus.shopcategoryservice.getcategorydetail/"))
        {
            oSession.utilDecodeResponse();//消除保存的请求可能存在乱码的情况
            var fso;
            var file;
            fso = new ActiveXObject("Scripting.FileSystemObject");
            //文件保存路径，可自定义
            file = fso.OpenTextFile("D:/githubPythonProject/hw-project/饿了么爬虫/elemedata/elemeData.txt",8 ,true, true);
            // file.writeLine("Response code: " + oSession.responseCode);
            file.writeLine(oSession.GetResponseBodyAsString());
            // file.writeLine("\n");
            file.close();
        }
```