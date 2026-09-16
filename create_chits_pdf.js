const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const data = JSON.parse(fs.readFileSync('quiz_data.json', 'utf-8'));

// 8 chits per page (4 rows x 2 columns)
const CHITS_PER_PAGE = 8;
const pages = [];

for (let i = 0; i < data.length; i += CHITS_PER_PAGE) {
  pages.push(data.slice(i, i + CHITS_PER_PAGE));
}

let pagesHtml = '';

pages.forEach((pageChits, pIdx) => {
  let chitsHtml = '';
  pageChits.forEach(chit => {
    let questionsHtml = '';
    chit.questions.forEach(q => {
      let runBadge = `${q.runs} रन:`;
      questionsHtml += `
        <div class="q-item">
          <span class="run-tag">${runBadge}</span> ${escapeHtml(q.question)}
        </div>
      `;
    });

    chitsHtml += `
      <div class="chit-card">
        <div class="chit-header">
          <div class="chit-title">🏏 प्रश्न संख्या ${chit.number}</div>
          <div class="cut-guide">✂ कट लाइन</div>
        </div>
        <div class="chit-body">
          ${questionsHtml}
        </div>
      </div>
    `;
  });

  pagesHtml += `
    <div class="sheet-page">
      ${chitsHtml}
    </div>
  `;
});

const htmlContent = `<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <title>जैन क्रिकेट क्विज़ - पर्ची प्रिंट (Chits Print)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap');

    @page {
      size: A4 portrait;
      margin: 8mm 8mm 8mm 8mm;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Noto Sans Devanagari', Arial, sans-serif;
      color: #0f172a;
      background: #ffffff;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    .sheet-page {
      width: 194mm;
      height: 281mm;
      page-break-after: always;
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: repeat(4, 1fr);
      gap: 5mm;
      overflow: hidden;
    }

    .sheet-page:last-child {
      page-break-after: avoid;
    }

    .chit-card {
      border: 1.5px dashed #475569;
      border-radius: 6px;
      padding: 7px 9px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      background: #ffffff;
      height: 100%;
      box-sizing: border-box;
      overflow: hidden;
    }

    .chit-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 4px;
      border-bottom: 1.5px solid #1e293b;
      margin-bottom: 5px;
      flex-shrink: 0;
    }

    .chit-title {
      font-size: 13pt;
      font-weight: 800;
      color: #0f172a;
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      letter-spacing: 0.01em;
    }

    .cut-guide {
      font-size: 8pt;
      color: #64748b;
      font-family: 'Noto Sans Devanagari', sans-serif;
      font-weight: 600;
    }

    .chit-body {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
      gap: 4px;
    }

    .q-item {
      font-size: 10.8pt;
      line-height: 1.34;
      color: #1e293b;
      font-weight: 500;
    }

    .run-tag {
      font-weight: 800;
      font-size: 11.2pt;
      color: #000000;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      border: 1px solid #cbd5e1;
      display: inline-block;
      margin-right: 2px;
    }
  </style>
</head>
<body>
  ${pagesHtml}
</body>
</html>`;

fs.writeFileSync('chits_print.html', htmlContent, 'utf-8');
console.log('Generated chits_print.html');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
  });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve('chits_print.html'), { waitUntil: 'networkidle0' });
  
  await page.pdf({
    path: 'Jain_Cricket_Quiz_Chits.pdf',
    format: 'A4',
    printBackground: true,
    margin: {
      top: '8mm',
      right: '8mm',
      bottom: '8mm',
      left: '8mm'
    }
  });

  await browser.close();
  console.log('Generated Jain_Cricket_Quiz_Chits.pdf successfully!');
})();

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
