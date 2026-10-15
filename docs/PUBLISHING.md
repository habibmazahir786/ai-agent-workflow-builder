# GitHub publishing and SEO checklist

## Preparation status on 15 October 2026

- Verified service URL: https://appliconsoft.com/ai-agents/. The README About link now uses this URL; use it for the repository website field too.
- Confirmed GitHub owner: `habibmazahir786`. The user has created https://github.com/habibmazahir786/ai-agent-workflow-builder. README and publishing commands now use this destination.
- Local tests could not run because Python is not installed. Git and GitHub CLI are also unavailable on PATH, and GitHub is not connected. No local commit or push has occurred; remote repository contents and visibility remain unverified.
- The existing GitHub Actions workflow runs unit tests on Python 3.11 without an API key. A successful hosted run remains to be verified after publishing.
- [Tutorial draft](TUTORIAL.md) is prepared for the AppliconSoft website and includes the confirmed repository URL. The article has not been published.
- Website CMS, GA4, and Search Console access are needed for publication and measurement. Community sharing remains pending selection of a relevant community and review of its current posting rules.   
- added comments on git

## Publishing steps

1. Create a GitHub organization or use the existing AppliconSoft organization.
2. Create a **public**, empty repository named `ai-agent-workflow-builder`. Do not auto-add a README/license because they are included here.
3. Extract the ZIP and open a terminal in the `ai-agent-workflow-builder` directory.
4. Run `python -m unittest discover -s tests -v` and `python -m src.main examples/demo.json --input '{"question":"Test"}'`.
5. Confirm the README clone URL uses `habibmazahir786/ai-agent-workflow-builder`.
6. Confirm the correct AI Agent Development service page URL and replace the general homepage link in the About section with it. Do not invent a service URL.
7. Commit and publish:

   ```bash
   git init
   git add .
   git commit -m "Initial release: JSON AI workflow MVP"
   git branch -M main
   git remote add origin https://github.com/habibmazahir786/ai-agent-workflow-builder.git
   git push -u origin main
   ```

8. Set repository description: `Open-source Python AI agent workflow builder with JSON automation, LLM examples, and tests.`
9. Add GitHub topics: `ai-agents`, `ai-agent-development`, `python`, `llm`, `workflow-automation`, `openai-api`.
10. Add the AppliconSoft website in the repository's website field; prefer the verified service URL if appropriate.
11. Confirm the GitHub Actions test workflow succeeds. Do not add API keys to public CI.
12. Write a separate, helpful tutorial on the AppliconSoft website with an original explanation and a link to the repository.
13. Share it with relevant developer communities only where permitted and useful; do not spam or buy links.
14. Track referral sessions and leads in GA4, website search queries in Search Console, and GitHub traffic in Insights.

## Suggested keyword mapping

- **Commercial target:** AI Agent Development (website service page)
- **Informational targets:** AI agent workflow builder, Python AI agent workflow, JSON AI automation example
- **README natural anchor:** `AI agent development services` or `AI development solutions`, only if that accurately describes the target page

Self-created GitHub links do not guarantee ranking improvements. Aim to earn independent references by maintaining a genuinely useful project.
