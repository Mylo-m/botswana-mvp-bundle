---
name: botswana-mvp-bundle
description: Complete Botswana Government MVP bundle — ThutoFund (Education Grants), Lekgetho (Tax), Ditshetelo (Legal), Dikgwebo (Business Registry) with shared templates and deployment scripts.
---

# Botswana Government MVP Bundle

## What's Included
1. **ThutoFund** (Port 9000) - Education Grants Management
2. **Lekgetho** (Port 9001) - Tax Filing System
3. **Ditshetelo** (Port 9002) - Legal Aid Platform
4. **Dikgwebo** (Port 9003) - Business Registry

## Shared Components
- Common Flask base templates
- Botswana-specific validation (Omang ID, phone numbers)
- Payment integration (PayPal + bank transfer)
- Admin panels for each MVP
- Deployment scripts (systemd, Nginx)

## Quick Start
```bash
python scripts/init_botswana_bundle.py my-gov-project
cd my-gov-project
pip install -r requirements.txt
python run_all.py
```

## User Context
Ports: 9000-9003. All agents no cron/triggers, manual delegate_task only. ~/project-hub/ has symlinks.

## Selling Points
- Complete gov SaaS suite
- Production-ready
- Follows Botswana requirements