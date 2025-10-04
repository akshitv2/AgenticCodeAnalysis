from crewai.tools import BaseTool
from crewai_tools.tools.directory_read_tool.directory_read_tool import DirectoryReadTool
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
from crewai_tools.tools.file_writer_tool.file_writer_tool import FileWriterTool
from crewai_tools.tools.scrape_website_tool.scrape_website_tool import ScrapeWebsiteTool
from crewai_tools.tools.serper_dev_tool.serper_dev_tool import SerperDevTool


def get_directory_read_tool(project_directory) -> BaseTool:
    return DirectoryReadTool(directory=project_directory)


def get_search_tool():
    return SerperDevTool()


def get_fetch_webpage_tool():
    return ScrapeWebsiteTool()


def get_file_read_tool():
    return FileReadTool()


def get_file_write_tool(directory, filename):
    return FileWriterTool(directory = directory, filename="")
