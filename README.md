# WGets

Are you looking for a squential batch URL downloader? WGets could be a viable
solution for you. Based on a given URL pattern, WGets generates the target URLs,
,and later downloads those files automatically for you. WGets is designed to
work sequentially to avoid undesired things such as being banned by the server
which could be caused by firing massive requests in a short period of time.

# Usage

```
./WGets.py "FILENAME_PRIFIX" "http://URL/'<3D>'/'<3D>'.jpg"
```

Since `'<3D>'` stands for 3 digits, WGets conceptually expands the given URL
pattern into a list of URLs which starts from `http://URL/001/001.jpg` to
`http://URL/999/999.jpg`, and later only downloads valid URLs from the list and
saves them under the `downloads` of the project root directory.

NOTE: Currently, `'<3D>'` is the only tag supported.

# Design

Though WGets does try to download all the possible derivatives of the given URL
pattern, WGet doesn't generate the entire URL list, since it could be
an unnecessary waste of time. In fact, we don't even have to try an URL if its
preceeding URL in the same level is invalid.

To make use of the fact, WGet creates a conceptual tree. By inorderly traversing
the tree and early returning in some cases, Wgets can downloads all the valid
derived URLs without bumping into too many invalid ones.

