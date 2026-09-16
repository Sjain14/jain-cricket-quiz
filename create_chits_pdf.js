const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const data = JSON.parse(fs.readFileSync('quiz_data.json', 'utf-8'));

// 6 Jain Gyan Paheliyan for No-Ball chits
const NO_BALL_PAHELIYAN = [
  {
    id: 1,
    paheli: 'एक अक्षर का मेरा नाम, मैं हूँ पंच प्रभु का धाम।\nसब जन करते मेरा ध्यान, बताओ तुम मेरा नाम?',
    answer: 'ॐ (पंच परमेष्ठी का प्रतीक)'
  },
  {
    id: 2,
    paheli: 'जहाँ वाणी प्रकट प्रभु की, छः अक्षर का मेरा नाम।\nगौतम जहाँ गणधर हुए, तीर्थंकर का भव्य धाम। बताओ क्या?',
    answer: 'समवशरण'
  },
  {
    id: 3,
    paheli: 'आठ गुणों को प्राप्त किया है, निराकार पद धार लिया है।\nअब न कभी जग में आना, सिद्धशिला पर धाम बनाना। बताओ कौन?',
    answer: 'सिद्ध भगवान'
  },
  {
    id: 4,
    paheli: 'जिसके सिर पर मैं हूँ आता, उसके होंठ-भुजा फड़काता।\nआँखें लाल विवेक मिटाता, छोटा-बड़ा न कोई सुहाता। बताओ कौन?',
    answer: 'क्रोध (कषाय)'
  },
  {
    id: 5,
    paheli: 'तीन लोक में अनुपम हूँ, तीनों लोकों का मैं सार।\nजिसने मुझको जान लिया, वही उतरे भव के पार। बताओ कौन?',
    answer: 'आत्मा (शुद्ध चेतन)'
  },
  {
    id: 6,
    paheli: 'ज्ञान का पावन सागर हूँ, जिनवर की वाणी कहलाऊँ।\nअज्ञान तिमिर को दूर करूँ, मोक्ष मार्ग दिखलाऊँ। बताओ कौन?',
    answer: 'जिनवाणी / शास्त्र'
  }
];

// Save No-Ball Paheliyan to JSON for project consistency
fs.writeFileSync('no_ball_paheliyan.json', JSON.stringify(NO_BALL_PAHELIYAN, null, 2), 'utf-8');

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

  // If this is the last page (page 6), fill the 3 remaining empty slots with 6 No-Ball half-chits
  if (pIdx === pages.length - 1) {
    // 3 slots, each with 2 no-ball cards
    for (let slot = 0; slot < 3; slot++) {
      const p1 = NO_BALL_PAHELIYAN[slot * 2];
      const p2 = NO_BALL_PAHELIYAN[slot * 2 + 1];

      chitsHtml += `
        <div class="noball-slot-container">
          <!-- No Ball Card 1 -->
          <div class="noball-card">
            <div class="noball-header">
              <div class="noball-title-row">
                <span class="noball-badge">⚾ नो बॉल #${p1.id}</span>
                <span class="noball-score-pill">नो बॉल: 1 रन • पहेली: 2 रन</span>
              </div>
              <span class="noball-cut">✂ कट लाइन</span>
            </div>
            <div class="noball-body">
              <div class="paheli-title-tag">💡 ज्ञान पहेली:</div>
              <div class="paheli-text">${escapeHtml(p1.paheli).replace(/\n/g, '<br>')}</div>
            </div>
          </div>

          <!-- No Ball Card 2 -->
          <div class="noball-card">
            <div class="noball-header">
              <div class="noball-title-row">
                <span class="noball-badge">⚾ नो बॉल #${p2.id}</span>
                <span class="noball-score-pill">नो बॉल: 1 रन • पहेली: 2 रन</span>
              </div>
              <span class="noball-cut">✂ कट लाइन</span>
            </div>
            <div class="noball-body">
              <div class="paheli-title-tag">💡 ज्ञान पहेली:</div>
              <div class="paheli-text">${escapeHtml(p2.paheli).replace(/\n/g, '<br>')}</div>
            </div>
          </div>
        </div>
      `;
    }
  }

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

    /* STANDARD QUESTION CARD */
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

    /* NO-BALL CARDS CONTAINER (2 half-cards per slot) */
    .noball-slot-container {
      display: flex;
      flex-direction: column;
      gap: 3mm;
      height: 100%;
      width: 100%;
      box-sizing: border-box;
    }

    .noball-card {
      border: 1.5px dashed #dc2626;
      border-radius: 6px;
      padding: 5px 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #fffafa;
      flex: 1;
      box-sizing: border-box;
      overflow: hidden;
    }

    .noball-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #fca5a5;
      padding-bottom: 3px;
      margin-bottom: 3px;
      flex-shrink: 0;
    }

    .noball-title-row {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .noball-badge {
      font-size: 10.5pt;
      font-weight: 800;
      color: #dc2626;
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      letter-spacing: 0.01em;
    }

    .noball-score-pill {
      font-size: 7.8pt;
      font-weight: 700;
      color: #991b1b;
      background: #fee2e2;
      padding: 1px 5px;
      border-radius: 3px;
      border: 0.5px solid #f87171;
    }

    .noball-cut {
      font-size: 7.5pt;
      color: #94a3b8;
      font-weight: 600;
    }

    .noball-body {
      display: flex;
      flex-direction: column;
      gap: 2px;
      flex: 1;
      justify-content: center;
    }

    .paheli-title-tag {
      font-size: 8pt;
      font-weight: 700;
      color: #b91c1c;
      text-transform: uppercase;
    }

    .paheli-text {
      font-size: 9.8pt;
      font-weight: 600;
      color: #1e293b;
      line-height: 1.28;
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
  console.log('Generated Jain_Cricket_Quiz_Chits.pdf with 6 No-Ball chits on Page 6 successfully!');
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
