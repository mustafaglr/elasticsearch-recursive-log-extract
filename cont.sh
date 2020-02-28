rm log.json
# shellcheck disable=SC2016
curl -X GET -tlsv1.2 --insecure -H "Authorization: Bearer $1"  "https://ELASTICSEARCH_URL/_search/scroll?pretty" -d "{ \"scroll\" : \"10m\", \"scroll_id\" :  \"$2\" }" -kv > log.json
