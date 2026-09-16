const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const htmlContent = `<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <title>जैन क्रिकेट - मास्टर मंच संचालन स्क्रिप्ट (Host Script)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap');

    @page {
      size: A4 portrait;
      margin: 10mm 12mm 10mm 12mm;
      @bottom-right {
        content: "पृष्ठ " counter(page) " / " counter(pages);
        font-family: 'Noto Sans Devanagari', 'Outfit', sans-serif;
        font-size: 8.5pt;
        color: #94a3b8;
      }
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Noto Sans Devanagari', Arial, sans-serif;
      color: #1e293b;
      background: #ffffff;
      line-height: 1.42;
      font-size: 10pt;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    /* HEADER BANNER */
    .script-header {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #311042 100%);
      color: #ffffff;
      border-radius: 10px;
      padding: 12px 16px;
      margin-bottom: 10px;
      border: 1px solid #334155;
    }

    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255, 255, 255, 0.18);
      padding-bottom: 6px;
      margin-bottom: 8px;
    }

    .temple-tag {
      font-size: 9.2pt;
      font-weight: 700;
      color: #fbbf24;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .ahimsa-tag {
      font-size: 8.5pt;
      color: #cbd5e1;
      font-weight: 600;
    }

    .header-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .main-title {
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      font-size: 18pt;
      font-weight: 900;
      color: #fef08a;
      letter-spacing: 0.01em;
      line-height: 1.1;
    }

    .main-subtitle {
      font-size: 9.5pt;
      color: #e2e8f0;
      margin-top: 2px;
      font-weight: 500;
    }

    .parva-badge {
      background: linear-gradient(135deg, #f59e0b, #d97706);
      color: #0f172a;
      font-weight: 800;
      font-size: 9pt;
      padding: 4px 10px;
      border-radius: 6px;
      text-align: right;
      line-height: 1.25;
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
    }

    .roles-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr 1.1fr;
      gap: 6px;
      margin-top: 8px;
      background: rgba(255, 255, 255, 0.08);
      padding: 6px 10px;
      border-radius: 6px;
    }

    .role-item {
      font-size: 8.5pt;
      color: #cbd5e1;
    }

    .role-label {
      font-weight: 700;
      color: #93c5fd;
      text-transform: uppercase;
      font-size: 7.2pt;
      letter-spacing: 0.03em;
    }

    .role-val {
      color: #ffffff;
      font-weight: 700;
    }

    /* SECTION HEADERS */
    .act-title {
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      font-size: 11.5pt;
      font-weight: 800;
      color: #0f172a;
      border-left: 3.5px solid #f59e0b;
      padding-left: 6px;
      margin-bottom: 6px;
      margin-top: 8px;
    }

    /* DIALOGUE BLOCKS */
    .dialogue-card {
      border-radius: 6px;
      padding: 6px 10px;
      margin-bottom: 5px;
      position: relative;
    }

    .dialogue-card.sahaj {
      background: #f0f7ff;
      border-left: 3.5px solid #2563eb;
    }

    .dialogue-card.aman {
      background: #fbf5ff;
      border-left: 3.5px solid #9333ea;
    }

    .dialogue-card.umpire {
      background: #fffbeb;
      border-left: 3.5px solid #d97706;
    }

    .speaker-badge {
      display: inline-block;
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      font-size: 8pt;
      font-weight: 800;
      padding: 1px 6px;
      border-radius: 3px;
      margin-bottom: 3px;
      text-transform: uppercase;
    }

    .badge-sahaj {
      background: #dbeafe;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
    }

    .badge-aman {
      background: #f3e8ff;
      color: #7e22ce;
      border: 1px solid #e9d5ff;
    }

    .badge-umpire {
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }

    .dialogue-text {
      font-size: 9.8pt;
      color: #1e293b;
      line-height: 1.38;
      font-weight: 500;
    }

    .stage-note {
      font-style: italic;
      color: #64748b;
      font-size: 8.8pt;
      margin: 2px 0;
      display: block;
    }

    /* TEAM CARDS */
    .teams-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
      margin: 6px 0 8px 0;
    }

    .team-box {
      border-radius: 6px;
      padding: 7px 10px;
      border: 1.5px solid;
    }

    .team-red {
      background: #fef2f2;
      border-color: #f87171;
    }

    .team-blue {
      background: #eff6ff;
      border-color: #60a5fa;
    }

    .team-green {
      background: #f0fdf4;
      border-color: #4ade80;
    }

    .team-gold {
      background: #fefce8;
      border-color: #facc15;
    }

    .team-name {
      font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
      font-size: 10.2pt;
      font-weight: 800;
      margin-bottom: 1px;
    }

    .team-slogan {
      font-size: 8.8pt;
      font-weight: 600;
      color: #475569;
    }

    /* RULES BOX */
    .rules-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 8px;
    }

    .rule-item {
      display: flex;
      align-items: flex-start;
      gap: 6px;
      margin-bottom: 4px;
      font-size: 9.4pt;
      line-height: 1.35;
    }

    .rule-bullet {
      background: #0f172a;
      color: #ffffff;
      font-family: 'Outfit', sans-serif;
      font-size: 7.2pt;
      font-weight: 700;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }

    /* SHAYARI HIGHLIGHT BOX */
    .shayari-card {
      background: linear-gradient(135deg, #fefce8 0%, #fffbeb 100%);
      border: 1.5px solid #fcd34d;
      border-radius: 6px;
      padding: 8px 12px;
      margin: 6px 0;
      text-align: center;
    }

    .shayari-text {
      font-size: 10pt;
      font-weight: 600;
      color: #78350f;
      line-height: 1.45;
    }

    /* SITUATIONAL PROMPTS */
    .situation-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      margin: 6px 0;
    }

    .situation-box {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 6px 9px;
    }

    .situation-header {
      font-size: 8.6pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .situation-punch {
      font-size: 8.8pt;
      color: #334155;
      line-height: 1.35;
    }

    .page-break {
      page-break-after: always;
    }
  </style>
</head>
<body>

  <!-- ==================== PAGE 1: GRAND OPENING, WELCOME, UMPIRE & COMMENTATORS ==================== -->
  <div class="script-header">
    <div class="header-top">
      <span class="temple-tag">🏛 माधवगंज के पारसनाथ • ज्ञान का खेल, संस्कारों का मेल</span>
      <span class="ahimsa-tag">॥ अहिंसा परमो धर्मः ॥</span>
    </div>
    <div class="header-title-row">
      <div>
        <div class="main-title">🏏 JAIN CRICKET (जैन क्रिकेट)</div>
        <div class="main-subtitle">मास्टर मंच संचालन स्क्रिप्ट (Master Anchoring Script) • प्रश्नों की पिच पर, ज्ञान की जीत</div>
      </div>
      <div class="parva-badge">
        दशलक्षण पर्व • दिन 1<br>
        <span style="font-size: 10.5pt; font-weight: 900;">उत्तम क्षमा धर्म</span>
      </div>
    </div>
    <div class="roles-grid">
      <div class="role-item">
        <div class="role-label">🎙 मुख्य संचालक (Hosts)</div>
        <div class="role-val">सहज भैया एवं अमन</div>
      </div>
      <div class="role-item">
        <div class="role-label">⚖ मुख्य अंपायर</div>
        <div class="role-val">डॉ. सुकुमार जैन</div>
      </div>
      <div class="role-item">
        <div class="role-label">🎧 कमेंटेटर्स</div>
        <div class="role-val">निर्मल जैन, विक्की जैन</div>
      </div>
    </div>
  </div>

  <!-- CHECKLIST -->
  <div class="rules-card" style="background: #f1f5f9; border-color: #cbd5e1; padding: 5px 10px; margin-bottom: 8px;">
    <span style="font-weight: 700; font-size: 8.5pt; color: #475569;">⚡ स्टेज चेकलिस्ट:</span>
    <span style="font-size: 8.4pt; color: #334155; margin-left: 5px;">
      माइक 1 (सहज भैया) • माइक 2 (अमन) • माइक 3 (कमेंट्री) • माइक 4 (अंपायर) • पर्चियों का बाउल (50 Chits + 6 No-Ball) • टॉस का सिक्का • स्कोरबोर्ड
    </span>
  </div>

  <!-- ACT 1 -->
  <div class="act-title">🎬 अंक 1: मंगलाचरण एवं धमाकेदार ओपनिंग (Grand Opening)</div>
  <span class="stage-note">*(मांगलिक संगीत / शंखनाद। सहज भैया और अमन दोनों मंच पर साथ आते हैं)*</span>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "णमो अरिहंताणं, णमो सिद्धाणं, णमो आयरियाणं। णमो उवज्झायाणं, णमो लोए सव्वसाहूणं॥<br>
      <strong>बोलिए 1008 श्री महावीर भगवान की जय! माधवगंज के पारसनाथ भगवान की जय! दशलक्षण महापर्व की जय!</strong>"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "जय जिनेंद्र माधवगंज! जय जिनेंद्र सभी धर्मप्रेमी बंधुओं, माताओं, बहनों और हमारे सभी युवा साथियों!<br>
      आज का दिन कोई साधारण दिन नहीं है... आज से प्रारंभ हो रहा है आत्म-कल्याण का पावन पर्व — <strong>दशलक्षण महापर्व</strong>! और आज प्रथम दिवस है <strong>'उत्तम क्षमा धर्म'</strong> का!"
    </div>
  </div>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "बिल्कुल अमन! और क्षमा का सार क्या है? <em>‘क्रोध को जीतना, वैर को मिटाना, और हर आत्मा से मैत्री भाव निभाना!’</em><br>
      लेकिन आज माधवगंज के इस पावन प्रांगण में धर्म के साथ-साथ एक अद्भुत इतिहास रचा जा रहा है। आज धर्म भी होगा, स्वाध्याय का ज्ञान भी होगा, और युवाओं का सबसे पसंदीदा खेल — <strong>क्रिकेट</strong> भी होगा!<br>
      इसीलिए हमारा नारा है: <strong>'ज्ञान का खेल, संस्कारों का मेल, आओ खेलें JAIN CRICKET, प्रश्नों के संग धर्म का संदेश!'</strong>"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "वाह सहज भैया! आज माधवगंज की यह पिच गवाह बनेगी एक अनोखे मुकाबले की —<br>
      जहाँ बल्ला लकड़ी का नहीं, विवेक का होगा... गेंद लेदर की नहीं, जैन आगम के ज्ञान की होगी... और जीत किसी ट्रॉफी की नहीं, हमारे सम्यग्ज्ञान और संस्कारों की होगी!"
    </div>
  </div>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "तो बोलिए एक बार पूरे माधवगंज के जोश के साथ —<br>
      <strong>'प्रश्नों की पिच पर...?'</strong> <span class="stage-note" style="display:inline;">*(ऑडियंस से बुलवाएं: 'ज्ञान की जीत!')*</span> — जोर से बोलिए — <strong>'प्रश्नों की पिच पर...?'</strong> <span class="stage-note" style="display:inline;">*(ऑडियंस: 'ज्ञान की जीत!')*</span>"
    </div>
  </div>

  <!-- ACT 2: UMPIRE & COMMENTATORS -->
  <div class="act-title">⚖ अंक 2: अंपायर एवं कमेंटेटर्स का भव्य स्वागत</div>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "क्रिकेट का मैच हो और निष्पक्ष अंपायर न हो, ऐसा तो नामुमकिन है! आज के इस मैच के लिए हमने आमंत्रित किया है एक ऐसे महापुरुष को, जिनका फैसला पत्थर की लकीर है! यहाँ कोई DRS या थर्ड अंपायर काम नहीं करेगा, क्योंकि इनका ज्ञान ही सर्वोच्च न्यायालय है!<br>
      तालियों की गड़गड़ाहट से मंच पर आमंत्रित कीजिए हमारे मुख्य अंपायर — <strong>आदरणीय डॉ. सुकुमार जैन साहब</strong>!"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "स्वागत है डॉक्टर साहब! आज मैदान पर कोई नो-बॉल होगी या गूगली, वो सिर्फ आपकी पैनी नजर ही तय करेगी!<br>
      और भैया, हर चौके, छक्के और विकेट का लाइव आंखों देखा हाल सुनाने के लिए कमेंट्री बॉक्स में पधार चुके हैं — माधवगंज के दो अनमोल रत्न, जिनकी बातों में नवजोत सिद्धू वाला जोश और हर्षा भोगले जैसी गहराई है —<br>
      स्वागत कीजिए हमारे कमेंटेटर्स: <strong>श्री निर्मल जैन जी</strong> और <strong>श्री विक्की जैन जी</strong>!"
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ==================== PAGE 2: TEAMS, RULES, TOSS & GAMEPLAY ==================== -->
  <div class="act-title">🛡 अंक 3: चारों महारथी टीमों की एंट्री व परिचय (The 4 Teams)</div>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "अब वक्त आ गया है उन चार योद्धा टीमों से मिलने का, जिन्होंने स्वाध्याय की पिच पर दिन-रात अभ्यास किया है! चार टीमें, चार रंग, और एक लक्ष्य — ज्ञान की विजय!"
    </div>
  </div>

  <div class="teams-container">
    <div class="team-box team-red">
      <div class="team-name" style="color: #b91c1c;">🦁 1. सुशील के शूरवीर</div>
      <div class="team-slogan">"शेर की दहाड़, ज्ञान का प्रहार!"</div>
      <div style="font-size: 8.5pt; color: #7f1d1d; margin-top: 2px;">वीरता और ज्ञान का अद्भुत संगम। लाल रंग का जोश!</div>
    </div>
    <div class="team-box team-blue">
      <div class="team-name" style="color: #1d4ed8;">💎 2. लक्ष्मी के खजाने</div>
      <div class="team-slogan">"ज्ञान का खजाना, जीत कर ही जाना!"</div>
      <div style="font-size: 8.5pt; color: #1e3a8a; margin-top: 2px;">जिनवाणी के अमूल्य रत्नों से भरी टीम। नीला रंग!</div>
    </div>
    <div class="team-box team-green">
      <div class="team-name" style="color: #15803d;">🧘 3. साधना के साधक</div>
      <div class="team-slogan">"संयम और साधना, जीत की आराधना!"</div>
      <div style="font-size: 8.5pt; color: #14532d; margin-top: 2px;">धैर्य, एकाग्रता और अचूक उत्तर। हरा रंग!</div>
    </div>
    <div class="team-box team-gold">
      <div class="team-name" style="color: #a16207;">🛡 4. राखी के रक्षक</div>
      <div class="team-slogan">"धर्म की ढाल, शूरवीर बेमिसाल!"</div>
      <div style="font-size: 8.5pt; color: #713f12; margin-top: 2px;">संस्कारों और धर्म की रक्षा के प्रहरी। स्वर्णिम रंग!</div>
    </div>
  </div>

  <!-- ACT 4: RULES -->
  <div class="act-title">📜 अंक 4: पिच के नियम एवं स्कोरिंग प्रणाली (Rules & Scoring)</div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "खिलाड़ी तैयार, अंपायर तैयार! लेकिन पहली गेंद फेंकने से पहले जान लेते हैं आज की पिच के सुनहरे नियम:"
    </div>
  </div>

  <div class="rules-card">
    <div class="rule-item">
      <div class="rule-bullet">1</div>
      <div><strong>बॉलर vs बैटर (पर्ची सिस्टम):</strong> फील्डिंग टीम का बॉलर पर्ची निकालेगा और बैटिंग टीम के बैटर से सवाल पूछेगा। कुल 50 विषय उपलब्ध हैं।</div>
    </div>
    <div class="rule-item">
      <div class="rule-bullet">2</div>
      <div><strong>गेंदों की वैरायटी (Runs):</strong> प्रत्येक पर्ची में 3 प्रश्न हैं —<br>
        • <strong>1 रन की गेंद:</strong> सीधा, बुनियादी सवाल (सिंगल रन)।<br>
        • <strong>2 रन की गेंद:</strong> थोड़ा घुमावदार, सूझबूझ की परीक्षा (डबल रन)।<br>
        • <strong>4 या 6 रन की गेंद:</strong> आगम का गहरा स्वाध्याय प्रश्न — सीधा बाउंड्री पार शॉट!
      </div>
    </div>
    <div class="rule-item">
      <div class="rule-bullet">3</div>
      <div><strong>समय सीमा (Timer):</strong> प्रत्येक प्रश्न का उत्तर सोचने के लिए केवल <strong>30 सेकंड</strong> का समय मिलेगा।</div>
    </div>
    <div class="rule-item">
      <div class="rule-bullet">4</div>
      <div><strong>आउट एवं उत्तम क्षमा:</strong> गलत उत्तर देने पर बैटर आउट! लेकिन याद रहे — आज <em>उत्तम क्षमा</em> का दिन है, इसलिए मुस्कुराते हुए पवेलियन लौटना है!</div>
    </div>
    <div class="rule-item" style="background: #fee2e2; border: 1px solid #f87171; border-radius: 6px; padding: 5px 8px; margin-top: 4px;">
      <div class="rule-bullet" style="background: #dc2626;">⚾</div>
      <div>
        <strong style="color: #991b1b;">धमाकेदार ट्विस्ट: नो बॉल (No-Ball) एवं फ्री-हिट:</strong><br>
        यदि 'नो बॉल' पर्ची निकली, तो बैटिंग टीम को तुरंत <strong>1 रन मुफ्त</strong> मिलेगा! साथ ही मिलेगी <strong>'ज्ञान पहेली (फ्री-हिट)'</strong> — यदि बैटर ने पहेली का सही उत्तर दिया, तो <strong>+2 बोनस रन</strong> और मिलेंगे! (कुल 3 रनों का जैकपॉट!)
      </div>
    </div>
  </div>

  <!-- ACT 5: TOSS -->
  <div class="act-title">🪙 अंक 5: टॉस एवं खेल का शुभारंभ</div>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "नियम स्पष्ट हैं! अब आमंत्रित करते हैं दोनों कप्तानों को टॉस के लिए। अंपायर डॉ. सुकुमार जैन साहब, सिक्का उछाला जाए!<br>
      <span class="stage-note" style="display:inline;">*(सिक्का उछलता है)*</span> — कॉल आया है... और टॉस जीता है <strong>[विजेता टीम का नाम]</strong> ने! बताइए कप्तान साहब, आप पहले बैटिंग चुनेंगे या फील्डिंग?"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "फैसला हो चुका है! फील्डर अपनी पोजीशन ले लें, बैटर क्रीज पर आ जाएं! स्कोरर तैयार, कमेंटेटर्स तैयार!<br>
      माधवगंज की जनता, एक बार जोरदार तालियों के साथ पहली गेंद का स्वागत कीजिए!"
    </div>
  </div>

  <div class="page-break"></div>

  <!-- ==================== PAGE 3: LIVE CUES, SHAYARIS, AND FINALE ==================== -->
  <div class="act-title">🎙 अंक 6: मैच के दौरान संचालक व कमेंट्री डायलॉग्स (Live Anchoring Situations)</div>

  <div class="situation-grid">
    <div class="situation-box">
      <div class="situation-header">⚡ स्थिति 1: 1 या 2 रन का सही उत्तर</div>
      <div class="situation-punch">
        <strong>सहज:</strong> "गेंद को गैप में धकेला, बढ़िया रनिंग बिटवीन द विकेट्स! खाता खुला!"<br>
        <strong>अमन:</strong> "बिल्कुल! ठोस शुरुआत, स्वाध्याय की पूरी तैयारी दिख रही है!"
      </div>
    </div>

    <div class="situation-box">
      <div class="situation-header">🚀 स्थिति 2: 4 या 6 रन का कठिन सवाल हल</div>
      <div class="situation-punch">
        <strong>सहज:</strong> "ओहोहो! गेंद दर्शकों की दीर्घा में... शानदार सिक्सर! पूरे 6 रन!"<br>
        <strong>अमन:</strong> "विरोधी बॉलर के पसीने छूट गए! कमेंट्री बॉक्स से निर्मल जी क्या कहेंगे?"
      </div>
    </div>

    <div class="situation-box" style="border-color: #fca5a5; background: #fffafa;">
      <div class="situation-header" style="color: #dc2626;">⚾ स्थिति 3: नो-बॉल की पर्ची निकली!</div>
      <div class="situation-punch">
        <strong>सहज:</strong> "सायरन बज चुका है... अंपायर का इशारा: <em>नो बॉल! 1 रन फ्री!</em>"<br>
        <strong>अमन:</strong> "और अब है फ्री-हिट ज्ञान पहेली! अगर बूझ ली तो मिलेंगे पूरे 2 बोनस रन!"
      </div>
    </div>

    <div class="situation-box">
      <div class="situation-header">☝ स्थिति 4: गलत उत्तर (Wicket / Out)</div>
      <div class="situation-punch">
        <strong>सहज:</strong> "क्लीन बोल्ड! मिडिल स्टंप हवा में! लेकिन कोई बात नहीं..."<br>
        <strong>अमन:</strong> "आज उत्तम क्षमा का दिन है! मुस्कुराकर डगआउट लौटिए, शानदार खेल दिखाया!"
      </div>
    </div>
  </div>

  <!-- AUDIENCE ROUND -->
  <div class="dialogue-card sahaj" style="margin-top: 4px;">
    <span class="speaker-badge badge-sahaj">सहज भैया (ऑडियंस कैच राउंड)</span>
    <div class="dialogue-text">
      "खिलाड़ियों ने तो दम दिखाया, अब बारी है हमारे माधवगंज के दर्शकों की — <strong>'ऑडियंस कैच'</strong>!<br>
      यह गूगली गेंद जा रही है सीधे दर्शकों के पाले में! जो भी सबसे पहले हाथ उठाकर सही उत्तर देगा, उसे मिलेगा स्पेशल पुरस्कार!"
    </div>
  </div>

  <!-- ACT 7: SHAYARIS & UTTAM KSHAMA -->
  <div class="act-title">🌟 अंक 7: उत्तम क्षमा धर्म विशेष पंक्तियाँ एवं शायरियां</div>

  <div class="shayari-card">
    <div class="shayari-text">
      "क्रिकेट की पिच पर रन आउट हो सकते हैं आप, मगर क्षमा के मार्ग पर कभी न होगा पश्चाताप!<br>
      गलती अगर विरोधी भी करे तो मुस्कुरा कर गले लगाइए,<br>
      आज उत्तम क्षमा का दिन है, पूरे माधवगंज में मैत्री की खुशबू फैलाइए!"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन</span>
    <div class="dialogue-text">
      "तीर्थंकर महावीर ने कहा है: <em>'खामेमि सव्वजीवे सव्वे जीवा खमंतु मे।'</em><br>
      बल्ले से जो लगे वो सिर्फ बाउंड्री कहलाती है, पर दिल में जो क्षमा हो वो आत्मा को सिद्धशिला तक ले जाती है!"
    </div>
  </div>

  <!-- ACT 8: FINALE -->
  <div class="act-title">🏆 अंक 8: समापन, पुरस्कार वितरण एवं आभार (Grand Finale)</div>

  <span class="stage-note">*(मैच समाप्ति की घोषणा। स्कोरर से अंतिम स्कोरकार्ड सहज भैया के हाथ में)*</span>

  <div class="dialogue-card sahaj">
    <span class="speaker-badge badge-sahaj">सहज भैया</span>
    <div class="dialogue-text">
      "और इसी के साथ इस ऐतिहासिक मुकाबले की अंतिम गेंद संपन्न हुई! क्या मुकाबला था! ज्ञान, उत्साह और संस्कारों की ऐसी धारा बही कि हर कोई मंत्रमुग्ध हो गया!<br>
      अब वक्त है आज के विजेता की घोषणा का! मैं मंच पर सादर आमंत्रित करता हूँ हमारे आदरणीय अंपायर <strong>डॉ. सुकुमार जैन साहब</strong> को, वे आएं और विजेता टीम की घोषणा करें!"
    </div>
  </div>

  <div class="dialogue-card umpire">
    <span class="speaker-badge badge-umpire">अंपायर: डॉ. सुकुमार जैन</span>
    <div class="dialogue-text">
      "आज सभी टीमों ने आगम के ज्ञान का उत्कृष्ट प्रदर्शन किया। लेकिन अंकों के आधार पर आज के मैच की उपविजेता टीम रही — <strong>[उपविजेता टीम]</strong> और विजेता घोषित की जाती है — <strong>[विजेता टीम]</strong>!"
    </div>
  </div>

  <div class="dialogue-card aman">
    <span class="speaker-badge badge-aman">अमन (आभार प्रदर्शन)</span>
    <div class="dialogue-text">
      "बधाई हो विजेता टीम को! और याद रखें — जैन क्रिकेट में कोई हारता नहीं, या तो जीतता है या सीखता है!<br>
      हम हृदय से आभारी हैं हमारे अंपायर <strong>डॉ. सुकुमार जैन साहब</strong> के, ऊर्जावान कमेंटेटर्स <strong>निर्मल जी व विक्की जी</strong> के, चारों महारथी टीमों के, और सबसे बढ़कर आप सभी प्रिय दर्शकों के, जिनकी तालियों ने इस शाम को अविस्मरणीय बना दिया!"
    </div>
  </div>

  <div class="dialogue-card sahaj" style="background: #fefce8; border-left-color: #f59e0b;">
    <span class="speaker-badge" style="background: #fde68a; color: #78350f;">सहज भैया एवं अमन (एक साथ)</span>
    <div class="dialogue-text">
      "आज दशलक्षण पर्व का पहला दिन है, इसलिए संचालन में या खेल के दौरान जाने-अनजाने में किसी के भी दिल को ठेस पहुंची हो, तो मन, वचन, काय से —<br>
      <strong>'उत्तम क्षमा! मिच्छामि दुक्कड़म्!'</strong><br>
      कल फिर मिलेंगे दूसरे दिन एक नए मुकाबले के साथ! तब तक के लिए — <strong>जय जिनेंद्र! जय महावीर! भारत माता की जय!</strong>"
    </div>
  </div>

</body>
</html>`;

fs.writeFileSync('script_print.html', htmlContent, 'utf-8');
console.log('Generated script_print.html');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none']
  });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve('script_print.html'), { waitUntil: 'networkidle0' });
  
  await page.pdf({
    path: 'Jain_Cricket_Host_Script.pdf',
    format: 'A4',
    printBackground: true,
    margin: {
      top: '10mm',
      right: '12mm',
      bottom: '12mm',
      left: '12mm'
    }
  });

  await browser.close();
  console.log('Generated Jain_Cricket_Host_Script.pdf successfully!');
})();
