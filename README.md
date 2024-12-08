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
   
3. AWS マネジメントコンソールで、AWS Step Functions コンソールに移動し、`circuitbreaker-statemachine` を開いて実行します。 入力として下記を使用します。
    - (**<AWS_REGION>** の部分は使用している AWS リージョンの IDに置き換えてください。 例: 東京リージョンなら `ap-northeast-1`）
    - (**<AWS_ACCOUNT>** の部分は使用している AWS アカウントの 12 桁の数字に置き換えてください）

    - 下記の入力は、サーキットブレーカーが CLOSE 状態のサービスの呼び出しです。 下記では正常に終了します。

    ```json
    {
      "TargetLambda": "arn:aws:lambda:<AWS_REGION>:<AWS_ACCOUNT>:function:circuitbreaker-Payment",
      "Payload": {"order" : {"item_id": "Dummy01", "unit": 10}}
    }
    ```

    - 下記の入力は、サーキットブレーカーが OPEN 状態 になるサービスの呼び出しです。下記はエラーで終了します。
    - 20秒以内に再実行してもサーキットブレーカーは OPEN のままなので、サービス呼び出しを行わずエラーで終了させています。

    ```json
    {
      "TargetLambda": "arn:aws:lambda:<AWS_REGION>:<AWS_ACCOUNT>:function:circuitbreaker-PaymentTimeout",
      "Payload": {"order" : {"item_id": "Dummy02", "unit": 20}}
    }
    ```
    
4. 環境をクリアする場合は、下記を実行します。
   
    ```
    sam delete --no-prompts
    ```
