# beststories
Get the best 500 stories through [Hacker News API](https://github.com/HackerNews/API#new-top-and-best-stories)

```bash
docker build -t beststories:1.0 .

docker run -it beststories:1.0

docker tag beststories:1.0 bh7cw/beststories:1.0
docker push bh7cw/beststories:1.0
```

Jenkins uses full GitHash Value as the tag, and marks the latest tag.