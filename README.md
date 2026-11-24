# Arabic Finance Icons

An open source SVG icon set for bilingual financial products. The first release includes 16 original outline icons for payments, transfers, accounts, and security. The symbols are neutral and contain no brand marks or currency glyphs.

## Browse

Open `preview/index.html` in a browser. Every icon is a standalone SVG in `icons/` with a 24 × 24 viewBox, `currentColor`, round joins, and a 1.8 px stroke. Icons can be used in Arabic RTL and English LTR layouts.

## Use

```html
<img src="icons/wallet.svg" alt="محفظة" width="24" height="24">
```

For decorative icons, use an empty `alt` attribute. For interactive buttons, give the button a meaningful label. SVGs use `currentColor` when embedded inline; an external `<img>` cannot inherit CSS `color` from its parent.

## Icon catalog

| File | English | العربية |
| --- | --- | --- |
| bank.svg | Bank | بنك |
| wallet.svg | Wallet | محفظة |
| card.svg | Card | بطاقة |
| transfer.svg | Transfer | تحويل |
| send.svg | Send | إرسال |
| receive.svg | Receive | استلام |
| exchange.svg | Exchange | صرف عملات |
| receipt.svg | Receipt | إيصال |
| history.svg | History | السجل |
| shield.svg | Protection | حماية |
| lock.svg | Lock | قفل |
| verify.svg | Verified | موثّق |
| savings.svg | Savings | ادخار |
| fees.svg | Fees | رسوم |
| globe.svg | International | دولي |
| phone.svg | Mobile payment | دفع بالموبايل |

Directional icons `send`, `receive`, and `transfer` are semantic actions, not layout arrows. Do not mirror them automatically for RTL: direction of money flow must be established by the surrounding label and interface context.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and meaningful pull requests are welcome. Please explain the use case before proposing a new icon.

## License

MIT. See [LICENSE](LICENSE).
