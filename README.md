# circuit-breaker-sfn-example
**AWS StepFunctions を使用した Circuit-breaker パターンの実装サンプル**

最新の AWS SAM CLI が使用できる環境でプロイできます。

1.  template.yml があるフォルダに移動し、sam build を行います。（Python 3.11 のランタイムが存在している場合）

    ```
    sam build
    ```
    
    Python 3.11 のランタイムが存在していない場合は下記を実行します。この場合、Docker がインストールされている必要があります。

    ```
    sam build --use-container
    ```

2. ビルドに成功したら、デプロイを行います。プロンプトに対して環境に応じた内容を入力してください。
   
   ```
   sam deploy --guided
   ```
   

