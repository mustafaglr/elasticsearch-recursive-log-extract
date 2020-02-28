curl -X GET -tlsv1.2 --insecure -H "Authorization: Bearer $1" "https://ELASTICSEARCH_URL/PROJECTINDEX/_search?scroll=10m&pretty" -d 'QUERY' -kv > log.json
