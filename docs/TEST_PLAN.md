# Test Plan — FitnessCourt Automation

This document outlines the testing scenarios and automated scripts covering the admin portal of the FitnessCourt gym management SaaS platform.

## Scope of Automation

We test the owner/admin dashboard, user directory, member profiling, and authentication layers:
1. **Authentication (UI)**: Step-by-step workspace lookup, credentials input, error alerting on wrong passwords/invalid workspace names, and logout redirect verification.
2. **Dashboard Analytics (UI)**: Verification of greeting segments and matching of active metric KPI cards (Active Members, Revenue / Month, Check-ins today, Churn risk).
3. **Members Directory (UI + API)**: Searching members, checking detail cards, status filters (Active vs Inactive), and Generating Telegram one-time link codes.

---

## Scenario Catalog

### 1. Authentication (`TestAuth`)
- **`test_successful_login`**: Navigates to `/login`, inputs slug, owner email, password, and validates landing page dashboard greeting.
- **`test_invalid_credentials_login`**: Submits wrong password and asserts warning text displays.
- **`test_invalid_workspace_slug`**: Submits non-existent slug name on Step 1 and checks error feedback alert.
- **`test_successful_logout`**: Clicks logout inside the nav sidebar and verifies url redirections to the login screen.

### 2. Dashboard (`TestDashboard`)
- **`test_dashboard_greeting_and_cards`**: Checks that the correct dynamic welcome message and all four KPI metric counters are present.
- **`test_sidebar_navigation_flow`**: Validates sidebar transition clicks to `/members` and `/plans`.

### 3. Members Directory (`TestMembers`)
- **`test_search_and_navigate_to_profile`**: Searches for "Aysel Mammadova", waits for the result row to render, clicks, and asserts info cards (phone, email, status).
- **`test_telegram_link_code_generation`**: Navigates to profile, requests one-time code, and validates that it is a 6-digit numeric string.
- **`test_status_filter_tabs`**: Switches filters to "Active" and asserts that all returned rows are flagged active.
