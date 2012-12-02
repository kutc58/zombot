class GameAction(object):
    pass


class GameApplyCompGiftEvent(GameAction):
    def __init__(self, itemId,  # @ReservedAssignment
                 extraId,  # @ReservedAssignment
                 objId,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x):  # @ReservedAssignment
        assert isinstance(extraId, int)
        assert isinstance(itemId, unicode)
        assert isinstance(objId, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.action = 'applyCompGift'
        self.extraId = extraId
        self.itemId = itemId
        self.objId = objId
        self.type = 'item'
        self.x = x
        self.y = y


class GameApplyGiftEvent(GameAction):
    def __init__(self, gift):  # @ReservedAssignment
        assert isinstance(gift, GameGift)
        self.action = 'applyGift'
        self.gift = gift
        self.type = 'gift'


class GameBuffs(object):
    def __init__(self, list):  # @ReservedAssignment
        assert isinstance(list, list)
        self.list = list


class GameBurySlot(object):
    def __init__(self, enabled):
        assert isinstance(enabled, bool)
        self.enabled = enabled


class GameCollectionItems(object):
    def __init__(self, C_18_2,
                 C_4_3,
                 C_18_1,
                 C_13_3,
                 C_4_4,
                 C_18_3,
                 C_19_3,
                 C_19_2,
                 C_19_1,
                 C_19_5,
                 C_37_2,
                 C_3_1,
                 C_30_5,
                 C_3_3,
                 C_3_2,
                 C_3_5,
                 C_9_4,
                 C_5_2,
                 C_2_1,
                 C_5_1,
                 C_2_3,
                 C_31_1,
                 C_2_5,
                 C_5_5,
                 C_31_2,
                 C_15_5,
                 C_1_4,
                 C_1_3,
                 C_8_3,
                 C_15_1,
                 C_12_5,
                 C_4_1,
                 C_4_5,
                 C_20_1,
                 C_12_1,
                 C_12_3,
                 C_17_1,
                 C_10_2,
                 C_31_3,
                 C_4_2,
                 C_7_2,
                 C_6_4,
                 C_6_5,
                 C_14_4,
                 C_10_5,
                 C_14_2,
                 C_6_1,
                 C_2_2,
                 C_6_3,
                 C_11_3,
                 C_21_3,
                 C_16_2,
                 C_16_4,
                 C_15_3,
                 C_20_3,
                 C_20_2,
                 C_17_3,
                 C_17_5,
                 C_8_4,
                 C_17_4,
                 C_13_4,
                 C_5_4,
                 C_23_2,
                 C_13_2,
                 C_22_5,
                 C_10_3,
                 C_20_4,
                 C_15_2,
                 C_10_4,
                 C_22_2,
                 C_25_4,
                 C_14_5,
                 C_25_2,
                 C_25_1,
                 C_24_5,
                 C_24_4,
                 C_24_2,
                 C_24_1,
                 C_9_2,
                 C_9_1,
                 C_6_2,
                 C_29_3,
                 C_14_1,
                 C_1_2):
        assert isinstance(C_10_2, int)
        assert isinstance(C_10_3, int)
        assert isinstance(C_10_4, int)
        assert isinstance(C_10_5, int)
        assert isinstance(C_11_3, int)
        assert isinstance(C_12_1, int)
        assert isinstance(C_12_3, int)
        assert isinstance(C_12_5, int)
        assert isinstance(C_13_2, int)
        assert isinstance(C_13_3, int)
        assert isinstance(C_13_4, int)
        assert isinstance(C_14_1, int)
        assert isinstance(C_14_2, int)
        assert isinstance(C_14_4, int)
        assert isinstance(C_14_5, int)
        assert isinstance(C_15_1, int)
        assert isinstance(C_15_2, int)
        assert isinstance(C_15_3, int)
        assert isinstance(C_15_5, int)
        assert isinstance(C_16_2, int)
        assert isinstance(C_16_4, int)
        assert isinstance(C_17_1, int)
        assert isinstance(C_17_3, int)
        assert isinstance(C_17_4, int)
        assert isinstance(C_17_5, int)
        assert isinstance(C_18_1, int)
        assert isinstance(C_18_2, int)
        assert isinstance(C_18_3, int)
        assert isinstance(C_19_1, int)
        assert isinstance(C_19_2, int)
        assert isinstance(C_19_3, int)
        assert isinstance(C_19_5, int)
        assert isinstance(C_1_2, int)
        assert isinstance(C_1_3, int)
        assert isinstance(C_1_4, int)
        assert isinstance(C_20_1, int)
        assert isinstance(C_20_2, int)
        assert isinstance(C_20_3, int)
        assert isinstance(C_20_4, int)
        assert isinstance(C_21_3, int)
        assert isinstance(C_22_2, int)
        assert isinstance(C_22_5, int)
        assert isinstance(C_23_2, int)
        assert isinstance(C_24_1, int)
        assert isinstance(C_24_2, int)
        assert isinstance(C_24_4, int)
        assert isinstance(C_24_5, int)
        assert isinstance(C_25_1, int)
        assert isinstance(C_25_2, int)
        assert isinstance(C_25_4, int)
        assert isinstance(C_29_3, int)
        assert isinstance(C_2_1, int)
        assert isinstance(C_2_2, int)
        assert isinstance(C_2_3, int)
        assert isinstance(C_2_5, int)
        assert isinstance(C_30_5, int)
        assert isinstance(C_31_1, int)
        assert isinstance(C_31_2, int)
        assert isinstance(C_31_3, int)
        assert isinstance(C_37_2, int)
        assert isinstance(C_3_1, int)
        assert isinstance(C_3_2, int)
        assert isinstance(C_3_3, int)
        assert isinstance(C_3_5, int)
        assert isinstance(C_4_1, int)
        assert isinstance(C_4_2, int)
        assert isinstance(C_4_3, int)
        assert isinstance(C_4_4, int)
        assert isinstance(C_4_5, int)
        assert isinstance(C_5_1, int)
        assert isinstance(C_5_2, int)
        assert isinstance(C_5_4, int)
        assert isinstance(C_5_5, int)
        assert isinstance(C_6_1, int)
        assert isinstance(C_6_2, int)
        assert isinstance(C_6_3, int)
        assert isinstance(C_6_4, int)
        assert isinstance(C_6_5, int)
        assert isinstance(C_7_2, int)
        assert isinstance(C_8_3, int)
        assert isinstance(C_8_4, int)
        assert isinstance(C_9_1, int)
        assert isinstance(C_9_2, int)
        assert isinstance(C_9_4, int)
        self.C_10_2 = C_10_2
        self.C_10_3 = C_10_3
        self.C_10_4 = C_10_4
        self.C_10_5 = C_10_5
        self.C_11_3 = C_11_3
        self.C_12_1 = C_12_1
        self.C_12_3 = C_12_3
        self.C_12_5 = C_12_5
        self.C_13_2 = C_13_2
        self.C_13_3 = C_13_3
        self.C_13_4 = C_13_4
        self.C_14_1 = C_14_1
        self.C_14_2 = C_14_2
        self.C_14_4 = C_14_4
        self.C_14_5 = C_14_5
        self.C_15_1 = C_15_1
        self.C_15_2 = C_15_2
        self.C_15_3 = C_15_3
        self.C_15_5 = C_15_5
        self.C_16_2 = C_16_2
        self.C_16_4 = C_16_4
        self.C_17_1 = C_17_1
        self.C_17_3 = C_17_3
        self.C_17_4 = C_17_4
        self.C_17_5 = C_17_5
        self.C_18_1 = C_18_1
        self.C_18_2 = C_18_2
        self.C_18_3 = C_18_3
        self.C_19_1 = C_19_1
        self.C_19_2 = C_19_2
        self.C_19_3 = C_19_3
        self.C_19_5 = C_19_5
        self.C_1_2 = C_1_2
        self.C_1_3 = C_1_3
        self.C_1_4 = C_1_4
        self.C_20_1 = C_20_1
        self.C_20_2 = C_20_2
        self.C_20_3 = C_20_3
        self.C_20_4 = C_20_4
        self.C_21_3 = C_21_3
        self.C_22_2 = C_22_2
        self.C_22_5 = C_22_5
        self.C_23_2 = C_23_2
        self.C_24_1 = C_24_1
        self.C_24_2 = C_24_2
        self.C_24_4 = C_24_4
        self.C_24_5 = C_24_5
        self.C_25_1 = C_25_1
        self.C_25_2 = C_25_2
        self.C_25_4 = C_25_4
        self.C_29_3 = C_29_3
        self.C_2_1 = C_2_1
        self.C_2_2 = C_2_2
        self.C_2_3 = C_2_3
        self.C_2_5 = C_2_5
        self.C_30_5 = C_30_5
        self.C_31_1 = C_31_1
        self.C_31_2 = C_31_2
        self.C_31_3 = C_31_3
        self.C_37_2 = C_37_2
        self.C_3_1 = C_3_1
        self.C_3_2 = C_3_2
        self.C_3_3 = C_3_3
        self.C_3_5 = C_3_5
        self.C_4_1 = C_4_1
        self.C_4_2 = C_4_2
        self.C_4_3 = C_4_3
        self.C_4_4 = C_4_4
        self.C_4_5 = C_4_5
        self.C_5_1 = C_5_1
        self.C_5_2 = C_5_2
        self.C_5_4 = C_5_4
        self.C_5_5 = C_5_5
        self.C_6_1 = C_6_1
        self.C_6_2 = C_6_2
        self.C_6_3 = C_6_3
        self.C_6_4 = C_6_4
        self.C_6_5 = C_6_5
        self.C_7_2 = C_7_2
        self.C_8_3 = C_8_3
        self.C_8_4 = C_8_4
        self.C_9_1 = C_9_1
        self.C_9_2 = C_9_2
        self.C_9_4 = C_9_4


class GameDailyBonus(object):
    def __init__(self, dayItemses,
                 current,
                 playFrom,
                 prizes):
        assert isinstance(current, int)
        assert isinstance(dayItemses, list)
        assert isinstance(playFrom, unicode)
        assert isinstance(prizes, list)
        self.current = current
        self.dayItemses = dayItemses
        self.playFrom = playFrom
        self.prizes = prizes


class GameEVTCommand(object):
    def __init__(self, id,  # @ReservedAssignment
                 events):  # @ReservedAssignment
        assert isinstance(events, list)
        assert isinstance(id, unicode)
        self.cmd = 'EVT'
        self.events = events
        self.id = id


class GameGameSettings(object):
    def __init__(self, sound,
                 tutorialState,
                 music):
        assert isinstance(music, bool)
        assert isinstance(sound, bool)
        assert isinstance(tutorialState, int)
        self.music = music
        self.sound = sound
        self.tutorialState = tutorialState


class GameGameStateEvent(GameAction):
    def __init__(self, isAway,  # @ReservedAssignment
                 haveTrickTreating,  # @ReservedAssignment
                 haveTreasure,  # @ReservedAssignment
                 wishlist,  # @ReservedAssignment
                 haveAttempts,  # @ReservedAssignment
                 haveRemoteFertilizeFruit,  # @ReservedAssignment
                 locationInfos,  # @ReservedAssignment
                 locationId,  # @ReservedAssignment
                 location,  # @ReservedAssignment
                 playerSettings,  # @ReservedAssignment
                 playerStatus,  # @ReservedAssignment
                 treasureRehide,  # @ReservedAssignment
                 id,  # @ReservedAssignment
                 haveThanksgivingAttempt):  # @ReservedAssignment
        assert isinstance(haveAttempts, bool)
        assert isinstance(haveRemoteFertilizeFruit, bool)
        assert isinstance(haveThanksgivingAttempt, bool)
        assert isinstance(haveTreasure, bool)
        assert isinstance(haveTrickTreating, bool)
        assert isinstance(id, unicode)
        assert isinstance(isAway, bool)
        assert isinstance(location, GameLocation)
        assert isinstance(locationId, unicode)
        assert isinstance(locationInfos, list)
        assert isinstance(playerSettings, GamePlayerSettings)
        assert isinstance(playerStatus, unicode)
        assert isinstance(treasureRehide, int)
        assert isinstance(wishlist, list)
        self.action = 'gameState'
        self.haveAttempts = haveAttempts
        self.haveRemoteFertilizeFruit = haveRemoteFertilizeFruit
        self.haveThanksgivingAttempt = haveThanksgivingAttempt
        self.haveTreasure = haveTreasure
        self.haveTrickTreating = haveTrickTreating
        self.id = id
        self.isAway = isAway
        self.location = location
        self.locationId = locationId
        self.locationInfos = locationInfos
        self.playerSettings = playerSettings
        self.playerStatus = playerStatus
        self.treasureRehide = treasureRehide
        self.type = 'gameState'
        self.wishlist = wishlist


class GameGetMissionsEvent(GameAction):
    def __init__(self, id,  # @ReservedAssignment
                 missions):  # @ReservedAssignment
        assert isinstance(id, unicode)
        assert isinstance(missions, list)
        self.action = 'getMissions'
        self.id = id
        self.missions = missions
        self.type = 'mission'


class GameGift(object):
    def __init__(self, id):  # @ReservedAssignment
        assert isinstance(id, int)
        self.id = id


class GameGuestInfo(object):
    def __init__(self, visitingTime,
                 userId,
                 playerSettings):
        assert isinstance(playerSettings, GamePlayerSettings)
        assert isinstance(userId, unicode)
        assert isinstance(visitingTime, int)
        self.playerSettings = playerSettings
        self.userId = userId
        self.visitingTime = visitingTime


class GameInfo(object):
    def __init__(self, city,
                 first_name,
                 last_name,
                 uid,
                 country,
                 sex,
                 bdate):
        assert isinstance(bdate, unicode)
        assert isinstance(city, unicode)
        assert isinstance(country, unicode)
        assert isinstance(first_name, unicode)
        assert isinstance(last_name, unicode)
        assert isinstance(sex, int)
        assert isinstance(uid, int)
        self.bdate = bdate
        self.city = city
        self.country = country
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.uid = uid


class GameItem(object):
    pass


class GameLocation(GameItem):
    def __init__(self, width,  # @ReservedAssignment
                 openedAreas,  # @ReservedAssignment
                 height,  # @ReservedAssignment
                 gameObjects,  # @ReservedAssignment
                 guestInfos,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(gameObjects, list)
        assert isinstance(guestInfos, list)
        assert isinstance(height, int)
        assert isinstance(id, unicode)
        assert isinstance(openedAreas, list)
        assert isinstance(width, int)
        self.gameObjects = gameObjects
        self.guestInfos = guestInfos
        self.height = height
        self.id = id
        self.item = '@isle_03'
        self.openedAreas = openedAreas
        self.width = width


class GameLocationInfo(object):
    def __init__(self, openedAreas,
                 occupiedBrainsCount,
                 locationId,
                 maxGameObjectId,
                 giftCoins):
        assert isinstance(giftCoins, int)
        assert isinstance(locationId, unicode)
        assert isinstance(maxGameObjectId, int)
        assert isinstance(occupiedBrainsCount, int)
        assert isinstance(openedAreas, list)
        self.giftCoins = giftCoins
        self.locationId = locationId
        self.maxGameObjectId = maxGameObjectId
        self.occupiedBrainsCount = occupiedBrainsCount
        self.openedAreas = openedAreas


class GameMagic(object):
    def __init__(self, expire,
                 used):
        assert isinstance(expire, unicode)
        assert isinstance(used, int)
        self.expire = expire
        self.used = used


class GameMailBonus(object):
    def __init__(self, bonuses,
                 acceptedBonuses):
        assert isinstance(acceptedBonuses, list)
        assert isinstance(bonuses, list)
        self.acceptedBonuses = acceptedBonuses
        self.bonuses = bonuses


class GameNextPlayTimes(object):
    pass


class GameNpcs(object):
    def __init__(self, npcClientId):
        assert isinstance(npcClientId, int)
        self.npcClientId = npcClientId


class GameParams(object):
    def __init__(self, magicLimit,
                 event):
        assert isinstance(event, GameGameStateEvent)
        assert isinstance(magicLimit, int)
        self.event = event
        self.magicLimit = magicLimit


class GamePlayerSettings(object):
    def __init__(self, userName,
                 dressId,
                 hatId):
        assert isinstance(dressId, unicode)
        assert isinstance(hatId, unicode)
        assert isinstance(userName, unicode)
        self.dressId = dressId
        self.hatId = hatId
        self.userName = userName


class GamePrize(GameItem):
    def __init__(self, count):
        assert isinstance(count, int)
        self.count = count
        self.item = '@CR_07'


class GameSTARTCommand(object):
    def __init__(self, state,  # @ReservedAssignment
                 params,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, unicode)
        assert isinstance(params, GameParams)
        assert isinstance(state, GameState)
        self.cmd = 'START'
        self.id = id
        self.params = params
        self.state = state


class GameState(object):
    def __init__(self, gameSettings,
                 cashMoneyReal,
                 definedBonuses,
                 treasureHide,
                 cashMoney,
                 remoteNewYearExpire,
                 gameMoneyReal,
                 storageItems,
                 buyedClothing,
                 mailBonus,
                 playerSettings,
                 dailyBonus,
                 gameMoney,
                 buffs,
                 remoteTrickTreating,
                 buyedBrains,
                 treasureExpire,
                 treasureCount,
                 burySlots,
                 collectionItems,
                 gifts,
                 freeGiftUsers,
                 remoteTreasure,
                 receivedGiftsExpire,
                 wishlist,
                 remoteNewYear,
                 brainsCount,
                 npcs,
                 magic,
                 storageGameObjects,
                 remoteFertilizeFruitTree,
                 receivedGiftsCoins,
                 level,
                 remoteFertilizeFruitTreeCount,
                 experience,
                 giftId,
                 retentionBonuses,
                 playerStatus,
                 registerDate,
                 remoteThanksgiving,
                 shopOpened):
        assert isinstance(brainsCount, int)
        assert isinstance(buffs, GameBuffs)
        assert isinstance(burySlots, list)
        assert isinstance(buyedBrains, list)
        assert isinstance(buyedClothing, list)
        assert isinstance(cashMoney, int)
        assert isinstance(cashMoneyReal, int)
        assert isinstance(collectionItems, GameCollectionItems)
        assert isinstance(dailyBonus, GameDailyBonus)
        assert isinstance(definedBonuses, list)
        assert isinstance(experience, int)
        assert isinstance(freeGiftUsers, list)
        assert isinstance(gameMoney, int)
        assert isinstance(gameMoneyReal, int)
        assert isinstance(gameSettings, GameGameSettings)
        assert isinstance(giftId, int)
        assert isinstance(gifts, list)
        assert isinstance(level, int)
        assert isinstance(magic, GameMagic)
        assert isinstance(mailBonus, GameMailBonus)
        assert isinstance(npcs, GameNpcs)
        assert isinstance(playerSettings, GamePlayerSettings)
        assert isinstance(playerStatus, unicode)
        assert isinstance(receivedGiftsCoins, int)
        assert isinstance(receivedGiftsExpire, unicode)
        assert isinstance(registerDate, unicode)
        assert isinstance(remoteFertilizeFruitTree, list)
        assert isinstance(remoteFertilizeFruitTreeCount, int)
        assert isinstance(remoteNewYear, list)
        assert isinstance(remoteNewYearExpire, unicode)
        assert isinstance(remoteThanksgiving, list)
        assert isinstance(remoteTreasure, list)
        assert isinstance(remoteTrickTreating, list)
        assert isinstance(retentionBonuses, bool)
        assert isinstance(shopOpened, list)
        assert isinstance(storageGameObjects, list)
        assert isinstance(storageItems, list)
        assert isinstance(treasureCount, int)
        assert isinstance(treasureExpire, unicode)
        assert isinstance(treasureHide, unicode)
        assert isinstance(wishlist, list)
        self.brainsCount = brainsCount
        self.buffs = buffs
        self.burySlots = burySlots
        self.buyedBrains = buyedBrains
        self.buyedClothing = buyedClothing
        self.cashMoney = cashMoney
        self.cashMoneyReal = cashMoneyReal
        self.collectionItems = collectionItems
        self.dailyBonus = dailyBonus
        self.definedBonuses = definedBonuses
        self.experience = experience
        self.freeGiftUsers = freeGiftUsers
        self.gameMoney = gameMoney
        self.gameMoneyReal = gameMoneyReal
        self.gameSettings = gameSettings
        self.giftId = giftId
        self.gifts = gifts
        self.level = level
        self.magic = magic
        self.mailBonus = mailBonus
        self.npcs = npcs
        self.playerSettings = playerSettings
        self.playerStatus = playerStatus
        self.receivedGiftsCoins = receivedGiftsCoins
        self.receivedGiftsExpire = receivedGiftsExpire
        self.registerDate = registerDate
        self.remoteFertilizeFruitTree = remoteFertilizeFruitTree
        self.remoteFertilizeFruitTreeCount = remoteFertilizeFruitTreeCount
        self.remoteNewYear = remoteNewYear
        self.remoteNewYearExpire = remoteNewYearExpire
        self.remoteThanksgiving = remoteThanksgiving
        self.remoteTreasure = remoteTreasure
        self.remoteTrickTreating = remoteTrickTreating
        self.retentionBonuses = retentionBonuses
        self.shopOpened = shopOpened
        self.storageGameObjects = storageGameObjects
        self.storageItems = storageItems
        self.treasureCount = treasureCount
        self.treasureExpire = treasureExpire
        self.treasureHide = treasureHide
        self.wishlist = wishlist


class GameStorageGameObject(GameItem):
    def __init__(self, count):
        assert isinstance(count, int)
        self.count = count
        self.item = '@SC_WOOD_GRAVE2'


class GameStorageItem(GameItem):
    def __init__(self, count):
        assert isinstance(count, int)
        self.count = count
        self.item = '@METAL_SCRAP'


class GameTarget(object):
    def __init__(self, id):  # @ReservedAssignment
        assert isinstance(id, int)
        self.id = id


class GameTasks(object):
    def __init__(self, Q15_11_T2,
                 Q15_11_T3,
                 Q15_11_T1):
        assert isinstance(Q15_11_T1, GameCountedItem)
        assert isinstance(Q15_11_T2, GameCountedItem)
        assert isinstance(Q15_11_T3, GameCountedItem)
        self.Q15_11_T1 = Q15_11_T1
        self.Q15_11_T2 = Q15_11_T2
        self.Q15_11_T3 = Q15_11_T3


class GameType(object):
    pass


class GameUpgradeBuilding(GameType):
    def __init__(self, count,  # @ReservedAssignment
                 finished):  # @ReservedAssignment
        assert isinstance(count, int)
        assert isinstance(finished, bool)
        self.count = count
        self.finished = finished
        self.type = 'upgradeBuilding'


class GameWoodGrave(GameType):
    def __init__(self, target,  # @ReservedAssignment
                 startCounter,  # @ReservedAssignment
                 materials,  # @ReservedAssignment
                 doneCounter,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(doneCounter, int)
        assert isinstance(id, int)
        assert isinstance(materials, list)
        assert isinstance(startCounter, int)
        assert isinstance(target, NoneType)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.doneCounter = doneCounter
        self.id = id
        self.item = '@SC_WOOD_GRAVE'
        self.materials = materials
        self.startCounter = startCounter
        self.target = target
        self.type = 'woodGrave'
        self.x = x
        self.y = y


class GameWoodTree(GameType):
    def __init__(self, materialCount,  # @ReservedAssignment
                 gainStarted,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(gainStarted, bool)
        assert isinstance(id, int)
        assert isinstance(materialCount, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.gainStarted = gainStarted
        self.id = id
        self.item = '@SC_OAK6'
        self.materialCount = materialCount
        self.type = 'woodTree'
        self.x = x
        self.y = y


class GameZombieWork(GameType):
    def __init__(self, count,  # @ReservedAssignment
                 finished):  # @ReservedAssignment
        assert isinstance(count, int)
        assert isinstance(finished, bool)
        self.count = count
        self.finished = finished
        self.type = 'zombieWork'


class GameBase(GameType):
    def __init__(self, y,  # @ReservedAssignment
                 id,  # @ReservedAssignment
                 x):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@D_FENCE1'
        self.type = 'base'
        self.x = x
        self.y = y


class GameBridge(GameType):
    def __init__(self, level,  # @ReservedAssignment
                 nextPlayTimes,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(level, int)
        assert isinstance(nextPlayTimes, GameNextPlayTimes)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@B_BRIDGE'
        self.level = level
        self.nextPlayTimes = nextPlayTimes
        self.type = 'bridge'
        self.x = x
        self.y = y


class GameBuilding(GameType):
    def __init__(self, level,  # @ReservedAssignment
                 nextPlayTimes,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(level, int)
        assert isinstance(nextPlayTimes, GameNextPlayTimes)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@B_FLAG_EMERALD'
        self.level = level
        self.nextPlayTimes = nextPlayTimes
        self.type = 'building'
        self.x = x
        self.y = y


class GameCookGraveWithBrains(GameType):
    def __init__(self, speeduped,  # @ReservedAssignment
                 id,  # @ReservedAssignment
                 materials,  # @ReservedAssignment
                 isUp,  # @ReservedAssignment
                 recipeNo,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 pendingRecipes):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(isUp, bool)
        assert isinstance(materials, list)
        assert isinstance(pendingRecipes, list)
        assert isinstance(recipeNo, int)
        assert isinstance(speeduped, bool)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.isUp = isUp
        self.item = '@SC_COOK_GRAVE_BRAINER'
        self.materials = materials
        self.pendingRecipes = pendingRecipes
        self.recipeNo = recipeNo
        self.speeduped = speeduped
        self.type = 'cookGraveWithBrains'
        self.x = x
        self.y = y


class GameCountedItem(GameType):
    def __init__(self, count,  # @ReservedAssignment
                 finished):  # @ReservedAssignment
        assert isinstance(count, int)
        assert isinstance(finished, bool)
        self.count = count
        self.finished = finished
        self.type = 'countedItem'


class GameDecoration(GameType):
    def __init__(self, placeTime,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(placeTime, unicode)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@D_UMBRELLA2_2'
        self.placeTime = placeTime
        self.type = 'decoration'
        self.x = x
        self.y = y


class GameEVT(GameType):
    def __init__(self, events):  # @ReservedAssignment
        assert isinstance(events, list)
        self.events = events
        self.type = 'EVT'


class GameGameMissionMission(GameType):
    def __init__(self, disabled,  # @ReservedAssignment
                 finished,  # @ReservedAssignment
                 tasks):  # @ReservedAssignment
        assert isinstance(disabled, bool)
        assert isinstance(finished, bool)
        assert isinstance(tasks, GameTasks)
        self.disabled = disabled
        self.finished = finished
        self.item = '@Q15_11'
        self.tasks = tasks
        self.type = 'gameMission'


class GameHalloweenTower(GameType):
    def __init__(self, users,  # @ReservedAssignment
                 level,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(level, int)
        assert isinstance(users, list)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@B_HALLOWEEN'
        self.level = level
        self.type = 'halloweenTower'
        self.users = users
        self.x = x
        self.y = y


class GameMoveGameObjectToLocation(GameType):
    def __init__(self, finished):  # @ReservedAssignment
        assert isinstance(finished, bool)
        self.finished = finished
        self.type = 'moveGameObjectToLocation'


class GameNEW_YEAR(GameType):
    def __init__(self, count,  # @ReservedAssignment
                 free,  # @ReservedAssignment
                 user,  # @ReservedAssignment
                 msg,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(count, int)
        assert isinstance(free, bool)
        assert isinstance(id, int)
        assert isinstance(msg, unicode)
        assert isinstance(user, unicode)
        self.count = count
        self.free = free
        self.id = id
        self.item = '@CR_11'
        self.msg = msg
        self.type = 'NEW_YEAR'
        self.user = user


class GamePickup(GameType):
    def __init__(self, parentId,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(parentId, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@SC_PICKUP_BOX_CAR'
        self.parentId = parentId
        self.type = 'pickup'
        self.x = x
        self.y = y


class GamePier(GameType):
    def __init__(self, level,  # @ReservedAssignment
                 nextPlayTimes,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(level, int)
        assert isinstance(nextPlayTimes, GameNextPlayTimes)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@B_PEAR2'
        self.level = level
        self.nextPlayTimes = nextPlayTimes
        self.type = 'pier'
        self.x = x
        self.y = y


class GamePlant(GameType):
    def __init__(self, fertilized,  # @ReservedAssignment
                 jobFinishTime,  # @ReservedAssignment
                 jobStartTime,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(fertilized, bool)
        assert isinstance(id, int)
        assert isinstance(jobFinishTime, unicode)
        assert isinstance(jobStartTime, unicode)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.fertilized = fertilized
        self.id = id
        self.item = '@P_07'
        self.jobFinishTime = jobFinishTime
        self.jobStartTime = jobStartTime
        self.type = 'plant'
        self.x = x
        self.y = y


class GameSTART(GameType):
    def __init__(self, lang,  # @ReservedAssignment
                 info,  # @ReservedAssignment
                 ad,  # @ReservedAssignment
                 serverTime,  # @ReservedAssignment
                 clientTime):  # @ReservedAssignment
        assert isinstance(ad, unicode)
        assert isinstance(clientTime, int)
        assert isinstance(info, GameInfo)
        assert isinstance(lang, unicode)
        assert isinstance(serverTime, int)
        self.ad = ad
        self.clientTime = clientTime
        self.info = info
        self.lang = lang
        self.serverTime = serverTime
        self.type = 'START'


class GameSlag(GameType):
    def __init__(self, y,  # @ReservedAssignment
                 id,  # @ReservedAssignment
                 x):  # @ReservedAssignment
        assert isinstance(id, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.id = id
        self.item = '@SLAG'
        self.type = 'Slag'
        self.x = x
        self.y = y


class GameSocialMission(GameType):
    def __init__(self, disabled,  # @ReservedAssignment
                 finished,  # @ReservedAssignment
                 limitShow):  # @ReservedAssignment
        assert isinstance(disabled, bool)
        assert isinstance(finished, bool)
        assert isinstance(limitShow, bool)
        self.disabled = disabled
        self.finished = finished
        self.item = '@MI_SOCIAL'
        self.limitShow = limitShow
        self.type = 'social'


class GameStayOnLocation(GameType):
    def __init__(self, finished):  # @ReservedAssignment
        assert isinstance(finished, bool)
        self.finished = finished
        self.type = 'stayOnLocation'


class GameStone(GameType):
    def __init__(self, materialCount,  # @ReservedAssignment
                 gainStarted,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(gainStarted, bool)
        assert isinstance(id, int)
        assert isinstance(materialCount, int)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.gainStarted = gainStarted
        self.id = id
        self.item = '@SC_STONE23'
        self.materialCount = materialCount
        self.type = 'stone'
        self.x = x
        self.y = y


class GameStoneGrave(GameType):
    def __init__(self, target,  # @ReservedAssignment
                 startCounter,  # @ReservedAssignment
                 materials,  # @ReservedAssignment
                 doneCounter,  # @ReservedAssignment
                 y,  # @ReservedAssignment
                 x,  # @ReservedAssignment
                 id):  # @ReservedAssignment
        assert isinstance(doneCounter, int)
        assert isinstance(id, int)
        assert isinstance(materials, list)
        assert isinstance(startCounter, int)
        assert isinstance(target, NoneType)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.doneCounter = doneCounter
        self.id = id
        self.item = '@SC_STONE_GRAVE'
        self.materials = materials
        self.startCounter = startCounter
        self.target = target
        self.type = 'stoneGrave'
        self.x = x
        self.y = y


class GameTIME(GameType):
    def __init__(self, ):  # @ReservedAssignment
        self.type = 'TIME'


if __name__ == '__main__':
    pass
