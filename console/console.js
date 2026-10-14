// Operator console: renders the fleet profile table.
const schema = require('cfgsvc-profile-schema');

function columns() {
  return schema.FIELDS;
}

module.exports = { columns, SCHEMA_VERSION: schema.VERSION };
