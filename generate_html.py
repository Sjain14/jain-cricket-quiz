import json

with open('quiz_data.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

with open('no_ball_paheliyan.json', 'r', encoding='utf-8') as f:
    no_ball_data = json.load(f)

quiz_json_str = json.dumps(quiz_data, ensure_ascii=False)
noball_json_str = json.dumps(no_ball_data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="hi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>🏏 जैन क्रिकेट क्विज़ (Jain Cricket Quiz) - 45 विषय व नो बॉल</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --font-dev: 'Noto Sans Devanagari', 'Outfit', sans-serif;
      --font-en: 'Outfit', sans-serif;

      /* Dark Theme */
      --bg-main: #0a0e17;
      --bg-surface: #111827;
      --bg-surface-elevated: #1a2234;
      --bg-surface-hover: #232e47;
      --border-subtle: #1f293d;
      --border-accent: #334155;
      
      --text-primary: #f1f5f9;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      
      --accent-saffron: #f59e0b;
      --accent-saffron-dark: #d97706;
      --accent-saffron-glow: rgba(245, 158, 11, 0.2);
      
      --run1-color: #38bdf8;
      --run1-bg: rgba(56, 189, 248, 0.1);
      --run1-border: rgba(56, 189, 248, 0.3);
      
      --run2-color: #34d399;
      --run2-bg: rgba(52, 211, 153, 0.1);
      --run2-border: rgba(52, 211, 153, 0.3);
      
      --run4-color: #c084fc;
      --run4-bg: rgba(192, 132, 252, 0.1);
      --run4-border: rgba(192, 132, 252, 0.3);
      
      --run6-color: #fb923c;
      --run6-bg: rgba(251, 146, 60, 0.12);
      --run6-border: rgba(251, 146, 60, 0.35);

      --noball-color: #f43f5e;
      --noball-bg: rgba(244, 63, 94, 0.12);
      --noball-border: rgba(244, 63, 94, 0.35);

      --ans-bg: rgba(255, 255, 255, 0.04);
      --ans-border: rgba(255, 255, 255, 0.08);

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    [data-theme="light"] {{
      --bg-main: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f1f5f9;
      --bg-surface-hover: #e2e8f0;
      --border-subtle: #e2e8f0;
      --border-accent: #cbd5e1;
      
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      
      --accent-saffron: #d97706;
      --accent-saffron-dark: #b45309;
      --accent-saffron-glow: rgba(217, 119, 6, 0.15);
      
      --run1-color: #0284c7;
      --run1-bg: #f0f9ff;
      --run1-border: #bae6fd;
      
      --run2-color: #059669;
      --run2-bg: #ecfdf5;
      --run2-border: #a7f3d0;
      
      --run4-color: #7c3aed;
      --run4-bg: #f5f3ff;
      --run4-border: #ddd6fe;
      
      --run6-color: #ea580c;
      --run6-bg: #fff7ed;
      --run6-border: #fed7aa;

      --noball-color: #e11d48;
      --noball-bg: #fff1f2;
      --noball-border: #fecdd3;

      --ans-bg: #f8fafc;
      --ans-border: #e2e8f0;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 10px rgba(0, 0, 0, 0.08);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      max-width: 100%;
      overflow-x: hidden !important;
    }}

    body {{
      font-family: var(--font-dev);
      background-color: var(--bg-main);
      color: var(--text-primary);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.6;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    /* HEADER */
    .app-header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(12px);
      box-shadow: var(--shadow-sm);
    }}

    .header-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-sizing: border-box;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      user-select: none;
    }}

    .brand-icon {{
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #f59e0b, #ea580c);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 3px 10px rgba(245, 158, 11, 0.35);
      flex-shrink: 0;
    }}

    .brand-text h1 {{
      font-size: 1.2rem;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-text p {{
      font-size: 0.75rem;
      color: var(--text-secondary);
      font-family: var(--font-en);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 14px;
      font-size: 0.88rem;
      font-weight: 600;
      font-family: var(--font-dev);
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      color: var(--text-primary);
      cursor: pointer;
      transition: background-color 0.15s ease, border-color 0.15s ease;
      user-select: none;
      box-sizing: border-box;
    }}

    .btn:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--border-accent);
    }}

    .btn:active {{
      transform: scale(0.98);
    }}

    .btn-icon-only {{
      width: 38px;
      height: 38px;
      padding: 0;
      border-radius: var(--radius-sm);
    }}

    .btn-noball {{
      background: var(--noball-bg);
      border: 1px solid var(--noball-border);
      color: var(--noball-color);
      font-weight: 700;
    }}
    .btn-noball:hover {{
      background: var(--noball-color);
      color: #ffffff;
    }}

    .btn-primary {{
      background: var(--accent-saffron);
      color: #ffffff;
      border: 1px solid var(--accent-saffron-dark);
      font-weight: 700;
    }}
    .btn-primary:hover {{
      background: #fbbf24;
      color: #0f172a;
    }}

    .hamburger-btn {{
      display: none;
      background: var(--bg-surface-elevated);
      border: 1.5px solid var(--accent-saffron);
      color: var(--accent-saffron);
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      font-weight: 700;
      font-size: 0.9rem;
      gap: 6px;
    }}

    /* MAIN CONTAINER */
    .app-main {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 20px 16px;
      display: flex;
      gap: 20px;
      flex: 1;
      width: 100%;
      box-sizing: border-box;
      overflow-x: hidden !important;
    }}

    /* LEFT PANEL */
    .content-panel {{
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    /* TOPIC HERO */
    .topic-hero {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}

    .topic-meta-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .sprint-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      font-size: 0.8rem;
      font-family: var(--font-en);
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 9999px;
    }}

    .topic-count-badge {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-family: var(--font-en);
      font-weight: 600;
    }}

    .topic-title-wrapper {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 14px;
      flex-wrap: wrap;
    }}

    .topic-number-badge {{
      background: var(--accent-saffron);
      color: #ffffff;
      font-family: var(--font-en);
      font-weight: 800;
      font-size: 1.25rem;
      padding: 5px 14px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}

    .topic-title {{
      font-size: 1.7rem;
      font-weight: 800;
      color: var(--text-primary);
      line-height: 1.25;
    }}

    .topic-nav-strip {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
      flex-wrap: wrap;
    }}

    .nav-btn {{
      padding: 8px 16px;
      font-size: 0.9rem;
      font-weight: 600;
    }}

    .random-btn {{
      background: rgba(245, 158, 11, 0.12);
      border-color: rgba(245, 158, 11, 0.3);
      color: var(--accent-saffron);
    }}
    .random-btn:hover {{
      background: rgba(245, 158, 11, 0.22);
      border-color: var(--accent-saffron);
    }}

    /* QUESTIONS LIST */
    .questions-container {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .q-card {{
      background: var(--bg-surface);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
    }}

    .q-card-run1 {{
      border-left: 5px solid var(--run1-color);
    }}
    .q-card-run2 {{
      border-left: 5px solid var(--run2-color);
    }}
    .q-card-run4 {{
      border-left: 5px solid var(--run4-color);
    }}
    .q-card-run6 {{
      border-left: 5px solid var(--run6-color);
    }}

    .q-header {{
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.02);
    }}

    .run-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.88rem;
      font-weight: 800;
      font-family: var(--font-en);
      padding: 4px 12px;
      border-radius: 9999px;
    }}

    .run-badge-1 {{
      background: var(--run1-bg);
      color: var(--run1-color);
      border: 1px solid var(--run1-border);
    }}

    .run-badge-2 {{
      background: var(--run2-bg);
      color: var(--run2-color);
      border: 1px solid var(--run2-border);
    }}

    .run-badge-4 {{
      background: var(--run4-bg);
      color: var(--run4-color);
      border: 1px solid var(--run4-border);
    }}

    .run-badge-6 {{
      background: var(--run6-bg);
      color: var(--run6-color);
      border: 1px solid var(--run6-border);
    }}

    .q-body {{
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .q-text-label {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }}

    .q-text {{
      font-size: 1.12rem;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.6;
    }}

    .ans-box {{
      background: var(--ans-bg);
      border: 1px solid var(--ans-border);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .ans-label {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--accent-saffron);
    }}

    .ans-text {{
      font-size: 1.08rem;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.55;
    }}

    /* RIGHT PANEL - QUESTION NUMBERS GRID */
    .sidebar-panel {{
      width: 320px;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      gap: 14px;
      box-sizing: border-box;
    }}

    .sidebar-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 16px;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 76px;
      max-height: calc(100vh - 96px);
      display: flex;
      flex-direction: column;
      overflow-x: hidden !important;
      box-sizing: border-box;
      width: 100%;
    }}

    .sidebar-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .sidebar-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .total-count-pill {{
      background: var(--bg-surface-elevated);
      color: var(--accent-saffron);
      font-family: var(--font-en);
      font-weight: 700;
      font-size: 0.78rem;
      padding: 2px 8px;
      border-radius: 9999px;
      border: 1px solid var(--border-subtle);
    }}

    /* TOPIC PREVIEW BAR */
    .topic-preview-bar {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 8px 12px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent-saffron);
      margin-bottom: 10px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      box-sizing: border-box;
    }}

    /* VIEW MODE TOGGLE */
    .view-mode-bar {{
      display: flex;
      gap: 6px;
      margin-bottom: 10px;
      width: 100%;
      box-sizing: border-box;
    }}

    .view-tab-btn {{
      flex: 1;
      padding: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      color: var(--text-secondary);
      cursor: pointer;
      text-align: center;
      transition: background-color 0.15s ease;
      box-sizing: border-box;
    }}

    .view-tab-btn.active {{
      background: var(--accent-saffron);
      color: #ffffff;
      border-color: var(--accent-saffron);
    }}

    /* SEARCH INPUT */
    .search-box {{
      position: relative;
      margin-bottom: 10px;
      width: 100%;
      box-sizing: border-box;
    }}

    .search-input {{
      width: 100%;
      padding: 8px 12px 8px 34px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-primary);
      font-family: var(--font-dev);
      font-size: 0.88rem;
      outline: none;
      box-sizing: border-box;
      transition: border-color 0.15s ease;
    }}

    .search-input:focus {{
      border-color: var(--accent-saffron);
    }}

    .search-icon {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      font-size: 13px;
    }}

    /* NUMBERS GRID CONTAINER */
    .numbers-grid-container {{
      overflow-y: auto;
      overflow-x: hidden !important;
      scrollbar-gutter: stable;
      flex: 1;
      width: 100%;
      box-sizing: border-box;
    }}

    .numbers-grid {{
      display: grid;
      grid-template-columns: repeat(5, minmax(0, 1fr));
      gap: 6px;
      width: 100%;
      box-sizing: border-box;
      overflow-x: hidden !important;
    }}

    .num-btn {{
      height: 42px;
      width: 100%;
      min-width: 0;
      padding: 0;
      margin: 0;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-primary);
      font-family: var(--font-en);
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      user-select: none;
      box-sizing: border-box;
      transition: background-color 0.15s, border-color 0.15s;
    }}

    .num-btn:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--accent-saffron);
    }}

    .num-btn.active {{
      background: var(--accent-saffron) !important;
      color: #ffffff !important;
      border-color: var(--accent-saffron-dark) !important;
      font-weight: 800;
    }}

    /* LIST VIEW */
    .topics-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      width: 100%;
      box-sizing: border-box;
    }}

    .list-item-btn {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-primary);
      cursor: pointer;
      text-align: left;
      width: 100%;
      box-sizing: border-box;
      transition: background-color 0.15s, border-color 0.15s;
    }}

    .list-item-btn:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--accent-saffron);
    }}

    .list-item-btn.active {{
      background: var(--accent-saffron) !important;
      color: #ffffff !important;
      border-color: var(--accent-saffron-dark) !important;
    }}

    .list-item-num {{
      font-family: var(--font-en);
      font-weight: 800;
      font-size: 0.9rem;
      background: rgba(0, 0, 0, 0.2);
      padding: 2px 6px;
      border-radius: 4px;
      min-width: 28px;
      text-align: center;
      flex-shrink: 0;
    }}

    .list-item-title {{
      font-size: 0.9rem;
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
      min-width: 0;
    }}

    /* MODAL OVERLAY & DRAWERS */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      z-index: 100;
      opacity: 0;
      transition: opacity 0.2s ease;
    }}

    .modal-overlay.open {{
      display: block;
      opacity: 1;
    }}

    .mobile-modal {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      width: 100%;
      max-width: 100%;
      max-height: 82vh;
      background: var(--bg-surface);
      border-top-left-radius: var(--radius-lg);
      border-top-right-radius: var(--radius-lg);
      border-top: 1px solid var(--border-accent);
      padding: 14px 14px 24px 14px;
      z-index: 101;
      display: flex;
      flex-direction: column;
      box-shadow: 0 -8px 30px rgba(0, 0, 0, 0.5);
      transform: translateY(100%);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      overflow-x: hidden !important;
      box-sizing: border-box;
    }}

    .mobile-modal.open {{
      transform: translateY(0);
    }}

    .modal-drag-pill {{
      width: 36px;
      height: 4px;
      background: var(--text-muted);
      border-radius: 9999px;
      margin: 0 auto 10px auto;
      opacity: 0.5;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
      width: 100%;
      box-sizing: border-box;
    }}

    .modal-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .modal-close-btn {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-secondary);
      font-size: 1rem;
      cursor: pointer;
    }}

    .mobile-grid-wrapper {{
      overflow-y: auto;
      overflow-x: hidden !important;
      scrollbar-gutter: stable;
      flex: 1;
      padding-bottom: 12px;
      width: 100%;
      box-sizing: border-box;
    }}

    /* NO-BALL MODAL */
    .noball-modal-dialog {{
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.95);
      width: 92%;
      max-width: 680px;
      max-height: 88vh;
      background: var(--bg-surface);
      border: 1px solid var(--noball-border);
      border-radius: var(--radius-lg);
      padding: 20px;
      z-index: 102;
      display: none;
      flex-direction: column;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
      box-sizing: border-box;
      transition: transform 0.2s ease, opacity 0.2s ease;
      opacity: 0;
    }}

    .noball-modal-dialog.open {{
      display: flex;
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }}

    .noball-modal-list {{
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding-right: 4px;
      margin-top: 10px;
    }}

    .noball-card-ui {{
      background: var(--bg-surface-elevated);
      border: 1.5px dashed var(--noball-color);
      border-radius: var(--radius-md);
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .noball-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 6px;
    }}

    .noball-card-badge {{
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--noball-color);
    }}

    .noball-rule-tag {{
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent-saffron);
      background: rgba(245, 158, 11, 0.12);
      padding: 2px 6px;
      border-radius: 4px;
    }}

    .noball-q {{
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.5;
    }}

    .noball-ans {{
      background: var(--ans-bg);
      border: 1px solid var(--ans-border);
      border-radius: var(--radius-sm);
      padding: 8px 12px;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--accent-saffron);
    }}

    /* MOBILE FLOATING BOTTOM BAR */
    .mobile-bottom-nav {{
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      padding: 10px 14px;
      z-index: 40;
      box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.3);
      backdrop-filter: blur(12px);
      box-sizing: border-box;
    }}

    .mobile-nav-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      max-width: 600px;
      margin: 0 auto;
      box-sizing: border-box;
    }}

    .mobile-nav-btn {{
      flex: 1;
      padding: 9px 6px;
      font-size: 0.88rem;
      font-weight: 700;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      box-sizing: border-box;
    }}

    /* RESPONSIVE MEDIA QUERIES */
    @media (max-width: 880px) {{
      .sidebar-panel {{
        display: none !important;
      }}
      .hamburger-btn {{
        display: inline-flex !important;
      }}
      .app-main {{
        padding: 12px 12px 76px 12px;
      }}
      .topic-hero {{
        padding: 16px;
      }}
      .topic-title {{
        font-size: 1.35rem;
      }}
      .topic-number-badge {{
        font-size: 1.05rem;
        padding: 4px 10px;
      }}
      .q-body {{
        padding: 14px;
      }}
      .q-text {{
        font-size: 1.02rem;
      }}
      .ans-text {{
        font-size: 0.98rem;
      }}
      .mobile-bottom-nav {{
        display: block;
      }}
      .topic-nav-strip {{
        display: none;
      }}
      .brand-text p {{
        display: none;
      }}
    }}

    @media (max-width: 440px) {{
      .header-container {{
        padding: 8px 10px;
      }}
      .brand-icon {{
        width: 36px;
        height: 36px;
        font-size: 18px;
      }}
      .brand-text h1 {{
        font-size: 1.05rem;
      }}
      .num-btn {{
        height: 40px;
        font-size: 0.92rem;
      }}
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header class="app-header">
    <div class="header-container">
      <div class="brand" onclick="goToTopicIndex(0)" title="जैन क्रिकेट क्विज़">
        <div class="brand-icon">🏏</div>
        <div class="brand-text">
          <h1>जैन क्रिकेट क्विज़</h1>
          <p>45 Topics • 135 Questions • 6 No-Ball Riddles</p>
        </div>
      </div>

      <div class="header-actions">
        <!-- No-Ball Button -->
        <button class="btn btn-noball" onclick="toggleNoBallModal(true)" title="नो बॉल ज्ञान पहेलियाँ">
          <span>⚾ नो बॉल</span>
        </button>

        <!-- Mobile Button to open Numbers Modal -->
        <button id="mobileMenuBtn" class="btn hamburger-btn" aria-label="क्वेश्चन चुनें" onclick="toggleMobileModal(true)">
          <span>☰</span>
          <span>विषय <span id="headerTopicNumBadge">1</span></span>
        </button>

        <!-- Theme Toggle -->
        <button id="themeToggleBtn" class="btn btn-icon-only" onclick="toggleTheme()" title="थीम बदलें (Dark / Light)">
          🌙
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN WRAPPER -->
  <main class="app-main">
    
    <!-- LEFT PANEL: TOPIC & QUESTIONS -->
    <section class="content-panel">

      <!-- TOPIC HERO -->
      <div class="topic-hero">
        <div class="topic-meta-bar">
          <span id="sprintBadge" class="sprint-badge">Sprint 1</span>
          <span id="progressIndicator" class="topic-count-badge">विषय 1 / 45</span>
        </div>

        <div class="topic-title-wrapper">
          <div id="topicBadge" class="topic-number-badge">विषय 1</div>
          <h2 id="topicTitle" class="topic-title">कषाय</h2>
        </div>

        <!-- Desktop Navigation Strip -->
        <div class="topic-nav-strip">
          <button id="prevBtn" class="btn nav-btn" onclick="prevTopic()">
            ← पिछला (Prev)
          </button>
          
          <button class="btn random-btn" onclick="selectRandomTopic()" title="पर्ची / रैंडम प्रश्न">
            🎲 रैंडम पर्ची (Random)
          </button>

          <button class="btn btn-noball" onclick="toggleNoBallModal(true)" title="नो बॉल ज्ञान पहेलियाँ">
            ⚾ नो बॉल (6 पहेलियाँ)
          </button>

          <button id="nextBtn" class="btn btn-primary nav-btn" onclick="nextTopic()">
            अगला (Next) →
          </button>
        </div>
      </div>

      <!-- QUESTIONS LIST (1 Run, 2 Run, 4 or 6 Run) -->
      <div id="questionsContainer" class="questions-container">
        <!-- Rendered dynamically -->
      </div>

    </section>

    <!-- RIGHT PANEL: QUESTION NUMBERS (DESKTOP) -->
    <aside class="sidebar-panel">
      <div class="sidebar-card">
        <div class="sidebar-header">
          <div class="sidebar-title">
            <span>📋 सभी प्रश्न</span>
            <span class="total-count-pill">45 विषय</span>
          </div>
          <button class="btn btn-noball" style="padding: 3px 8px; font-size: 0.75rem;" onclick="toggleNoBallModal(true)">
            ⚾ नो बॉल
          </button>
        </div>

        <!-- Topic Hover / Active Preview -->
        <div id="desktopPreviewBar" class="topic-preview-bar">
          विषय 1: कषाय
        </div>

        <!-- Mode Toggle: Grid or List -->
        <div class="view-mode-bar">
          <button id="modeGridBtn" class="view-tab-btn active" onclick="setViewMode('grid')">🔢 ग्रिड (Grid)</button>
          <button id="modeListBtn" class="view-tab-btn" onclick="setViewMode('list')">📝 सूची (List)</button>
        </div>

        <!-- Search / Filter -->
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input 
            type="text" 
            id="desktopSearchInput" 
            class="search-input" 
            placeholder="विषय या नंबर खोजें..." 
            oninput="handleSearch(this.value)"
          />
        </div>

        <!-- Numbers Grid / List Container -->
        <div id="desktopContainer" class="numbers-grid-container">
          <div id="desktopNumbersGrid" class="numbers-grid"></div>
          <div id="desktopTopicsList" class="topics-list" style="display: none;"></div>
        </div>
      </div>
    </aside>

  </main>

  <!-- MOBILE BOTTOM FLOATING NAVIGATION -->
  <div class="mobile-bottom-nav">
    <div class="mobile-nav-row">
      <button class="btn mobile-nav-btn" onclick="prevTopic()">
        ← पिछला
      </button>
      <button class="btn mobile-nav-btn random-btn" onclick="selectRandomTopic()">
        🎲 पर्ची
      </button>
      <button class="btn mobile-nav-btn btn-noball" onclick="toggleNoBallModal(true)">
        ⚾ नो बॉल
      </button>
      <button class="btn hamburger-btn" style="display:inline-flex; flex:1;" onclick="toggleMobileModal(true)">
        ☰ # <span id="mobileTopicNumBtn">1</span>
      </button>
      <button class="btn btn-primary mobile-nav-btn" onclick="nextTopic()">
        अगला →
      </button>
    </div>
  </div>

  <!-- MOBILE NUMBERS MODAL / DRAWER -->
  <div id="mobileModalOverlay" class="modal-overlay" onclick="closeAllModals()"></div>
  <div id="mobileModal" class="mobile-modal">
    <div class="modal-drag-pill"></div>
    <div class="modal-header">
      <div class="modal-title">
        <span>🔢</span>
        <span>क्वेश्चन चुनें (1 - 50)</span>
      </div>
      <button class="modal-close-btn" onclick="toggleMobileModal(false)" aria-label="बंद करें">✕</button>
    </div>

    <!-- Active Topic Preview in Modal -->
    <div id="mobilePreviewBar" class="topic-preview-bar">
      वर्तमान: विषय 1 - कषाय
    </div>

    <!-- Mobile Mode Toggle -->
    <div class="view-mode-bar">
      <button id="mobileModeGridBtn" class="view-tab-btn active" onclick="setMobileViewMode('grid')">🔢 ग्रिड (Grid)</button>
      <button id="mobileModeListBtn" class="view-tab-btn" onclick="setMobileViewMode('list')">📝 सूची (List)</button>
    </div>

    <!-- Search in modal -->
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input 
        type="text" 
        id="mobileSearchInput" 
        class="search-input" 
        placeholder="नंबर या विषय का नाम खोजें..." 
        oninput="handleSearch(this.value)"
      />
    </div>

    <div class="mobile-grid-wrapper">
      <div id="mobileNumbersGrid" class="numbers-grid"></div>
      <div id="mobileTopicsList" class="topics-list" style="display: none;"></div>
    </div>
  </div>

  <!-- NO-BALL MODAL DIALOG (FOR HOST VIEWING ANSWERS) -->
  <div id="noBallModal" class="noball-modal-dialog">
    <div class="modal-header">
      <div class="modal-title" style="color: var(--noball-color);">
        <span>⚾</span>
        <span>नो बॉल (No Ball) - 6 ज्ञान पहेलियाँ</span>
      </div>
      <button class="modal-close-btn" onclick="toggleNoBallModal(false)" aria-label="बंद करें">✕</button>
    </div>
    <div style="font-size: 0.82rem; color: var(--text-secondary); padding-bottom: 6px; border-bottom: 1px solid var(--border-subtle);">
      📌 <b>नियम:</b> नो बॉल = 1 रन | पहेली का सही उत्तर देने पर = 2 रन (बोनस / फ्री-हिट)
    </div>
    <div id="noBallModalList" class="noball-modal-list">
      <!-- Rendered dynamically -->
    </div>
  </div>

  <!-- EMBEDDED DATA SCRIPT -->
  <script>
    const QUIZ_DATA = {quiz_json_str};
    const NO_BALL_DATA = {noball_json_str};

    // APPLICATION STATE
    let currentIndex = 0;
    let searchQuery = '';
    let currentViewMode = 'grid';
    let mobileViewMode = 'grid';

    // DOM ELEMENTS
    const topicBadge = document.getElementById('topicBadge');
    const topicTitle = document.getElementById('topicTitle');
    const sprintBadge = document.getElementById('sprintBadge');
    const progressIndicator = document.getElementById('progressIndicator');
    const questionsContainer = document.getElementById('questionsContainer');
    const desktopPreviewBar = document.getElementById('desktopPreviewBar');
    const mobilePreviewBar = document.getElementById('mobilePreviewBar');
    const headerTopicNumBadge = document.getElementById('headerTopicNumBadge');
    const mobileTopicNumBtn = document.getElementById('mobileTopicNumBtn');
    
    const desktopNumbersGrid = document.getElementById('desktopNumbersGrid');
    const desktopTopicsList = document.getElementById('desktopTopicsList');
    const mobileNumbersGrid = document.getElementById('mobileNumbersGrid');
    const mobileTopicsList = document.getElementById('mobileTopicsList');
    
    const mobileModalOverlay = document.getElementById('mobileModalOverlay');
    const mobileModal = document.getElementById('mobileModal');
    const noBallModal = document.getElementById('noBallModal');
    const noBallModalList = document.getElementById('noBallModalList');
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    // INITIALIZATION
    function initApp() {{
      const savedTheme = localStorage.getItem('jain_quiz_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      updateThemeIcon(savedTheme);

      const savedIdx = parseInt(localStorage.getItem('jain_quiz_idx'), 10);
      if (!isNaN(savedIdx) && savedIdx >= 0 && savedIdx < QUIZ_DATA.length) {{
        currentIndex = savedIdx;
      }}

      renderAllSelectors();
      renderCurrentTopic();
      renderNoBallModal();
      setupKeyboardNavigation();
    }}

    // RENDER CURRENT TOPIC
    function renderCurrentTopic() {{
      const topic = QUIZ_DATA[currentIndex];
      if (!topic) return;

      localStorage.setItem('jain_quiz_idx', currentIndex);

      topicBadge.textContent = `विषय ${{topic.number}}`;
      topicTitle.textContent = topic.title;
      sprintBadge.textContent = topic.sprint || `Sprint`;
      progressIndicator.textContent = `विषय ${{currentIndex + 1}} / ${{QUIZ_DATA.length}}`;
      if (headerTopicNumBadge) headerTopicNumBadge.textContent = topic.number;
      if (mobileTopicNumBtn) mobileTopicNumBtn.textContent = topic.number;
      if (desktopPreviewBar) desktopPreviewBar.textContent = `विषय ${{topic.number}}: ${{topic.title}}`;
      if (mobilePreviewBar) mobilePreviewBar.textContent = `वर्तमान: विषय ${{topic.number}} - ${{topic.title}}`;

      if (prevBtn) prevBtn.disabled = currentIndex === 0;
      if (nextBtn) nextBtn.disabled = currentIndex === QUIZ_DATA.length - 1;

      let html = '';
      topic.questions.forEach(q => {{
        const runs = q.runs;
        let runBadgeClass = `run-badge-${{runs}}`;
        let cardClass = `q-card-run${{runs}}`;
        let runLabel = '';

        if (runs === 1) {{
          runLabel = '🏏 1 RUN (एक रन)';
        }} else if (runs === 2) {{
          runLabel = '🏏🏏 2 RUNS (दो रन)';
        }} else if (runs === 4) {{
          runLabel = '💥 4 RUNS (चौका)';
        }} else if (runs === 6) {{
          runLabel = '🚀 6 RUNS (छक्का)';
        }} else {{
          runLabel = `🏏 ${{runs}} RUNS`;
        }}

        html += `
          <div class="q-card ${{cardClass}}">
            <div class="q-header">
              <span class="run-badge ${{runBadgeClass}}">${{runLabel}}</span>
            </div>
            <div class="q-body">
              <div>
                <div class="q-text-label">प्रश्न (Question):</div>
                <div class="q-text">${{escapeHtml(q.question)}}</div>
              </div>
              <div class="ans-box">
                <span class="ans-label">✨ उत्तर (Answer):</span>
                <div class="ans-text">${{escapeHtml(q.answer)}}</div>
              </div>
            </div>
          </div>
        `;
      }});

      questionsContainer.innerHTML = html;
      updateActiveSelectorUI();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // RENDER SELECTORS
    function renderAllSelectors() {{
      const filtered = QUIZ_DATA.filter(t => {{
        if (!searchQuery) return true;
        const q = searchQuery.toLowerCase().trim();
        return t.number.toString() === q || 
               t.title.toLowerCase().includes(q) ||
               (t.sprint && t.sprint.toLowerCase().includes(q));
      }});

      const makeGridHtml = () => {{
        if (filtered.length === 0) {{
          return `<div style="grid-column: 1 / -1; padding: 16px; text-align: center; color: var(--text-muted); font-size: 0.88rem;">कोई विषय नहीं मिला</div>`;
        }}
        return filtered.map(t => {{
          const realIdx = QUIZ_DATA.findIndex(item => item.number === t.number);
          const isActive = realIdx === currentIndex;
          return `
            <button 
              type="button"
              class="num-btn ${{isActive ? 'active' : ''}}" 
              onclick="goToTopicIndex(${{realIdx}})"
              onmouseenter="setPreviewHover(${{realIdx}})"
              title="विषय ${{t.number}}: ${{escapeHtml(t.title)}}"
              data-idx="${{realIdx}}"
            >
              ${{t.number}}
            </button>
          `;
        }}).join('');
      }};

      const makeListHtml = () => {{
        if (filtered.length === 0) {{
          return `<div style="padding: 16px; text-align: center; color: var(--text-muted); font-size: 0.88rem;">कोई विषय नहीं मिला</div>`;
        }}
        return filtered.map(t => {{
          const realIdx = QUIZ_DATA.findIndex(item => item.number === t.number);
          const isActive = realIdx === currentIndex;
          return `
            <button 
              type="button"
              class="list-item-btn ${{isActive ? 'active' : ''}}" 
              onclick="goToTopicIndex(${{realIdx}})"
              data-idx="${{realIdx}}"
            >
              <span class="list-item-num">${{t.number}}</span>
              <span class="list-item-title">${{escapeHtml(t.title)}}</span>
            </button>
          `;
        }}).join('');
      }};

      const gridHtml = makeGridHtml();
      const listHtml = makeListHtml();

      if (desktopNumbersGrid) desktopNumbersGrid.innerHTML = gridHtml;
      if (desktopTopicsList) desktopTopicsList.innerHTML = listHtml;
      if (mobileNumbersGrid) mobileNumbersGrid.innerHTML = gridHtml;
      if (mobileTopicsList) mobileTopicsList.innerHTML = listHtml;
    }}

    // RENDER NO-BALL MODAL
    function renderNoBallModal() {{
      if (!noBallModalList) return;
      noBallModalList.innerHTML = NO_BALL_DATA.map(nb => `
        <div class="noball-card-ui">
          <div class="noball-card-top">
            <span class="noball-card-badge">⚾ नो बॉल #${{nb.id}}</span>
            <span class="noball-rule-tag">नो बॉल: 1 रन • पहेली उत्तर: 2 रन</span>
          </div>
          <div class="noball-q">💡 <b>पहेली:</b> "${{escapeHtml(nb.paheli).replace(/\\n/g, '<br>')}}"</div>
          <div class="noball-ans">✨ <b>उत्तर:</b> ${{escapeHtml(nb.answer)}}</div>
        </div>
      `).join('');
    }}

    // UPDATE ACTIVE STATE
    function updateActiveSelectorUI() {{
      document.querySelectorAll('.num-btn').forEach(btn => {{
        const btnIdx = parseInt(btn.getAttribute('data-idx'), 10);
        btn.classList.toggle('active', btnIdx === currentIndex);
      }});

      document.querySelectorAll('.list-item-btn').forEach(btn => {{
        const btnIdx = parseInt(btn.getAttribute('data-idx'), 10);
        btn.classList.toggle('active', btnIdx === currentIndex);
      }});
    }}

    function setPreviewHover(idx) {{
      const topic = QUIZ_DATA[idx];
      if (topic && desktopPreviewBar) {{
        desktopPreviewBar.textContent = `विषय ${{topic.number}}: ${{topic.title}}`;
      }}
    }}

    function setViewMode(mode) {{
      currentViewMode = mode;
      document.getElementById('modeGridBtn').classList.toggle('active', mode === 'grid');
      document.getElementById('modeListBtn').classList.toggle('active', mode === 'list');
      desktopNumbersGrid.style.display = mode === 'grid' ? 'grid' : 'none';
      desktopTopicsList.style.display = mode === 'list' ? 'flex' : 'none';
    }}

    function setMobileViewMode(mode) {{
      mobileViewMode = mode;
      document.getElementById('mobileModeGridBtn').classList.toggle('active', mode === 'grid');
      document.getElementById('mobileModeListBtn').classList.toggle('active', mode === 'list');
      mobileNumbersGrid.style.display = mode === 'grid' ? 'grid' : 'none';
      mobileTopicsList.style.display = mode === 'list' ? 'flex' : 'none';
    }}

    function goToTopicIndex(index) {{
      if (index >= 0 && index < QUIZ_DATA.length) {{
        currentIndex = index;
        renderCurrentTopic();
        closeAllModals();
      }}
    }}

    function nextTopic() {{
      if (currentIndex < QUIZ_DATA.length - 1) {{
        goToTopicIndex(currentIndex + 1);
      }}
    }}

    function prevTopic() {{
      if (currentIndex > 0) {{
        goToTopicIndex(currentIndex - 1);
      }}
    }}

    function selectRandomTopic() {{
      const randIdx = Math.floor(Math.random() * QUIZ_DATA.length);
      goToTopicIndex(randIdx);
    }}

    function handleSearch(val) {{
      searchQuery = val;
      renderAllSelectors();
      updateActiveSelectorUI();
    }}

    function toggleMobileModal(show) {{
      if (show) {{
        closeAllModals();
        mobileModalOverlay.classList.add('open');
        mobileModal.classList.add('open');
        document.body.style.overflow = 'hidden';
        const input = document.getElementById('mobileSearchInput');
        if (input) {{
          input.value = '';
          searchQuery = '';
          renderAllSelectors();
          updateActiveSelectorUI();
        }}
      }} else {{
        mobileModalOverlay.classList.remove('open');
        mobileModal.classList.remove('open');
        document.body.style.overflow = '';
      }}
    }}

    function toggleNoBallModal(show) {{
      if (show) {{
        closeAllModals();
        mobileModalOverlay.classList.add('open');
        noBallModal.classList.add('open');
        document.body.style.overflow = 'hidden';
      }} else {{
        mobileModalOverlay.classList.remove('open');
        noBallModal.classList.remove('open');
        document.body.style.overflow = '';
      }}
    }}

    function closeAllModals() {{
      mobileModalOverlay.classList.remove('open');
      mobileModal.classList.remove('open');
      noBallModal.classList.remove('open');
      document.body.style.overflow = '';
    }}

    function toggleTheme() {{
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('jain_quiz_theme', newTheme);
      updateThemeIcon(newTheme);
    }}

    function updateThemeIcon(theme) {{
      if (themeToggleBtn) {{
        themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
        themeToggleBtn.title = theme === 'dark' ? 'लाइट थीम चालू करें' : 'डार्क थीम चालू करें';
      }}
    }}

    function setupKeyboardNavigation() {{
      window.addEventListener('keydown', (e) => {{
        if (e.target.tagName === 'INPUT') return;
        if (e.key === 'ArrowRight' || e.key === 'PageDown') {{
          nextTopic();
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
          prevTopic();
        }} else if (e.key === 'Escape') {{
          closeAllModals();
        }}
      }});
    }}

    function escapeHtml(str) {{
      if (!str) return '';
      return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    window.addEventListener('DOMContentLoaded', initApp);
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Regenerated index.html with No-Ball modal and quiz data.")
