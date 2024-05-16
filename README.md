"# Star Project" 


# commands to create graph using csv import 

```
bin\neo4j-admin.bat database import full --overwrite-destination --nodes="import\assets_nodes_header.csv","import\assets_nodes.csv" --nodes="import\detection_nodes_header.csv","import\detection_nodes.csv" --nodes="import\qualys_kb_nodes_header.csv","import\qualys_kb_nodes.csv" --nodes="import\cve_db_nodes_header.csv","import\cve_db_nodes.csv" --nodes="import\threat_actor_nodes_header.csv","import\threat_actor_nodes.csv" --nodes="import\ransomware_nodes_header.csv","import\ransomware_nodes.csv" --nodes="import\malware_nodes_header.csv","import\malware_nodes.csv"  --relationships="import\detection_found_on_assets_rel.csv" --relationships="import\asset_has_risk_detection_rel.csv" --relationships="import\detection_to_qualys_kb_rel.csv" --relationships="import\qualys_kb_to_cve_rel.csv" --relationships="import\threat_to_cve_rel.csv" --relationships="import\cve_to_threat_rel.csv" --relationships="import\ransomware_to_cve_rel.csv" --relationships="import\cve_to_ransomware_rel.csv" --relationships="import\malware_to_cve_rel.csv" --relationships="import\cve_to_malware_rel.csv" --skip-bad-relationships --multiline-fields=true
```
