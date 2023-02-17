def getID(link: str) -> str:
    '''
    ligma balls
    :param link:
    :return:
    '''
    if link.find('v=') != -1:
        return link[link.find('v=') + 2:]
    else:
        return link[link.find('.be/') + 4:]
help(getID)
print(getID('https://www.youtube.com/watch?v=4G5fDpQugwc'))
print(getID('https://youtu.be/4G5fDpQugwc'))
