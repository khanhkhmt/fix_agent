#!/usr/bin/env sh
set -eu

if [ ! -r /proc/meminfo ]; then
  echo "This helper is intended for Linux hosts with /proc/meminfo." >&2
  exit 1
fi

cpu_total="$(nproc)"
mem_total_mb="$(awk '/MemTotal/ { printf "%d", $2 / 1024 }' /proc/meminfo)"

round_tenth() {
  awk -v value="$1" 'BEGIN { printf "%.1f", value }'
}

to_mb() {
  awk -v total="$1" -v ratio="$2" 'BEGIN {
    value = int(total * ratio)
    if (value < 128) value = 128
    printf "%dm", value
  }'
}

server_cpu="$(round_tenth "$(awk -v total="$cpu_total" 'BEGIN { value = total * 0.5; if (value < 1.0) value = 1.0; print value }')")"
web_cpu="$(round_tenth "$(awk -v total="$cpu_total" 'BEGIN { value = total * 0.2; if (value < 0.5) value = 0.5; print value }')")"
mysql_cpu="$(round_tenth "$(awk -v total="$cpu_total" 'BEGIN { value = total * 0.2; if (value < 0.5) value = 0.5; print value }')")"
redis_cpu="$(round_tenth "$(awk -v total="$cpu_total" 'BEGIN { value = total * 0.1; if (value < 0.1) value = 0.1; print value }')")"
edge_cpu="$(round_tenth "$(awk -v total="$cpu_total" 'BEGIN { value = total * 0.1; if (value < 0.2) value = 0.2; print value }')")"

cat <<EOF
# Host capacity detected
# CPU cores: ${cpu_total}
# Memory MB: ${mem_total_mb}

SERVER_CPU_LIMIT=${server_cpu}
SERVER_MEMORY_LIMIT=$(to_mb "$mem_total_mb" 0.45)
WEB_CPU_LIMIT=${web_cpu}
WEB_MEMORY_LIMIT=$(to_mb "$mem_total_mb" 0.18)
MYSQL_CPU_LIMIT=${mysql_cpu}
MYSQL_MEMORY_LIMIT=$(to_mb "$mem_total_mb" 0.22)
REDIS_CPU_LIMIT=${redis_cpu}
REDIS_MEMORY_LIMIT=$(to_mb "$mem_total_mb" 0.08)
EDGE_CPU_LIMIT=${edge_cpu}
EDGE_MEMORY_LIMIT=$(to_mb "$mem_total_mb" 0.05)
EOF
