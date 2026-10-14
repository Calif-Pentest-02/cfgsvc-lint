# cfgsvc operator console

Small read-only console for the appliance fleet profile tables. The column set
comes from the vendor's schema package so the console and the service cannot
drift apart.

```
npm install
node -e "console.log(require('./console.js').columns())"
```
