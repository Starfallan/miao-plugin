import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dir = path.join(__dirname, 'resources', 'meta-gs', 'character');
const noEtaList = [];

fs.readdirSync(dir).forEach(folder => {
  const dataPath = path.join(dir, folder, 'data.json');
  if (fs.existsSync(dataPath)) {
    try {
      let data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
      if (!data.eta) {
        noEtaList.push(data.name || folder);
      }
    } catch (e) {
      console.log(`Error reading ${dataPath}: ${e.message}`);
    }
  }
});

console.log('没有 eta 的角色列表:');
console.log("个数:", noEtaList.length);
noEtaList.forEach(name => console.log(name));