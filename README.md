# FX為替レート予測ツール開発ポートフォリオ



Python独学3ヶ月の学習記録として、MetaTrader5とXGBoostを用いた

FXレート予測モデルを試作1から段階的に発展させてきた過程をまとめています。

通貨ペアはドル円で（今後選択できる機能を追加予定）、時間足の高値と安値を予想するモデルです。



## 開発の流れ



| 段階 | 内容 | 特徴 |

|---|---|---|

| 試作1 |初回学習 | XGBoostの基本的な1回学習・検証 |

| 試作2 | window特徴量 | 過去100本分をフラット化し学習 |

| 試作3 | 予測結果とMSE記録 | CSVへの評価結果出力機能を追加 |

| 試作4 | バッチ学習・設定クラス化 | 12本ごとのバッチ学習、パス管理の分離 |



## 各試作の詳細



各試作の詳しい開発過程・コミット履歴は個別リポジトリを参照してください。



- [試作1](https://github.com/ksyan-hub/MetaTrader5-ML-prototype-1)

- [試作2](https://github.com/ksyan-hub/MetaTrader5-ML-prototype-2)

- [試作3](https://github.com/ksyan-hub/MetaTrader5-ML-prototype-3)

- [試作4](https://github.com/ksyan-hub/MetaTrader5-ML-prototype-4)



## 本体(継続開発中)



実運用を想定した最新版は以下の別リポジトリで開発を続けています。



-[XGB_predict_fxrate_MetaTrader5_tool](https://github.com/ksyan-hub/XGB\_predict\_fxrate\_MetaTrader5\_tool)



## 使用技術



- Python

- XGBoost

- pandas

- MetaTrader5 (MT5) API



## 開発の振り返り



独学でPythonを学び始めて3ヶ月、プログラミングの知識は全くない状態からの開発です。

初期はファイル名や構成が整理されていませんでしたが、

開発を進める中で命名規則・フォルダ構成・コミットメッセージの

書き方を意識するようになりました。

