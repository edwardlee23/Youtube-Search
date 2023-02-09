from youtubesearchpython.__future__ import VideosSearch


class YoutubeLinks:
    def __init__(self, links):
        self.__links = links

    def __iter__(self):
        for link in self.__links:
            yield link

    def htmlize_links(self):
        links = ''
        for link in self:
            link = f'{link.replace("watch?v=", "embed/")}?enablejsapi=1'
            links += f'<iframe width="800" height="600" src="{link}"></iframe><br/>'
        return links


class YoutubeSearch(VideosSearch):
    def __init__(self, keyword: str):
        super().__init__(keyword, limit=3)

    @staticmethod
    def youtube_links(links) -> YoutubeLinks:
        return YoutubeLinks(links)

    async def __search_videos(self) -> dict:
        return await self.next()

    async def get_youtube_links(self) -> str:
        videos_result = await self.__search_videos()
        links = (result["link"] for result in videos_result["result"])
        return self.youtube_links(links).htmlize_links()
