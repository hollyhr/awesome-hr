# Maintenance

Awesome HR is an actively curated public resource, not an exhaustive vendor
directory.

## Accountability

- Accountable maintainer: Paul Gould (`@paulgould`).
- GitHub ownership: `.github/CODEOWNERS` routes every change to the accountable
  maintainer.
- Community pull requests are welcome. The maintainer owns inclusion decisions,
  factual corrections and removal of stale resources.

If no human catalogue change or documented review is made for 90 days, the
maintainer must either name a replacement owner, publish a recovery issue with a
date, or archive the repository. Dependabot and scheduled link-check commits do
not count as human maintenance.

## Cadence

- Weekly: automated link and catalogue-policy checks.
- Monthly: human review of failures, open contributions and time-sensitive UK
  employment links, including the exact automated-check exceptions in
  `lychee.toml`; record completion in a dated GitHub issue or merged pull request.
- Quarterly: review category coverage, project activity, licences and whether
  commercial entries still provide independent value.
- Annually: reconsider the scope, licence, accountable owner and whether the
  list is earning external use or contributions.

## Quality bar

One authoritative, maintained resource is worth more than several generic
articles or vendor links, so the list grows only when a resource earns its
place. The earlier targets of 75 and 100 resources were dropped in November
2026, when the list was cut to stay focused on HR. The automated floor in
`scripts/check_catalogue.py` prevents accidental shrinkage; raise it only after
the corresponding resources are merged.

## Measures

The monthly review records:

- resource count and category coverage;
- broken, redirected, replaced and removed links;
- community pull requests opened, accepted and declined;
- repository traffic, stars and referring sites when GitHub exposes them;
- the date and owner of the next review.

There is no paid placement. HollyHR, the maintainer's company, does not list its
own products.
