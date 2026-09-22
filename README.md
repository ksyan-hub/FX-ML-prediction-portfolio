# 試作1: 初回学習・検証

USDJPY 5分足データを使い、XGBoost で高値(high)を予測する最初の試作です。
学習期間(2026/7/6〜7/13)と検証期間(2026/7/13〜7/20)を分けて、汎化性能を確認しました。

## 特徴

- 学習用と検証用のデータを時間的に分離(未来のデータが学習に混ざらないようにしている)
- 特徴量: open, low, close, tick_volume, spread / 正解ラベル: high

## ファイル構成

| ファイル | 役割 |
|---|---|
| `train_data_to_csv.py` | MT5から学習期間のレートデータを取得しCSVに保存 |
| `test_data_to_csv.py` | MT5から検証期間のレートデータを取得しCSVに保存 |
| `01_xgb_USDJPY_5m_20260706_20260713.py` | 学習・予測・MSE評価の本体処理 |

## 実行方法

1. `train_data_to_csv.py` / `test_data_to_csv.py` を実行しレートデータを取得(MT5端末が起動・ログイン済みであること)
2. `01_xgb_USDJPY_5m_20260706_20260713.py` を実行し、学習・検証・MSEの表示を行う

## 動作環境

- Windows(MetaTrader5 パッケージが Windows 専用のため)
- MT5 端末とブローカー口座が必要
- 必要パッケージ: pandas, numpy, xgboost, scikit-learn, MetaTrader5, pytz

## 結果

Name: high, Length: 1441, dtype: float64
[0]     train-rmse:0.29720      eval-rmse:0.18040
[1]     train-rmse:0.26814      eval-rmse:0.16218
[2]     train-rmse:0.24195      eval-rmse:0.14583
[3]     train-rmse:0.21833      eval-rmse:0.13123
[4]     train-rmse:0.19705      eval-rmse:0.11820
[5]     train-rmse:0.17786      eval-rmse:0.10645
[6]     train-rmse:0.16055      eval-rmse:0.09573
[7]     train-rmse:0.14496      eval-rmse:0.08622
[8]     train-rmse:0.13089      eval-rmse:0.07770
[9]     train-rmse:0.11819      eval-rmse:0.07000

## 学び・今後の課題

- 特徴量に同じローソク足の close"を含めていたため、正解ラベル("high")と時間的に同時の情報を使ってしまっていた。試作2で過去のwindowデータのみを特徴量にする形に修正した
- 学習は1回のみで、バッチ学習・継続学習はまだ行っていない(試作4で対応)
