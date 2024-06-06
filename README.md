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
    - (<AWS_ACCOUNT> の部分は使用している AWS アカウントの 12 桁の数字に置き換えてください）

    - サーキットブレーカーが CLOSE 状態のサービスの呼び出し: (正常に終了）

    ```json
    {
      "TargetLambda": "arn:aws:lambda:ap-northeast-1:330174381929:function:circuitbreaker-Payment",
      "Payload": {"order" : {"item_id": "Dummy01", "unit": 10}}
    }
    ```

    - サーキットブレーカーが OPEN 状態 になるサービスの呼び出し: (エラーで終了）
    - 20秒以内に再実行してもサーキットブレーカーは OPEN のままなので、サービス呼び出しを行わずエラーで終了させています。

    ```json
    {
      "TargetLambda": "arn:aws:lambda:ap-northeast-1:330174381929:function:circuitbreaker-PaymentTimeout",
      "Payload": {"order" : {"item_id": "Dummy02", "unit": 20}}
    }
    ```


