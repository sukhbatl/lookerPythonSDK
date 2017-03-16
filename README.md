## Looker API Python SDK

This is a swagger generated python SDK used to access Looker's API

To generate client SDK, follow this tutorial.
NOTE: After the step 4 of the Setup section in this tutorial, rename the swagger.json file into lookerapi.json. Otherwise it will result in an error.
https://discourse.looker.com/t/generating-client-sdks-for-the-looker-api/3185

To download the dashboard in jpg format, try this interactive SDK. Specifically, try create_dashboard_render_task (for body section just put in {"dashboard_style": "tiled"}) and render_task_results to get the rendered dashboard.
https://das42.looker.com:19999/api-docs/index.html#!/RenderTask/create_dashboard_render_task
