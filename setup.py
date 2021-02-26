from setuptools import setup, find_packages

setup(
    name = 'moocxing',
    version = '0.0.7',
    keywords='moocxing',
    description = 'anzhi',
    license = 'MIT License',
    description = '用于MOOCXING教育学习使用', 
    url = 'https://github.com/Aanzhi/moocxing',
    author = 'anzhi',
    author_email = '1532741445@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'requests>=2.24.0',
        'pyserial>=3.4',
        'mcpi>=1.2.0',
        'minecraftstuff>=1.0.1',
        'baidu-aip>=2.2.18.0',
        'bs4>=0.0.1',
        'ffmpeg-python>=0.2.0',
        'paho-mqtt>=1.5.0',
        'xpinyin>=0.5.6',
        'pyecharts>=1.9.0'
        ],
   
)
