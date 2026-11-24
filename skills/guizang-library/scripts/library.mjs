import { join } from 'node:path';
import { homedir } from 'node:os';
import { fileURLToPath } from 'node:url';
import { readFileSync } from 'node:fs';
import { addWork, listWorks } from '../../../lib/library.js';
import { recipesFor } from '../../../lib/recipes.js';

process.env.DSH_HOME = process.env.CODEX_HOME || join(homedir(), '.codex');
const [command, target, title] = process.argv.slice(2);
let result;
switch (command) {
  case 'recipes': result = recipesFor('zh'); break;
  case 'examples': {
    const manifest = fileURLToPath(new URL('../../../examples/manifest.json', import.meta.url));
    result = JSON.parse(readFileSync(manifest, 'utf8'));
    break;
  }
  case 'list': result = listWorks(); break;
  case 'add':
    if (!target || !title) throw new Error('用法：add <路径> <标题>');
    result = addWork(target, {title});
    break;
  default: throw new Error('可用命令：list、add、recipes、examples');
}
console.log(JSON.stringify(result, null, 2));
