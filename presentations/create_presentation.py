from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

OUT=Path(__file__).parent
r=Presentation(); r.slide_width=Inches(13.333); r.slide_height=Inches(7.5)
BG='0B1220'; PANEL='142238'; WHITE='F0F5FC'; MUTED='A9BBD2'; BLUE='46B5FF'; GREEN='46DDAC'
def box(s,x,y,w,h,color):
 sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)); sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(color); sh.line.fill.background(); return sh
def text(s,x,y,w,h,t,size=20,color=WHITE,bold=False):
 tf=s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)).text_frame; tf.word_wrap=True
 for i,line in enumerate(t.split('\n')):
  p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text=line; p.font.name='Aptos'; p.font.size=Pt(size); p.font.bold=bold; p.font.color.rgb=RGBColor.from_string(color); p.space_after=Pt(12)
def slide(title,kicker='PROJECT OVERVIEW',note=''):
 s=r.slides.add_slide(r.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=RGBColor.from_string(BG)
 text(s,.55,.28,12,.3,kicker,11,BLUE,True); text(s,.55,.82,12,1.1,title,32,WHITE,True)
 box(s,.55,6.98,12.2,.025,BLUE); text(s,.55,7.1,11,.25,'FRAUD DETECTION  /  Azure workflow: user-described • Application architecture: proposed',9,MUTED); text(s,12,7.07,.7,.3,f'{len(r.slides):02}',11,BLUE)
 s.notes_slide.notes_text_frame.text = note or ('Explain this slide as project context or a proposed design. Azure usage is based on the project owner’s description; no model results or deployment metrics have been verified.')
 return s
def cards(title,items,kicker='PROJECT OVERVIEW',note=''):
 s=slide(title,kicker,note); n=len(items); w=12.2/n
 for i,(h,b) in enumerate(items):
  x=.55+i*w; box(s,x,2.15,w-.18,4.45,PANEL); text(s,x+.22,2.42,w-.6,.8,h,22,BLUE,True); text(s,x+.22,3.35,w-.6,3.05,b,18)
 return s
s=slide('Enterprise Real-Time\nFraud Detection Platform','PROJECT PRESENTATION', 'The title reflects the repository topic. Real-time scoring is a target architecture, not a verified implementation. User reports Azure Databricks preprocessing, storage and a triggered Azure pipeline. No application code is present in the supplied checkout.')
text(s,.6,3.05,10,1.2,'Azure Databricks preprocessing\nCloud storage • Triggered pipelines • Fraud analytics',25,MUTED)
box(s,.6,5.25,11.9,1.05,PANEL); text(s,.85,5.48,11.3,.65,'From transaction data to actionable risk decisions',24,GREEN,True)
cards('Why this platform?', [('Challenge','Fraud patterns evolve quickly.\nManual review cannot scale with transaction volumes.\nLate detection increases exposure.'),('Objective','Prepare trusted transaction data.\nIdentify suspicious behavior.\nSupport timely, explainable decisions.'),('Success criteria','Detect more fraud at a manageable review load.\nReduce unnecessary declines.\nMeasure latency and operating cost.')],note='These are project motivations and proposed success criteria, not measured business outcomes.')
cards('Scope and evidence', [('User-described Azure work','Azure Databricks for preprocessing.\nAzure cloud storage.\nA triggered pipeline on Azure.'),('Repository inspected','Initial checkout: project scaffold.\nPresentation generator added.\nNo application implementation supplied.\nAzure resources live outside this checkout.'),('Not yet verified','Dataset and schema.\nModel, API and dashboard code.\nExact storage and trigger services.\nPerformance and deployment results.')], 'IMPLEMENTATION BOUNDARY', 'Source: local checkout at commit 95380f2 and the user’s description. The repository does not establish a working application. Ignore patterns are not implementation evidence.')
s=slide('End-to-end architecture','REFERENCE DESIGN', 'Azure Databricks, storage and triggered pipeline are user-described. Exact Azure storage service and orchestrator are unspecified. All downstream fraud application components are proposed. Scheduled or event-triggered preprocessing does not by itself establish real-time inference.')
for i,(h,b) in enumerate([('01  INGEST','Transaction source\nFormat to confirm'),('02  PREPARE','Azure Databricks\nValidate + transform'),('03  PERSIST','Azure storage\nCurated datasets')]):
 x=.65+i*4.15; box(s,x,2.12,3.8,1.5,PANEL); text(s,x+.2,2.3,3.4,.4,h,18,BLUE,True); text(s,x+.2,2.83,3.4,.7,b,17)
for y in (2.7, 5.2):
 for x in (4.48, 8.63):
  arrow = s.shapes.add_shape(MSO_SHAPE.CHEVRON, Inches(x), Inches(y), Inches(.28), Inches(.32))
  arrow.fill.solid(); arrow.fill.fore_color.rgb = RGBColor.from_string(GREEN); arrow.line.fill.background()
text(s,.8,3.88,11.8,.5,'Triggered Azure pipeline coordinates data preparation and storage',21,GREEN)
for i,(h,b) in enumerate([('04  SCORE','Features + fraud model'),('05  DECIDE','Risk score + policy'),('06  ACT','Alert + analyst review')]):
 x=.65+i*4.15; box(s,x,4.7,3.8,1.4,PANEL); text(s,x+.2,4.88,3.4,.4,h,18,BLUE,True); text(s,x+.2,5.45,3.4,.4,b,17)
text(s,.8,6.4,11.8,.3,'01–03: Azure workflow context   |   04–06: proposed application layer',13,MUTED)
cards('Preprocessing with Azure Databricks',[('Validate','Check required fields and types.\nHandle missing values.\nRemove duplicate transactions.\nQuarantine invalid records.'),('Transform','Standardize timestamps and currencies.\nEncode categorical attributes.\nBuild time-window aggregates.\nPrevent future-data leakage.'),('Publish','Write curated data to Azure storage.\nRecord schema and run metadata.\nTrack data-quality checks.\nProvide repeatable model inputs.')], 'DATA ENGINEERING', 'Databricks usage is user-described. The individual validation, transformation and publishing steps are recommended, not verified notebook code.')
cards('Storage and triggered orchestration',[('Storage design','Suggested raw, cleaned and feature layers.\nSeparate source data from derived outputs.\nRetain lineage and access boundaries.'),('Pipeline flow','Trigger → read → validate → transform → write.\nRecord execution status.\nRetry transient failures safely.'),('Configuration to confirm','Storage service and file format.\nTrigger type and orchestrator.\nCompute settings and schedule.\nAlerting and recovery policy.')], 'AZURE WORKFLOW', 'Layered storage is a proposed design. The storage and orchestration services are not named by the user; do not assume ADLS, Blob Storage, Azure Data Factory or Databricks Workflows are deployed.')
cards('Fraud signals and feature design',[('Transaction signals','Amount and transaction time.\nMerchant or category.\nPayment channel.\nGeographic context, if available.'),('Behavioral signals','Recent transaction frequency.\nDeviation from typical spend.\nNew device or location.\nRepeated failed attempts.'),('Safe feature handling','Confirm fields exist in the dataset.\nCompute only from past events.\nProtect sensitive identifiers.\nKeep training and serving consistent.')], 'PROPOSED ANALYTICS', 'All example features depend on the actual dataset. No schema or sample data was supplied.')
cards('Model development and evaluation',[('Build a baseline','Start with transparent rules.\nCompare a supervised classifier if labels exist.\nUse anomaly detection if labels are limited.'),('Evaluate correctly','Use a time-based holdout.\nAddress class imbalance.\nTrack precision, recall and PR-AUC.\nInspect false positives and missed fraud.'),('Choose a threshold','Balance fraud loss and review cost.\nCalibrate scores if needed.\nTest across customer segments.\nVersion data, features and models.')], 'PROPOSED MODEL LIFECYCLE', 'No trained model or measured result is present. Candidate methods and metrics are recommendations only. Fit preprocessing on training data, not the complete dataset.')
cards('Real-time scoring and decisions',[('Request path','Receive a transaction.\nValidate the payload.\nRetrieve or compute features.\nReturn a score and reason codes.'),('Decision policy','Low risk: allow.\nIntermediate risk: review or step-up.\nHigh risk: flag or block under policy.\nKeep a decision audit trail.'),('Serving requirements','Define latency and availability SLOs.\nUse consistent feature logic.\nHandle missing features safely.\nKeep batch training separate from serving.')], 'TARGET APPLICATION DESIGN', 'An event-triggered batch pipeline is not equivalent to a low-latency scoring service. This slide describes a proposed future serving path; no API implementation was found.')
cards('Security, reliability and monitoring',[('Protect','Use least-privilege access.\nKeep secrets out of source control.\nEncrypt data in transit and at rest.\nDefine retention and access policies.'),('Operate','Monitor pipeline failures and freshness.\nTrack scoring errors and latency.\nUse idempotent processing.\nPlan rollback and recovery.'),('Improve','Watch feature and score drift.\nCollect analyst feedback.\nMeasure outcomes when labels arrive.\nReview fairness and model degradation.')], 'RECOMMENDED CONTROLS', 'These controls are recommendations; the checkout does not verify Azure identities, secret stores, monitoring or deployment configurations.')
cards('Demonstration and validation plan',[('Azure evidence','Show a pipeline trigger and successful run.\nOpen the Databricks notebook.\nCompare raw and curated records.\nShow the storage output.'),('Application evidence','When implemented: score a sample transaction.\nDisplay a risk reason and decision.\nShow a review or alert record.\nDemonstrate failure handling.'),('Results to capture','Data-quality pass rate.\nPipeline runtime and throughput.\nPrecision, recall and PR-AUC.\nScoring latency percentiles.')], 'PROJECT DEMONSTRATION', 'A proposed demonstration checklist, not a claim that the demonstrations have been executed. Populate results only from real runs; no accuracy or latency numbers are currently available.')
cards('Roadmap to a reproducible platform',[('01  Document','Add architecture and setup steps.\nRecord exact Azure services.\nDefine schema and label source.\nExport notebooks without secrets.'),('02  Implement','Add preprocessing and tests.\nBuild and evaluate a baseline.\nAdd scoring and decision logic.\nPin runtime dependencies.'),('03  Validate','Run end-to-end integration tests.\nCapture reproducible metrics.\nTest access and failure scenarios.\nAutomate deployment and monitoring.')], 'NEXT STEPS', 'The repository is currently a scaffold. The roadmap is suggested work and does not imply the Azure work described by the user is absent outside this checkout.')
s=slide('A cloud data foundation.\nA clear path to fraud intelligence.','SUMMARY & DISCUSSION')
text(s,.65,3.05,11.9,2.4,'Azure Databricks prepares transaction data.\nAzure storage and triggered pipelines support repeatable processing.\nThe next layer connects trusted features to risk decisions.',25,MUTED)
text(s,.65,5.8,11.8,.7,'Discussion: dataset • Azure configuration • model choice • live demo',20,GREEN,True)
assert len(r.slides) == 13, 'The presentation must contain exactly 13 slides'
r.core_properties.title = 'Enterprise Real-Time Fraud Detection Platform'
r.core_properties.subject = 'Azure Databricks, cloud storage and triggered pipelines'
r.core_properties.keywords = 'Azure, Databricks, fraud detection, reference architecture'
r.save(OUT/'Enterprise_Fraud_Detection_Platform.pptx')
print(f'Saved {len(r.slides)} slides')
