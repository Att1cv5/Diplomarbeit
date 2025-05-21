import yaml

targets = []
ip_last = 9
for i in range(1, 151):
    ip_last += 1
    targets.append(f'10.0.0.{ip_last}:9100')

prometheus_config = {
    'scrape_configs': [
        {
            'job_name': 'fakehosts',
            'static_configs': [
                {
                    'targets': targets
                }
            ]
        }
    ]
}

with open('prometheus.yml', 'w') as outfile:
    yaml.dump(prometheus_config, outfile, default_flow_style=False)

print("prometheus.yml wurde generiert.")