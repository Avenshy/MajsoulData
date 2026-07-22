# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [amulet_struct.proto](#amulet_struct-proto)
    - [ActivityAmuletData](#lq-ActivityAmuletData)
    - [ActivityAmuletEffectRecordData](#lq-ActivityAmuletEffectRecordData)
    - [ActivityAmuletGameRecordData](#lq-ActivityAmuletGameRecordData)
    - [ActivityAmuletHuRecord](#lq-ActivityAmuletHuRecord)
    - [ActivityAmuletHuRecordDirty](#lq-ActivityAmuletHuRecordDirty)
    - [ActivityAmuletIllustratedBookData](#lq-ActivityAmuletIllustratedBookData)
    - [ActivityAmuletMapNodeDataArrayDirty](#lq-ActivityAmuletMapNodeDataArrayDirty)
    - [ActivityAmuletStatisticData](#lq-ActivityAmuletStatisticData)
    - [ActivityAmuletTradeItemArrayDirty](#lq-ActivityAmuletTradeItemArrayDirty)
    - [ActivityAmuletTradeRewardDirty](#lq-ActivityAmuletTradeRewardDirty)
    - [ActivityAmuletUpgradeData](#lq-ActivityAmuletUpgradeData)
    - [AmuletActivityTingInfo](#lq-AmuletActivityTingInfo)
    - [AmuletAdvancedShopGoods](#lq-AmuletAdvancedShopGoods)
    - [AmuletAdvancedShopGoodsArrayDirty](#lq-AmuletAdvancedShopGoodsArrayDirty)
    - [AmuletAdvancedShopUpgrade](#lq-AmuletAdvancedShopUpgrade)
    - [AmuletAdvancedShopUpgradeArrayDirty](#lq-AmuletAdvancedShopUpgradeArrayDirty)
    - [AmuletBadgeData](#lq-AmuletBadgeData)
    - [AmuletBuffData](#lq-AmuletBuffData)
    - [AmuletBuffDataArrayDirty](#lq-AmuletBuffDataArrayDirty)
    - [AmuletCharacterData](#lq-AmuletCharacterData)
    - [AmuletCharacterDataChanges](#lq-AmuletCharacterDataChanges)
    - [AmuletEffectCandidate](#lq-AmuletEffectCandidate)
    - [AmuletEffectCandidatesArrayDirty](#lq-AmuletEffectCandidatesArrayDirty)
    - [AmuletEffectCounterData](#lq-AmuletEffectCounterData)
    - [AmuletEffectCounterDataArrayDirty](#lq-AmuletEffectCounterDataArrayDirty)
    - [AmuletEffectData](#lq-AmuletEffectData)
    - [AmuletEffectDataArrayDirty](#lq-AmuletEffectDataArrayDirty)
    - [AmuletEffectDataChanges](#lq-AmuletEffectDataChanges)
    - [AmuletEffectedHookData](#lq-AmuletEffectedHookData)
    - [AmuletEnemyData](#lq-AmuletEnemyData)
    - [AmuletEnemyDirty](#lq-AmuletEnemyDirty)
    - [AmuletEventData](#lq-AmuletEventData)
    - [AmuletEventHookData](#lq-AmuletEventHookData)
    - [AmuletEventResult](#lq-AmuletEventResult)
    - [AmuletEventResult.AdvancedShopUpgradeResult](#lq-AmuletEventResult-AdvancedShopUpgradeResult)
    - [AmuletEventResult.DealResult](#lq-AmuletEventResult-DealResult)
    - [AmuletEventResult.GambleResult](#lq-AmuletEventResult-GambleResult)
    - [AmuletEventResult.GameEndResult](#lq-AmuletEventResult-GameEndResult)
    - [AmuletEventResult.GangResult](#lq-AmuletEventResult-GangResult)
    - [AmuletEventResult.HuResult](#lq-AmuletEventResult-HuResult)
    - [AmuletEventResult.HuResult.HuInfo](#lq-AmuletEventResult-HuResult-HuInfo)
    - [AmuletEventResult.SelectPackResult](#lq-AmuletEventResult-SelectPackResult)
    - [AmuletEventResult.SellEffectResult](#lq-AmuletEventResult-SellEffectResult)
    - [AmuletEventResult.UpgradeResult](#lq-AmuletEventResult-UpgradeResult)
    - [AmuletFan](#lq-AmuletFan)
    - [AmuletFanValue](#lq-AmuletFanValue)
    - [AmuletFanValueArrayDirty](#lq-AmuletFanValueArrayDirty)
    - [AmuletGameData](#lq-AmuletGameData)
    - [AmuletGameEffectData](#lq-AmuletGameEffectData)
    - [AmuletGameInfoData](#lq-AmuletGameInfoData)
    - [AmuletGameInfoDataChanges](#lq-AmuletGameInfoDataChanges)
    - [AmuletGameOperation](#lq-AmuletGameOperation)
    - [AmuletGameOperation.GangTiles](#lq-AmuletGameOperation-GangTiles)
    - [AmuletGameOperationArrayDirty](#lq-AmuletGameOperationArrayDirty)
    - [AmuletGameRecordData](#lq-AmuletGameRecordData)
    - [AmuletGameRoundData](#lq-AmuletGameRoundData)
    - [AmuletGameShopGoods](#lq-AmuletGameShopGoods)
    - [AmuletHookResult](#lq-AmuletHookResult)
    - [AmuletHookResult.AddBadge](#lq-AmuletHookResult-AddBadge)
    - [AmuletHookResult.AddDoraResult](#lq-AmuletHookResult-AddDoraResult)
    - [AmuletHookResult.AddEffectResult](#lq-AmuletHookResult-AddEffectResult)
    - [AmuletHookResult.AmuletChangeDesktopResult](#lq-AmuletHookResult-AmuletChangeDesktopResult)
    - [AmuletHookResult.BigIntValueResult](#lq-AmuletHookResult-BigIntValueResult)
    - [AmuletHookResult.CopyEffect](#lq-AmuletHookResult-CopyEffect)
    - [AmuletHookResult.ModifyDoraResult](#lq-AmuletHookResult-ModifyDoraResult)
    - [AmuletHookResult.TransformResult](#lq-AmuletHookResult-TransformResult)
    - [AmuletHookResult.UInt32ValueResult](#lq-AmuletHookResult-UInt32ValueResult)
    - [AmuletHookResult.UpgradeEffectResult](#lq-AmuletHookResult-UpgradeEffectResult)
    - [AmuletMapData](#lq-AmuletMapData)
    - [AmuletMapDataChanges](#lq-AmuletMapDataChanges)
    - [AmuletMapNodeData](#lq-AmuletMapNodeData)
    - [AmuletMingInfo](#lq-AmuletMingInfo)
    - [AmuletMingInfoArrayDirty](#lq-AmuletMingInfoArrayDirty)
    - [AmuletNodeEventChanges](#lq-AmuletNodeEventChanges)
    - [AmuletNodeEventData](#lq-AmuletNodeEventData)
    - [AmuletPackQueue](#lq-AmuletPackQueue)
    - [AmuletPackQueueArrayDirty](#lq-AmuletPackQueueArrayDirty)
    - [AmuletRecordDataChanges](#lq-AmuletRecordDataChanges)
    - [AmuletRoundDataChanges](#lq-AmuletRoundDataChanges)
    - [AmuletRuneStoneArrayDirty](#lq-AmuletRuneStoneArrayDirty)
    - [AmuletRuneStoneData](#lq-AmuletRuneStoneData)
    - [AmuletShopData](#lq-AmuletShopData)
    - [AmuletShopDataChanges](#lq-AmuletShopDataChanges)
    - [AmuletShopGoodsArrayDirty](#lq-AmuletShopGoodsArrayDirty)
    - [AmuletShopUpgradeGoods](#lq-AmuletShopUpgradeGoods)
    - [AmuletShopUpgradeGoodsArrayDirty](#lq-AmuletShopUpgradeGoodsArrayDirty)
    - [AmuletShowDesktopTileData](#lq-AmuletShowDesktopTileData)
    - [AmuletShowDesktopTileDataArrayDirty](#lq-AmuletShowDesktopTileDataArrayDirty)
    - [AmuletSkillData](#lq-AmuletSkillData)
    - [AmuletStateData](#lq-AmuletStateData)
    - [AmuletTile](#lq-AmuletTile)
    - [AmuletTileArrayDirty](#lq-AmuletTileArrayDirty)
    - [AmuletTileScore](#lq-AmuletTileScore)
    - [AmuletTileScoreArrayDirty](#lq-AmuletTileScoreArrayDirty)
    - [AmuletTingInfoArrayDirty](#lq-AmuletTingInfoArrayDirty)
    - [AmuletTradeItem](#lq-AmuletTradeItem)
    - [AmuletTradeReward](#lq-AmuletTradeReward)
    - [AmuletValueChanges](#lq-AmuletValueChanges)
    - [CharacterStatistic](#lq-CharacterStatistic)

- [cli_game.proto](#cli_game-proto)
    - [GameRestore](#lq-GameRestore)
    - [NotifyAccountLevelChange](#lq-NotifyAccountLevelChange)
    - [NotifyActivityPoint](#lq-NotifyActivityPoint)
    - [NotifyActivityPoint.ActivityPoint](#lq-NotifyActivityPoint-ActivityPoint)
    - [NotifyActivityReward](#lq-NotifyActivityReward)
    - [NotifyActivityReward.ActivityReward](#lq-NotifyActivityReward-ActivityReward)
    - [NotifyEndGameVote](#lq-NotifyEndGameVote)
    - [NotifyEndGameVote.VoteResult](#lq-NotifyEndGameVote-VoteResult)
    - [NotifyGameBroadcast](#lq-NotifyGameBroadcast)
    - [NotifyGameEndResult](#lq-NotifyGameEndResult)
    - [NotifyGameFinishReward](#lq-NotifyGameFinishReward)
    - [NotifyGameFinishReward.CharacterGift](#lq-NotifyGameFinishReward-CharacterGift)
    - [NotifyGameFinishReward.LevelChange](#lq-NotifyGameFinishReward-LevelChange)
    - [NotifyGameFinishReward.MainCharacter](#lq-NotifyGameFinishReward-MainCharacter)
    - [NotifyGameFinishReward.MatchChest](#lq-NotifyGameFinishReward-MatchChest)
    - [NotifyGamePause](#lq-NotifyGamePause)
    - [NotifyGameTerminate](#lq-NotifyGameTerminate)
    - [NotifyLeaderboardPoint](#lq-NotifyLeaderboardPoint)
    - [NotifyLeaderboardPoint.LeaderboardPoint](#lq-NotifyLeaderboardPoint-LeaderboardPoint)
    - [NotifyNewGame](#lq-NotifyNewGame)
    - [NotifyObserveData](#lq-NotifyObserveData)
    - [NotifyPlayerConnectionState](#lq-NotifyPlayerConnectionState)
    - [NotifyPlayerLoadGameReady](#lq-NotifyPlayerLoadGameReady)
    - [ReqAuthGame](#lq-ReqAuthGame)
    - [ReqAuthObserve](#lq-ReqAuthObserve)
    - [ReqBroadcastInGame](#lq-ReqBroadcastInGame)
    - [ReqChiPengGang](#lq-ReqChiPengGang)
    - [ReqGMCommandInGaming](#lq-ReqGMCommandInGaming)
    - [ReqSelfOperation](#lq-ReqSelfOperation)
    - [ReqSyncGame](#lq-ReqSyncGame)
    - [ReqVoteGameEnd](#lq-ReqVoteGameEnd)
    - [ResAuthGame](#lq-ResAuthGame)
    - [ResEnterGame](#lq-ResEnterGame)
    - [ResGameEndVote](#lq-ResGameEndVote)
    - [ResGamePlayerState](#lq-ResGamePlayerState)
    - [ResStartObserve](#lq-ResStartObserve)
    - [ResSyncGame](#lq-ResSyncGame)

- [cli_lobby.proto](#cli_lobby-proto)
    - [ContestSetting](#lq-ContestSetting)
    - [ContestSetting.LevelLimit](#lq-ContestSetting-LevelLimit)
    - [ReqAccountInfo](#lq-ReqAccountInfo)
    - [ReqAccountList](#lq-ReqAccountList)
    - [ReqAccountStatisticInfo](#lq-ReqAccountStatisticInfo)
    - [ReqAddCollectedGameRecord](#lq-ReqAddCollectedGameRecord)
    - [ReqAddRoomRobot](#lq-ReqAddRoomRobot)
    - [ReqAmuletActivityBuy](#lq-ReqAmuletActivityBuy)
    - [ReqAmuletActivityEffectSort](#lq-ReqAmuletActivityEffectSort)
    - [ReqAmuletActivityEndShopping](#lq-ReqAmuletActivityEndShopping)
    - [ReqAmuletActivityFetchBrief](#lq-ReqAmuletActivityFetchBrief)
    - [ReqAmuletActivityFetchInfo](#lq-ReqAmuletActivityFetchInfo)
    - [ReqAmuletActivityGameOperate](#lq-ReqAmuletActivityGameOperate)
    - [ReqAmuletActivityGiveup](#lq-ReqAmuletActivityGiveup)
    - [ReqAmuletActivityOperate](#lq-ReqAmuletActivityOperate)
    - [ReqAmuletActivityRefreshShop](#lq-ReqAmuletActivityRefreshShop)
    - [ReqAmuletActivitySelectBookEffect](#lq-ReqAmuletActivitySelectBookEffect)
    - [ReqAmuletActivitySelectFreeEffect](#lq-ReqAmuletActivitySelectFreeEffect)
    - [ReqAmuletActivitySelectPack](#lq-ReqAmuletActivitySelectPack)
    - [ReqAmuletActivitySelectRewardPack](#lq-ReqAmuletActivitySelectRewardPack)
    - [ReqAmuletActivitySellEffect](#lq-ReqAmuletActivitySellEffect)
    - [ReqAmuletActivitySetSkillLevel](#lq-ReqAmuletActivitySetSkillLevel)
    - [ReqAmuletActivityStartGame](#lq-ReqAmuletActivityStartGame)
    - [ReqAmuletActivityUpgrade](#lq-ReqAmuletActivityUpgrade)
    - [ReqAmuletActivityUpgradeShopBuff](#lq-ReqAmuletActivityUpgradeShopBuff)
    - [ReqApplyFriend](#lq-ReqApplyFriend)
    - [ReqArenaReward](#lq-ReqArenaReward)
    - [ReqBindAccount](#lq-ReqBindAccount)
    - [ReqBindEmail](#lq-ReqBindEmail)
    - [ReqBindOauth2](#lq-ReqBindOauth2)
    - [ReqBindPhoneNumber](#lq-ReqBindPhoneNumber)
    - [ReqBingoActivityReceiveReward](#lq-ReqBingoActivityReceiveReward)
    - [ReqBingoActivityReceiveReward.BingoReward](#lq-ReqBingoActivityReceiveReward-BingoReward)
    - [ReqBuyArenaTicket](#lq-ReqBuyArenaTicket)
    - [ReqBuyFestivalProposal](#lq-ReqBuyFestivalProposal)
    - [ReqBuyFromChestShop](#lq-ReqBuyFromChestShop)
    - [ReqBuyFromShop](#lq-ReqBuyFromShop)
    - [ReqBuyFromShop.Item](#lq-ReqBuyFromShop-Item)
    - [ReqBuyFromZHP](#lq-ReqBuyFromZHP)
    - [ReqBuyInABMatch](#lq-ReqBuyInABMatch)
    - [ReqBuyShiLian](#lq-ReqBuyShiLian)
    - [ReqCancelGooglePlayOrder](#lq-ReqCancelGooglePlayOrder)
    - [ReqCancelMatchQueue](#lq-ReqCancelMatchQueue)
    - [ReqCancelUnifiedMatch](#lq-ReqCancelUnifiedMatch)
    - [ReqChallangeLeaderboard](#lq-ReqChallangeLeaderboard)
    - [ReqChangeAvatar](#lq-ReqChangeAvatar)
    - [ReqChangeCharacterSkin](#lq-ReqChangeCharacterSkin)
    - [ReqChangeCharacterView](#lq-ReqChangeCharacterView)
    - [ReqChangeCollectedGameRecordRemarks](#lq-ReqChangeCollectedGameRecordRemarks)
    - [ReqChangeCommonView](#lq-ReqChangeCommonView)
    - [ReqChangeMainCharacter](#lq-ReqChangeMainCharacter)
    - [ReqCheckPrivacy](#lq-ReqCheckPrivacy)
    - [ReqCheckPrivacy.Versions](#lq-ReqCheckPrivacy-Versions)
    - [ReqClientMessage](#lq-ReqClientMessage)
    - [ReqCombiningRecycleCraft](#lq-ReqCombiningRecycleCraft)
    - [ReqCommonViews](#lq-ReqCommonViews)
    - [ReqCompleteActivityFlipTaskBatch](#lq-ReqCompleteActivityFlipTaskBatch)
    - [ReqCompleteActivityTask](#lq-ReqCompleteActivityTask)
    - [ReqCompleteActivityTaskBatch](#lq-ReqCompleteActivityTaskBatch)
    - [ReqCompletePeriodActivityTaskBatch](#lq-ReqCompletePeriodActivityTaskBatch)
    - [ReqCompleteSegmentTaskReward](#lq-ReqCompleteSegmentTaskReward)
    - [ReqCompleteVillageTask](#lq-ReqCompleteVillageTask)
    - [ReqComposeShard](#lq-ReqComposeShard)
    - [ReqCreateAlipayAppOrder](#lq-ReqCreateAlipayAppOrder)
    - [ReqCreateAlipayOrder](#lq-ReqCreateAlipayOrder)
    - [ReqCreateAlipayScanOrder](#lq-ReqCreateAlipayScanOrder)
    - [ReqCreateBillingOrder](#lq-ReqCreateBillingOrder)
    - [ReqCreateCustomizedContest](#lq-ReqCreateCustomizedContest)
    - [ReqCreateDMMOrder](#lq-ReqCreateDMMOrder)
    - [ReqCreateENAlipayOrder](#lq-ReqCreateENAlipayOrder)
    - [ReqCreateENJCBOrder](#lq-ReqCreateENJCBOrder)
    - [ReqCreateENMasterCardOrder](#lq-ReqCreateENMasterCardOrder)
    - [ReqCreateENPaypalOrder](#lq-ReqCreateENPaypalOrder)
    - [ReqCreateENVisaOrder](#lq-ReqCreateENVisaOrder)
    - [ReqCreateEmailVerifyCode](#lq-ReqCreateEmailVerifyCode)
    - [ReqCreateGameObserveAuth](#lq-ReqCreateGameObserveAuth)
    - [ReqCreateGamePlan](#lq-ReqCreateGamePlan)
    - [ReqCreateIAPOrder](#lq-ReqCreateIAPOrder)
    - [ReqCreateJPAuOrder](#lq-ReqCreateJPAuOrder)
    - [ReqCreateJPCreditCardOrder](#lq-ReqCreateJPCreditCardOrder)
    - [ReqCreateJPDocomoOrder](#lq-ReqCreateJPDocomoOrder)
    - [ReqCreateJPGMOOrder](#lq-ReqCreateJPGMOOrder)
    - [ReqCreateJPPayPayOrder](#lq-ReqCreateJPPayPayOrder)
    - [ReqCreateJPPaypalOrder](#lq-ReqCreateJPPaypalOrder)
    - [ReqCreateJPSoftbankOrder](#lq-ReqCreateJPSoftbankOrder)
    - [ReqCreateJPWebMoneyOrder](#lq-ReqCreateJPWebMoneyOrder)
    - [ReqCreateKRAlipayOrder](#lq-ReqCreateKRAlipayOrder)
    - [ReqCreateKRJCBOrder](#lq-ReqCreateKRJCBOrder)
    - [ReqCreateKRMasterCardOrder](#lq-ReqCreateKRMasterCardOrder)
    - [ReqCreateKRPaypalOrder](#lq-ReqCreateKRPaypalOrder)
    - [ReqCreateKRVisaOrder](#lq-ReqCreateKRVisaOrder)
    - [ReqCreateMyCardOrder](#lq-ReqCreateMyCardOrder)
    - [ReqCreateNickname](#lq-ReqCreateNickname)
    - [ReqCreatePaypalOrder](#lq-ReqCreatePaypalOrder)
    - [ReqCreatePhoneLoginBind](#lq-ReqCreatePhoneLoginBind)
    - [ReqCreatePhoneVerifyCode](#lq-ReqCreatePhoneVerifyCode)
    - [ReqCreateRoom](#lq-ReqCreateRoom)
    - [ReqCreateSeerReport](#lq-ReqCreateSeerReport)
    - [ReqCreateSteamOrder](#lq-ReqCreateSteamOrder)
    - [ReqCreateWechatAppOrder](#lq-ReqCreateWechatAppOrder)
    - [ReqCreateWechatNativeOrder](#lq-ReqCreateWechatNativeOrder)
    - [ReqCreateXsollaOrder](#lq-ReqCreateXsollaOrder)
    - [ReqCreateYostarOrder](#lq-ReqCreateYostarOrder)
    - [ReqCreateYostarV4SDKOrder](#lq-ReqCreateYostarV4SDKOrder)
    - [ReqCurrentMatchInfo](#lq-ReqCurrentMatchInfo)
    - [ReqDMMPreLogin](#lq-ReqDMMPreLogin)
    - [ReqDeleteComment](#lq-ReqDeleteComment)
    - [ReqDeleteMail](#lq-ReqDeleteMail)
    - [ReqDeliverAA32Order](#lq-ReqDeliverAA32Order)
    - [ReqDigMine](#lq-ReqDigMine)
    - [ReqDoActivitySignIn](#lq-ReqDoActivitySignIn)
    - [ReqEmailLogin](#lq-ReqEmailLogin)
    - [ReqEnterArena](#lq-ReqEnterArena)
    - [ReqEnterCustomizedContest](#lq-ReqEnterCustomizedContest)
    - [ReqExchangeActivityItem](#lq-ReqExchangeActivityItem)
    - [ReqExchangeCurrency](#lq-ReqExchangeCurrency)
    - [ReqFastLogin](#lq-ReqFastLogin)
    - [ReqFeedActivityFeed](#lq-ReqFeedActivityFeed)
    - [ReqFetchAccountGameHuRecords](#lq-ReqFetchAccountGameHuRecords)
    - [ReqFetchAccountInfoExtra](#lq-ReqFetchAccountInfoExtra)
    - [ReqFetchActivityFlipInfo](#lq-ReqFetchActivityFlipInfo)
    - [ReqFetchActivityRank](#lq-ReqFetchActivityRank)
    - [ReqFetchAmuletActivityData](#lq-ReqFetchAmuletActivityData)
    - [ReqFetchAnnouncement](#lq-ReqFetchAnnouncement)
    - [ReqFetchBannerActivityData](#lq-ReqFetchBannerActivityData)
    - [ReqFetchBingoActivityData](#lq-ReqFetchBingoActivityData)
    - [ReqFetchCommentContent](#lq-ReqFetchCommentContent)
    - [ReqFetchCommentList](#lq-ReqFetchCommentList)
    - [ReqFetchContestPlayerRank](#lq-ReqFetchContestPlayerRank)
    - [ReqFetchContestTeamMember](#lq-ReqFetchContestTeamMember)
    - [ReqFetchContestTeamPlayerRank](#lq-ReqFetchContestTeamPlayerRank)
    - [ReqFetchContestTeamRank](#lq-ReqFetchContestTeamRank)
    - [ReqFetchCustomizedContestAuthInfo](#lq-ReqFetchCustomizedContestAuthInfo)
    - [ReqFetchCustomizedContestByContestId](#lq-ReqFetchCustomizedContestByContestId)
    - [ReqFetchCustomizedContestGameLiveList](#lq-ReqFetchCustomizedContestGameLiveList)
    - [ReqFetchCustomizedContestGameRecords](#lq-ReqFetchCustomizedContestGameRecords)
    - [ReqFetchCustomizedContestList](#lq-ReqFetchCustomizedContestList)
    - [ReqFetchCustomizedContestOnlineInfo](#lq-ReqFetchCustomizedContestOnlineInfo)
    - [ReqFetchDailySignActivityData](#lq-ReqFetchDailySignActivityData)
    - [ReqFetchFriendGiftActivityData](#lq-ReqFetchFriendGiftActivityData)
    - [ReqFetchJPCommonCreditCardOrder](#lq-ReqFetchJPCommonCreditCardOrder)
    - [ReqFetchLastPrivacy](#lq-ReqFetchLastPrivacy)
    - [ReqFetchManagerCustomizedContest](#lq-ReqFetchManagerCustomizedContest)
    - [ReqFetchOBToken](#lq-ReqFetchOBToken)
    - [ReqFetchOauth2](#lq-ReqFetchOauth2)
    - [ReqFetchProgressRewardActivityInfo](#lq-ReqFetchProgressRewardActivityInfo)
    - [ReqFetchQuestionnaireDetail](#lq-ReqFetchQuestionnaireDetail)
    - [ReqFetchQuestionnaireList](#lq-ReqFetchQuestionnaireList)
    - [ReqFetchRPGBattleHistory](#lq-ReqFetchRPGBattleHistory)
    - [ReqFetchRankPointLeaderboard](#lq-ReqFetchRankPointLeaderboard)
    - [ReqFetchReadyPlayerList](#lq-ReqFetchReadyPlayerList)
    - [ReqFetchRollingNotice](#lq-ReqFetchRollingNotice)
    - [ReqFetchSeerReport](#lq-ReqFetchSeerReport)
    - [ReqFetchSimulationGameRank](#lq-ReqFetchSimulationGameRank)
    - [ReqFetchSimulationGameRecord](#lq-ReqFetchSimulationGameRecord)
    - [ReqFetchVoteActivity](#lq-ReqFetchVoteActivity)
    - [ReqFetchmanagerCustomizedContestList](#lq-ReqFetchmanagerCustomizedContestList)
    - [ReqFinishCombiningOrder](#lq-ReqFinishCombiningOrder)
    - [ReqFinishedEnding](#lq-ReqFinishedEnding)
    - [ReqForceCompleteChallengeTask](#lq-ReqForceCompleteChallengeTask)
    - [ReqGMCommand](#lq-ReqGMCommand)
    - [ReqGainAccumulatedPointActivityReward](#lq-ReqGainAccumulatedPointActivityReward)
    - [ReqGainMultiPointActivityReward](#lq-ReqGainMultiPointActivityReward)
    - [ReqGainRankPointReward](#lq-ReqGainRankPointReward)
    - [ReqGainVipReward](#lq-ReqGainVipReward)
    - [ReqGameLiveInfo](#lq-ReqGameLiveInfo)
    - [ReqGameLiveLeftSegment](#lq-ReqGameLiveLeftSegment)
    - [ReqGameLiveList](#lq-ReqGameLiveList)
    - [ReqGamePointRank](#lq-ReqGamePointRank)
    - [ReqGameRecord](#lq-ReqGameRecord)
    - [ReqGameRecordList](#lq-ReqGameRecordList)
    - [ReqGameRecordListV2](#lq-ReqGameRecordListV2)
    - [ReqGameRecordsDetail](#lq-ReqGameRecordsDetail)
    - [ReqGameRecordsDetailV2](#lq-ReqGameRecordsDetailV2)
    - [ReqGenerateAnnualReportToken](#lq-ReqGenerateAnnualReportToken)
    - [ReqGenerateCombiningCraft](#lq-ReqGenerateCombiningCraft)
    - [ReqGetFriendVillageData](#lq-ReqGetFriendVillageData)
    - [ReqHandleFriendApply](#lq-ReqHandleFriendApply)
    - [ReqHeatBeat](#lq-ReqHeatBeat)
    - [ReqIslandActivityBuy](#lq-ReqIslandActivityBuy)
    - [ReqIslandActivityBuy.BuyItems](#lq-ReqIslandActivityBuy-BuyItems)
    - [ReqIslandActivityMove](#lq-ReqIslandActivityMove)
    - [ReqIslandActivitySell](#lq-ReqIslandActivitySell)
    - [ReqIslandActivitySell.SellItem](#lq-ReqIslandActivitySell-SellItem)
    - [ReqIslandActivityTidyBag](#lq-ReqIslandActivityTidyBag)
    - [ReqIslandActivityTidyBag.BagData](#lq-ReqIslandActivityTidyBag-BagData)
    - [ReqIslandActivityTidyBag.BagData.ITemData](#lq-ReqIslandActivityTidyBag-BagData-ITemData)
    - [ReqIslandActivityUnlockBagGrid](#lq-ReqIslandActivityUnlockBagGrid)
    - [ReqJoinCustomizedContestChatRoom](#lq-ReqJoinCustomizedContestChatRoom)
    - [ReqJoinMatchQueue](#lq-ReqJoinMatchQueue)
    - [ReqJoinRoom](#lq-ReqJoinRoom)
    - [ReqLeaveComment](#lq-ReqLeaveComment)
    - [ReqLevelLeaderboard](#lq-ReqLevelLeaderboard)
    - [ReqLikeSNS](#lq-ReqLikeSNS)
    - [ReqLogReport](#lq-ReqLogReport)
    - [ReqLogin](#lq-ReqLogin)
    - [ReqLoginBeat](#lq-ReqLoginBeat)
    - [ReqLogout](#lq-ReqLogout)
    - [ReqMMOActivityDebugSetTeamCandidate](#lq-ReqMMOActivityDebugSetTeamCandidate)
    - [ReqMMOActivityEquipFusion](#lq-ReqMMOActivityEquipFusion)
    - [ReqMMOActivityFetchData](#lq-ReqMMOActivityFetchData)
    - [ReqMMOActivityFinishBattle](#lq-ReqMMOActivityFinishBattle)
    - [ReqMMOActivityReceiveSupportReward](#lq-ReqMMOActivityReceiveSupportReward)
    - [ReqMMOActivitySetCharacter](#lq-ReqMMOActivitySetCharacter)
    - [ReqMMOActivitySetEquip](#lq-ReqMMOActivitySetEquip)
    - [ReqMMOActivitySetTeamMember](#lq-ReqMMOActivitySetTeamMember)
    - [ReqMMOActivitySetTeamMember.MMOActivityTeamMember](#lq-ReqMMOActivitySetTeamMember-MMOActivityTeamMember)
    - [ReqMMOActivityStartBattle](#lq-ReqMMOActivityStartBattle)
    - [ReqMMOActivityUpdatehFriendList](#lq-ReqMMOActivityUpdatehFriendList)
    - [ReqMarathonActivityFinishRace](#lq-ReqMarathonActivityFinishRace)
    - [ReqMarathonActivityStartRace](#lq-ReqMarathonActivityStartRace)
    - [ReqModifyBirthday](#lq-ReqModifyBirthday)
    - [ReqModifyNickname](#lq-ReqModifyNickname)
    - [ReqModifyPassword](#lq-ReqModifyPassword)
    - [ReqModifyRoom](#lq-ReqModifyRoom)
    - [ReqModifySignature](#lq-ReqModifySignature)
    - [ReqMoveCombiningCraft](#lq-ReqMoveCombiningCraft)
    - [ReqMultiAccountId](#lq-ReqMultiAccountId)
    - [ReqMutiChallengeLevel](#lq-ReqMutiChallengeLevel)
    - [ReqNextGameRecordList](#lq-ReqNextGameRecordList)
    - [ReqNextRoundVillage](#lq-ReqNextRoundVillage)
    - [ReqOauth2Auth](#lq-ReqOauth2Auth)
    - [ReqOauth2Check](#lq-ReqOauth2Check)
    - [ReqOauth2Login](#lq-ReqOauth2Login)
    - [ReqOauth2Signup](#lq-ReqOauth2Signup)
    - [ReqOpenAllRewardItem](#lq-ReqOpenAllRewardItem)
    - [ReqOpenChest](#lq-ReqOpenChest)
    - [ReqOpenGacha](#lq-ReqOpenGacha)
    - [ReqOpenManualItem](#lq-ReqOpenManualItem)
    - [ReqOpenPreChestItem](#lq-ReqOpenPreChestItem)
    - [ReqOpenRandomRewardItem](#lq-ReqOpenRandomRewardItem)
    - [ReqOpenidCheck](#lq-ReqOpenidCheck)
    - [ReqPayMonthTicket](#lq-ReqPayMonthTicket)
    - [ReqPlatformBillingProducts](#lq-ReqPlatformBillingProducts)
    - [ReqPrepareLogin](#lq-ReqPrepareLogin)
    - [ReqProgressRewardActivityReceive](#lq-ReqProgressRewardActivityReceive)
    - [ReqQuestCrewActivityFeed](#lq-ReqQuestCrewActivityFeed)
    - [ReqQuestCrewActivityHire](#lq-ReqQuestCrewActivityHire)
    - [ReqQuestCrewActivityRefreshMarket](#lq-ReqQuestCrewActivityRefreshMarket)
    - [ReqQuestCrewActivityStartQuest](#lq-ReqQuestCrewActivityStartQuest)
    - [ReqRandomCharacter](#lq-ReqRandomCharacter)
    - [ReqReadAnnouncement](#lq-ReqReadAnnouncement)
    - [ReqReadMail](#lq-ReqReadMail)
    - [ReqReadSNS](#lq-ReqReadSNS)
    - [ReqReceiveAchievementGroupReward](#lq-ReqReceiveAchievementGroupReward)
    - [ReqReceiveAchievementReward](#lq-ReqReceiveAchievementReward)
    - [ReqReceiveActivityFlipTask](#lq-ReqReceiveActivityFlipTask)
    - [ReqReceiveActivityFlipTaskBatch](#lq-ReqReceiveActivityFlipTaskBatch)
    - [ReqReceiveActivityGift](#lq-ReqReceiveActivityGift)
    - [ReqReceiveActivitySpotReward](#lq-ReqReceiveActivitySpotReward)
    - [ReqReceiveAllActivityGift](#lq-ReqReceiveAllActivityGift)
    - [ReqReceiveChallengeRankReward](#lq-ReqReceiveChallengeRankReward)
    - [ReqReceiveCharacterRewards](#lq-ReqReceiveCharacterRewards)
    - [ReqReceiveRPGReward](#lq-ReqReceiveRPGReward)
    - [ReqReceiveRPGRewards](#lq-ReqReceiveRPGRewards)
    - [ReqReceiveUpgradeActivityReward](#lq-ReqReceiveUpgradeActivityReward)
    - [ReqReceiveVillageBuildingReward](#lq-ReqReceiveVillageBuildingReward)
    - [ReqReceiveVillageTripReward](#lq-ReqReceiveVillageTripReward)
    - [ReqRecoverCombiningRecycle](#lq-ReqRecoverCombiningRecycle)
    - [ReqRefreshDailyTask](#lq-ReqRefreshDailyTask)
    - [ReqRefreshGameObserveAuth](#lq-ReqRefreshGameObserveAuth)
    - [ReqRemarkFriend](#lq-ReqRemarkFriend)
    - [ReqRemoveCollectedGameRecord](#lq-ReqRemoveCollectedGameRecord)
    - [ReqRemoveFriend](#lq-ReqRemoveFriend)
    - [ReqReplySNS](#lq-ReqReplySNS)
    - [ReqReshZHPShop](#lq-ReqReshZHPShop)
    - [ReqResolveFestivalActivityEvent](#lq-ReqResolveFestivalActivityEvent)
    - [ReqResolveFestivalActivityProposal](#lq-ReqResolveFestivalActivityProposal)
    - [ReqRichmanChestInfo](#lq-ReqRichmanChestInfo)
    - [ReqRichmanNextMove](#lq-ReqRichmanNextMove)
    - [ReqRichmanSpecialMove](#lq-ReqRichmanSpecialMove)
    - [ReqRoomDressing](#lq-ReqRoomDressing)
    - [ReqRoomKickPlayer](#lq-ReqRoomKickPlayer)
    - [ReqRoomReady](#lq-ReqRoomReady)
    - [ReqRoomStart](#lq-ReqRoomStart)
    - [ReqSaveCommonViews](#lq-ReqSaveCommonViews)
    - [ReqSayChatMessage](#lq-ReqSayChatMessage)
    - [ReqSearchAccountByEidLobby](#lq-ReqSearchAccountByEidLobby)
    - [ReqSearchAccountById](#lq-ReqSearchAccountById)
    - [ReqSearchAccountByPattern](#lq-ReqSearchAccountByPattern)
    - [ReqSelectChestChooseGroupActivity](#lq-ReqSelectChestChooseGroupActivity)
    - [ReqSelectChestChooseUp](#lq-ReqSelectChestChooseUp)
    - [ReqSellItem](#lq-ReqSellItem)
    - [ReqSellItem.Item](#lq-ReqSellItem-Item)
    - [ReqSendActivityGiftToFriend](#lq-ReqSendActivityGiftToFriend)
    - [ReqSendClientMessage](#lq-ReqSendClientMessage)
    - [ReqSendGiftToCharacter](#lq-ReqSendGiftToCharacter)
    - [ReqSendGiftToCharacter.Gift](#lq-ReqSendGiftToCharacter-Gift)
    - [ReqSetAccountFavoriteHu](#lq-ReqSetAccountFavoriteHu)
    - [ReqSetActivityBuff](#lq-ReqSetActivityBuff)
    - [ReqSetActivityBuff.BuffInfo](#lq-ReqSetActivityBuff-BuffInfo)
    - [ReqSetFriendRoomRandomBotChar](#lq-ReqSetFriendRoomRandomBotChar)
    - [ReqSetHiddenCharacter](#lq-ReqSetHiddenCharacter)
    - [ReqSetLoadingImage](#lq-ReqSetLoadingImage)
    - [ReqSetVerifiedHidden](#lq-ReqSetVerifiedHidden)
    - [ReqSetVillageWorker](#lq-ReqSetVillageWorker)
    - [ReqShootActivityAttackEnemies](#lq-ReqShootActivityAttackEnemies)
    - [ReqShopPurchase](#lq-ReqShopPurchase)
    - [ReqSignupAccount](#lq-ReqSignupAccount)
    - [ReqSignupCustomizedContest](#lq-ReqSignupCustomizedContest)
    - [ReqSimV2ActivityEndMatch](#lq-ReqSimV2ActivityEndMatch)
    - [ReqSimV2ActivityFetchInfo](#lq-ReqSimV2ActivityFetchInfo)
    - [ReqSimV2ActivityGiveUp](#lq-ReqSimV2ActivityGiveUp)
    - [ReqSimV2ActivitySelectEvent](#lq-ReqSimV2ActivitySelectEvent)
    - [ReqSimV2ActivitySetUpgrade](#lq-ReqSimV2ActivitySetUpgrade)
    - [ReqSimV2ActivityStartMatch](#lq-ReqSimV2ActivityStartMatch)
    - [ReqSimV2ActivityStartSeason](#lq-ReqSimV2ActivityStartSeason)
    - [ReqSimV2ActivityTrain](#lq-ReqSimV2ActivityTrain)
    - [ReqSimulationActivityTrain](#lq-ReqSimulationActivityTrain)
    - [ReqSnowballActivityFinishBattle](#lq-ReqSnowballActivityFinishBattle)
    - [ReqSnowballActivityReceiveReward](#lq-ReqSnowballActivityReceiveReward)
    - [ReqSnowballActivityStartBattle](#lq-ReqSnowballActivityStartBattle)
    - [ReqSnowballActivityUpgrade](#lq-ReqSnowballActivityUpgrade)
    - [ReqSolveGooglePlayOrder](#lq-ReqSolveGooglePlayOrder)
    - [ReqSolveGooglePlayOrderV3](#lq-ReqSolveGooglePlayOrderV3)
    - [ReqStartCustomizedContest](#lq-ReqStartCustomizedContest)
    - [ReqStartSimulationActivityGame](#lq-ReqStartSimulationActivityGame)
    - [ReqStartUnifiedMatch](#lq-ReqStartUnifiedMatch)
    - [ReqStartVillageTrip](#lq-ReqStartVillageTrip)
    - [ReqStopCustomizedContest](#lq-ReqStopCustomizedContest)
    - [ReqStoryActivityReceiveAllFinishReward](#lq-ReqStoryActivityReceiveAllFinishReward)
    - [ReqStoryActivityReceiveEndingReward](#lq-ReqStoryActivityReceiveEndingReward)
    - [ReqStoryActivityReceiveFinishReward](#lq-ReqStoryActivityReceiveFinishReward)
    - [ReqStoryActivityUnlock](#lq-ReqStoryActivityUnlock)
    - [ReqStoryActivityUnlockEnding](#lq-ReqStoryActivityUnlockEnding)
    - [ReqStoryActivityUnlockEndingAndReceive](#lq-ReqStoryActivityUnlockEndingAndReceive)
    - [ReqSubmitQuestionnaire](#lq-ReqSubmitQuestionnaire)
    - [ReqSubmitQuestionnaire.QuestionnaireAnswer](#lq-ReqSubmitQuestionnaire-QuestionnaireAnswer)
    - [ReqSubmitQuestionnaire.QuestionnaireAnswer.QuestionnaireAnswerValue](#lq-ReqSubmitQuestionnaire-QuestionnaireAnswer-QuestionnaireAnswerValue)
    - [ReqTakeAttachment](#lq-ReqTakeAttachment)
    - [ReqTargetCustomizedContest](#lq-ReqTargetCustomizedContest)
    - [ReqTaskRequest](#lq-ReqTaskRequest)
    - [ReqUnbindPhoneNumber](#lq-ReqUnbindPhoneNumber)
    - [ReqUnlockActivitySpot](#lq-ReqUnlockActivitySpot)
    - [ReqUnlockActivitySpotEnding](#lq-ReqUnlockActivitySpotEnding)
    - [ReqUpdateAccountSettings](#lq-ReqUpdateAccountSettings)
    - [ReqUpdateCharacterSort](#lq-ReqUpdateCharacterSort)
    - [ReqUpdateClientValue](#lq-ReqUpdateClientValue)
    - [ReqUpdateCommentSetting](#lq-ReqUpdateCommentSetting)
    - [ReqUpdateIDCardInfo](#lq-ReqUpdateIDCardInfo)
    - [ReqUpdateManagerCustomizedContest](#lq-ReqUpdateManagerCustomizedContest)
    - [ReqUpdateReadComment](#lq-ReqUpdateReadComment)
    - [ReqUpgradeActivityBuff](#lq-ReqUpgradeActivityBuff)
    - [ReqUpgradeActivityLevel](#lq-ReqUpgradeActivityLevel)
    - [ReqUpgradeCharacter](#lq-ReqUpgradeCharacter)
    - [ReqUpgradeVillageBuilding](#lq-ReqUpgradeVillageBuilding)
    - [ReqUseBagItem](#lq-ReqUseBagItem)
    - [ReqUseCommonView](#lq-ReqUseCommonView)
    - [ReqUseGiftCode](#lq-ReqUseGiftCode)
    - [ReqUseTitle](#lq-ReqUseTitle)
    - [ReqUserComplain](#lq-ReqUserComplain)
    - [ReqUserComplain.GameRoundInfo](#lq-ReqUserComplain-GameRoundInfo)
    - [ReqVerificationIAPOrder](#lq-ReqVerificationIAPOrder)
    - [ReqVerifyCodeForSecure](#lq-ReqVerifyCodeForSecure)
    - [ReqVerifyMyCardOrder](#lq-ReqVerifyMyCardOrder)
    - [ReqVerifySteamOrder](#lq-ReqVerifySteamOrder)
    - [ReqVoteActivity](#lq-ReqVoteActivity)
    - [ReqYostarDeleteAccount](#lq-ReqYostarDeleteAccount)
    - [ResAccountActivityData](#lq-ResAccountActivityData)
    - [ResAccountActivityData.ActivityRichmanData](#lq-ResAccountActivityData-ActivityRichmanData)
    - [ResAccountActivityData.ActivitySNSData](#lq-ResAccountActivityData-ActivitySNSData)
    - [ResAccountActivityData.ActivitySignInData](#lq-ResAccountActivityData-ActivitySignInData)
    - [ResAccountActivityData.BuffData](#lq-ResAccountActivityData-BuffData)
    - [ResAccountActivityData.ChestUpData](#lq-ResAccountActivityData-ChestUpData)
    - [ResAccountChallengeRankInfo](#lq-ResAccountChallengeRankInfo)
    - [ResAccountChallengeRankInfo.ChallengeRank](#lq-ResAccountChallengeRankInfo-ChallengeRank)
    - [ResAccountCharacterInfo](#lq-ResAccountCharacterInfo)
    - [ResAccountInfo](#lq-ResAccountInfo)
    - [ResAccountSettings](#lq-ResAccountSettings)
    - [ResAccountStates](#lq-ResAccountStates)
    - [ResAccountStatisticInfo](#lq-ResAccountStatisticInfo)
    - [ResAchievement](#lq-ResAchievement)
    - [ResActivityBuff](#lq-ResActivityBuff)
    - [ResActivityList](#lq-ResActivityList)
    - [ResAddCollectedGameRecord](#lq-ResAddCollectedGameRecord)
    - [ResAllcommonViews](#lq-ResAllcommonViews)
    - [ResAllcommonViews.Views](#lq-ResAllcommonViews-Views)
    - [ResAmuletActivityFetchBrief](#lq-ResAmuletActivityFetchBrief)
    - [ResAmuletActivityFetchInfo](#lq-ResAmuletActivityFetchInfo)
    - [ResAmuletActivityMaintainInfo](#lq-ResAmuletActivityMaintainInfo)
    - [ResAmuletEventResponse](#lq-ResAmuletEventResponse)
    - [ResAnnouncement](#lq-ResAnnouncement)
    - [ResArenaReward](#lq-ResArenaReward)
    - [ResArenaReward.RewardItem](#lq-ResArenaReward-RewardItem)
    - [ResBagInfo](#lq-ResBagInfo)
    - [ResBingoActivityReceiveReward](#lq-ResBingoActivityReceiveReward)
    - [ResBuyFestivalProposal](#lq-ResBuyFestivalProposal)
    - [ResBuyFromChestShop](#lq-ResBuyFromChestShop)
    - [ResBuyFromShop](#lq-ResBuyFromShop)
    - [ResChallengeLeaderboard](#lq-ResChallengeLeaderboard)
    - [ResChallengeLeaderboard.Item](#lq-ResChallengeLeaderboard-Item)
    - [ResChallengeSeasonInfo](#lq-ResChallengeSeasonInfo)
    - [ResChallengeSeasonInfo.ChallengeInfo](#lq-ResChallengeSeasonInfo-ChallengeInfo)
    - [ResChangeCollectedGameRecordRemarks](#lq-ResChangeCollectedGameRecordRemarks)
    - [ResCharacterInfo](#lq-ResCharacterInfo)
    - [ResClientValue](#lq-ResClientValue)
    - [ResClientValue.Value](#lq-ResClientValue-Value)
    - [ResCollectedGameRecordList](#lq-ResCollectedGameRecordList)
    - [ResCombiningRecycleCraft](#lq-ResCombiningRecycleCraft)
    - [ResCommentSetting](#lq-ResCommentSetting)
    - [ResCommonView](#lq-ResCommonView)
    - [ResCommonView.Slot](#lq-ResCommonView-Slot)
    - [ResCommonViews](#lq-ResCommonViews)
    - [ResCompleteActivityFlipTaskBatch](#lq-ResCompleteActivityFlipTaskBatch)
    - [ResCompleteSegmentTaskReward](#lq-ResCompleteSegmentTaskReward)
    - [ResCompleteVillageTask](#lq-ResCompleteVillageTask)
    - [ResConnectionInfo](#lq-ResConnectionInfo)
    - [ResCreateAlipayAppOrder](#lq-ResCreateAlipayAppOrder)
    - [ResCreateAlipayOrder](#lq-ResCreateAlipayOrder)
    - [ResCreateAlipayScanOrder](#lq-ResCreateAlipayScanOrder)
    - [ResCreateBillingOrder](#lq-ResCreateBillingOrder)
    - [ResCreateCustomizedContest](#lq-ResCreateCustomizedContest)
    - [ResCreateDmmOrder](#lq-ResCreateDmmOrder)
    - [ResCreateENAlipayOrder](#lq-ResCreateENAlipayOrder)
    - [ResCreateENJCBOrder](#lq-ResCreateENJCBOrder)
    - [ResCreateENMasterCardOrder](#lq-ResCreateENMasterCardOrder)
    - [ResCreateENPaypalOrder](#lq-ResCreateENPaypalOrder)
    - [ResCreateENVisaOrder](#lq-ResCreateENVisaOrder)
    - [ResCreateGameObserveAuth](#lq-ResCreateGameObserveAuth)
    - [ResCreateIAPOrder](#lq-ResCreateIAPOrder)
    - [ResCreateJPAuOrder](#lq-ResCreateJPAuOrder)
    - [ResCreateJPCreditCardOrder](#lq-ResCreateJPCreditCardOrder)
    - [ResCreateJPDocomoOrder](#lq-ResCreateJPDocomoOrder)
    - [ResCreateJPGMOOrder](#lq-ResCreateJPGMOOrder)
    - [ResCreateJPPayPayOrder](#lq-ResCreateJPPayPayOrder)
    - [ResCreateJPPaypalOrder](#lq-ResCreateJPPaypalOrder)
    - [ResCreateJPSoftbankOrder](#lq-ResCreateJPSoftbankOrder)
    - [ResCreateJPWebMoneyOrder](#lq-ResCreateJPWebMoneyOrder)
    - [ResCreateKRAlipayOrder](#lq-ResCreateKRAlipayOrder)
    - [ResCreateKRJCBOrder](#lq-ResCreateKRJCBOrder)
    - [ResCreateKRMasterCardOrder](#lq-ResCreateKRMasterCardOrder)
    - [ResCreateKRPaypalOrder](#lq-ResCreateKRPaypalOrder)
    - [ResCreateKRVisaOrder](#lq-ResCreateKRVisaOrder)
    - [ResCreateMyCardOrder](#lq-ResCreateMyCardOrder)
    - [ResCreatePaypalOrder](#lq-ResCreatePaypalOrder)
    - [ResCreateRoom](#lq-ResCreateRoom)
    - [ResCreateSeerReport](#lq-ResCreateSeerReport)
    - [ResCreateSteamOrder](#lq-ResCreateSteamOrder)
    - [ResCreateWechatAppOrder](#lq-ResCreateWechatAppOrder)
    - [ResCreateWechatAppOrder.CallWechatAppParam](#lq-ResCreateWechatAppOrder-CallWechatAppParam)
    - [ResCreateWechatNativeOrder](#lq-ResCreateWechatNativeOrder)
    - [ResCreateXsollaOrder](#lq-ResCreateXsollaOrder)
    - [ResCreateYostarOrder](#lq-ResCreateYostarOrder)
    - [ResCreateYostarV4SDKOrder](#lq-ResCreateYostarV4SDKOrder)
    - [ResCurrentMatchInfo](#lq-ResCurrentMatchInfo)
    - [ResCurrentMatchInfo.CurrentMatchInfo](#lq-ResCurrentMatchInfo-CurrentMatchInfo)
    - [ResDMMPreLogin](#lq-ResDMMPreLogin)
    - [ResDailySignInInfo](#lq-ResDailySignInInfo)
    - [ResDailyTask](#lq-ResDailyTask)
    - [ResDeleteAccount](#lq-ResDeleteAccount)
    - [ResDigMine](#lq-ResDigMine)
    - [ResDoActivitySignIn](#lq-ResDoActivitySignIn)
    - [ResDoActivitySignIn.RewardData](#lq-ResDoActivitySignIn-RewardData)
    - [ResEnterCustomizedContest](#lq-ResEnterCustomizedContest)
    - [ResExchangeActivityItem](#lq-ResExchangeActivityItem)
    - [ResFastLogin](#lq-ResFastLogin)
    - [ResFeedActivityFeed](#lq-ResFeedActivityFeed)
    - [ResFeedActivityFeed.RewardItem](#lq-ResFeedActivityFeed-RewardItem)
    - [ResFetchABMatch](#lq-ResFetchABMatch)
    - [ResFetchABMatch.MatchPoint](#lq-ResFetchABMatch-MatchPoint)
    - [ResFetchAccountGameHuRecords](#lq-ResFetchAccountGameHuRecords)
    - [ResFetchAccountGameHuRecords.GameHuRecords](#lq-ResFetchAccountGameHuRecords-GameHuRecords)
    - [ResFetchAccountInfoExtra](#lq-ResFetchAccountInfoExtra)
    - [ResFetchAccountInfoExtra.AccountGameRankDetail](#lq-ResFetchAccountInfoExtra-AccountGameRankDetail)
    - [ResFetchAccountInfoExtra.AccountInfoGameRecord](#lq-ResFetchAccountInfoExtra-AccountInfoGameRecord)
    - [ResFetchAccountInfoExtra.AccountInfoGameRecord.AccountGameResult](#lq-ResFetchAccountInfoExtra-AccountInfoGameRecord-AccountGameResult)
    - [ResFetchAccountInfoExtra.GameHuTypeDetail](#lq-ResFetchAccountInfoExtra-GameHuTypeDetail)
    - [ResFetchAchievementRate](#lq-ResFetchAchievementRate)
    - [ResFetchAchievementRate.AchievementRate](#lq-ResFetchAchievementRate-AchievementRate)
    - [ResFetchActivityFlipInfo](#lq-ResFetchActivityFlipInfo)
    - [ResFetchActivityInterval](#lq-ResFetchActivityInterval)
    - [ResFetchActivityInterval.ActivityInterval](#lq-ResFetchActivityInterval-ActivityInterval)
    - [ResFetchActivityRank](#lq-ResFetchActivityRank)
    - [ResFetchActivityRank.ActivityRankItem](#lq-ResFetchActivityRank-ActivityRankItem)
    - [ResFetchAmuletActivityData](#lq-ResFetchAmuletActivityData)
    - [ResFetchAnnualReportInfo](#lq-ResFetchAnnualReportInfo)
    - [ResFetchBannerActivityData](#lq-ResFetchBannerActivityData)
    - [ResFetchBingoActivityData](#lq-ResFetchBingoActivityData)
    - [ResFetchChallengeInfo](#lq-ResFetchChallengeInfo)
    - [ResFetchCommentContent](#lq-ResFetchCommentContent)
    - [ResFetchCommentList](#lq-ResFetchCommentList)
    - [ResFetchContestPlayerRank](#lq-ResFetchContestPlayerRank)
    - [ResFetchContestPlayerRank.ContestPlayerAccountData](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData)
    - [ResFetchContestPlayerRank.ContestPlayerAccountData.ContestGameResult](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestGameResult)
    - [ResFetchContestPlayerRank.ContestPlayerAccountData.ContestSeriesGameResult](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestSeriesGameResult)
    - [ResFetchContestPlayerRank.PlayerData](#lq-ResFetchContestPlayerRank-PlayerData)
    - [ResFetchContestPlayerRank.SeasonRank](#lq-ResFetchContestPlayerRank-SeasonRank)
    - [ResFetchContestTeamMember](#lq-ResFetchContestTeamMember)
    - [ResFetchContestTeamMember.ContestTeamMemberRank](#lq-ResFetchContestTeamMember-ContestTeamMemberRank)
    - [ResFetchContestTeamRank](#lq-ResFetchContestTeamRank)
    - [ResFetchContestTeamRank.ContestTeamData](#lq-ResFetchContestTeamRank-ContestTeamData)
    - [ResFetchContestTeamRank.SeasonTeamRank](#lq-ResFetchContestTeamRank-SeasonTeamRank)
    - [ResFetchCustomizedContestAuthInfo](#lq-ResFetchCustomizedContestAuthInfo)
    - [ResFetchCustomizedContestByContestId](#lq-ResFetchCustomizedContestByContestId)
    - [ResFetchCustomizedContestGameLiveList](#lq-ResFetchCustomizedContestGameLiveList)
    - [ResFetchCustomizedContestGameRecords](#lq-ResFetchCustomizedContestGameRecords)
    - [ResFetchCustomizedContestList](#lq-ResFetchCustomizedContestList)
    - [ResFetchCustomizedContestOnlineInfo](#lq-ResFetchCustomizedContestOnlineInfo)
    - [ResFetchDailySignActivityData](#lq-ResFetchDailySignActivityData)
    - [ResFetchDailySignActivityData.DailySignActivityData](#lq-ResFetchDailySignActivityData-DailySignActivityData)
    - [ResFetchDailySignActivityData.DailySignActivityDay](#lq-ResFetchDailySignActivityData-DailySignActivityDay)
    - [ResFetchDailySignActivityData.DailySignActivityReward](#lq-ResFetchDailySignActivityData-DailySignActivityReward)
    - [ResFetchFriendGiftActivityData](#lq-ResFetchFriendGiftActivityData)
    - [ResFetchFriendGiftActivityData.FriendData](#lq-ResFetchFriendGiftActivityData-FriendData)
    - [ResFetchFriendGiftActivityData.ItemCountData](#lq-ResFetchFriendGiftActivityData-ItemCountData)
    - [ResFetchGamingInfo](#lq-ResFetchGamingInfo)
    - [ResFetchInfo](#lq-ResFetchInfo)
    - [ResFetchJPCommonCreditCardOrder](#lq-ResFetchJPCommonCreditCardOrder)
    - [ResFetchLastPrivacy](#lq-ResFetchLastPrivacy)
    - [ResFetchLastPrivacy.PrivacyInfo](#lq-ResFetchLastPrivacy-PrivacyInfo)
    - [ResFetchMaintainNotice](#lq-ResFetchMaintainNotice)
    - [ResFetchManagerCustomizedContest](#lq-ResFetchManagerCustomizedContest)
    - [ResFetchManagerCustomizedContest.SeasonInfo](#lq-ResFetchManagerCustomizedContest-SeasonInfo)
    - [ResFetchManagerCustomizedContestList](#lq-ResFetchManagerCustomizedContestList)
    - [ResFetchOBToken](#lq-ResFetchOBToken)
    - [ResFetchOauth2](#lq-ResFetchOauth2)
    - [ResFetchPhoneLoginBind](#lq-ResFetchPhoneLoginBind)
    - [ResFetchProgressRewardActivityInfo](#lq-ResFetchProgressRewardActivityInfo)
    - [ResFetchQuestionnaireDetail](#lq-ResFetchQuestionnaireDetail)
    - [ResFetchQuestionnaireList](#lq-ResFetchQuestionnaireList)
    - [ResFetchQueueInfo](#lq-ResFetchQueueInfo)
    - [ResFetchRPGBattleHistory](#lq-ResFetchRPGBattleHistory)
    - [ResFetchRPGBattleHistory.BattleResult](#lq-ResFetchRPGBattleHistory-BattleResult)
    - [ResFetchRPGBattleHistoryV2](#lq-ResFetchRPGBattleHistoryV2)
    - [ResFetchRPGBattleHistoryV2.BattleResultV2](#lq-ResFetchRPGBattleHistoryV2-BattleResultV2)
    - [ResFetchRankPointLeaderboard](#lq-ResFetchRankPointLeaderboard)
    - [ResFetchRankPointLeaderboard.Item](#lq-ResFetchRankPointLeaderboard-Item)
    - [ResFetchReadyPlayerList](#lq-ResFetchReadyPlayerList)
    - [ResFetchReadyPlayerList.Player](#lq-ResFetchReadyPlayerList-Player)
    - [ResFetchRefundOrder](#lq-ResFetchRefundOrder)
    - [ResFetchRefundOrder.OrderInfo](#lq-ResFetchRefundOrder-OrderInfo)
    - [ResFetchRollingNotice](#lq-ResFetchRollingNotice)
    - [ResFetchSeerInfo](#lq-ResFetchSeerInfo)
    - [ResFetchSeerReport](#lq-ResFetchSeerReport)
    - [ResFetchSeerReportList](#lq-ResFetchSeerReportList)
    - [ResFetchSelfGamePointRank](#lq-ResFetchSelfGamePointRank)
    - [ResFetchServerMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo)
    - [ResFetchServerMaintenanceInfo.ServerActivityMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo-ServerActivityMaintenanceInfo)
    - [ResFetchServerMaintenanceInfo.ServerFunctionMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo-ServerFunctionMaintenanceInfo)
    - [ResFetchShopInterval](#lq-ResFetchShopInterval)
    - [ResFetchShopInterval.ShopInterval](#lq-ResFetchShopInterval-ShopInterval)
    - [ResFetchSimulationGameRank](#lq-ResFetchSimulationGameRank)
    - [ResFetchSimulationGameRank.RankInfo](#lq-ResFetchSimulationGameRank-RankInfo)
    - [ResFetchSimulationGameRecord](#lq-ResFetchSimulationGameRecord)
    - [ResFetchVoteActivity](#lq-ResFetchVoteActivity)
    - [ResFetchVoteActivity.VoteRankData](#lq-ResFetchVoteActivity-VoteRankData)
    - [ResFetchrecentFriend](#lq-ResFetchrecentFriend)
    - [ResFinishCombiningOrder](#lq-ResFinishCombiningOrder)
    - [ResFriendApplyList](#lq-ResFriendApplyList)
    - [ResFriendApplyList.FriendApply](#lq-ResFriendApplyList-FriendApply)
    - [ResFriendList](#lq-ResFriendList)
    - [ResGameLiveInfo](#lq-ResGameLiveInfo)
    - [ResGameLiveLeftSegment](#lq-ResGameLiveLeftSegment)
    - [ResGameLiveList](#lq-ResGameLiveList)
    - [ResGamePointRank](#lq-ResGamePointRank)
    - [ResGamePointRank.RankInfo](#lq-ResGamePointRank-RankInfo)
    - [ResGameRecord](#lq-ResGameRecord)
    - [ResGameRecordList](#lq-ResGameRecordList)
    - [ResGameRecordListV2](#lq-ResGameRecordListV2)
    - [ResGameRecordsDetail](#lq-ResGameRecordsDetail)
    - [ResGameRecordsDetailV2](#lq-ResGameRecordsDetailV2)
    - [ResGenerateAnnualReportToken](#lq-ResGenerateAnnualReportToken)
    - [ResGenerateCombiningCraft](#lq-ResGenerateCombiningCraft)
    - [ResGenerateContestManagerLoginCode](#lq-ResGenerateContestManagerLoginCode)
    - [ResGetFriendVillageData](#lq-ResGetFriendVillageData)
    - [ResGetFriendVillageData.FriendVillageData](#lq-ResGetFriendVillageData-FriendVillageData)
    - [ResIDCardInfo](#lq-ResIDCardInfo)
    - [ResJoinCustomizedContestChatRoom](#lq-ResJoinCustomizedContestChatRoom)
    - [ResJoinRoom](#lq-ResJoinRoom)
    - [ResLevelLeaderboard](#lq-ResLevelLeaderboard)
    - [ResLevelLeaderboard.Item](#lq-ResLevelLeaderboard-Item)
    - [ResLikeSNS](#lq-ResLikeSNS)
    - [ResLogin](#lq-ResLogin)
    - [ResLogout](#lq-ResLogout)
    - [ResMMOActivityDebugSetTeamCandidate](#lq-ResMMOActivityDebugSetTeamCandidate)
    - [ResMMOActivityEquipFusion](#lq-ResMMOActivityEquipFusion)
    - [ResMMOActivityFetchData](#lq-ResMMOActivityFetchData)
    - [ResMMOActivityFinishBattle](#lq-ResMMOActivityFinishBattle)
    - [ResMMOActivityReceiveSupportReward](#lq-ResMMOActivityReceiveSupportReward)
    - [ResMMOActivitySetCharacter](#lq-ResMMOActivitySetCharacter)
    - [ResMMOActivitySetEquip](#lq-ResMMOActivitySetEquip)
    - [ResMMOActivitySetTeamMember](#lq-ResMMOActivitySetTeamMember)
    - [ResMMOActivityStartBattle](#lq-ResMMOActivityStartBattle)
    - [ResMMOActivityStartBattle.MMOActivityBattleAction](#lq-ResMMOActivityStartBattle-MMOActivityBattleAction)
    - [ResMMOActivityStartBattle.MMOActivityBattleUnit](#lq-ResMMOActivityStartBattle-MMOActivityBattleUnit)
    - [ResMMOActivityUpdatehFriendList](#lq-ResMMOActivityUpdatehFriendList)
    - [ResMailInfo](#lq-ResMailInfo)
    - [ResMarathonActivityFinishRace](#lq-ResMarathonActivityFinishRace)
    - [ResMarathonActivityStartRace](#lq-ResMarathonActivityStartRace)
    - [ResMisc](#lq-ResMisc)
    - [ResMisc.MiscFaithData](#lq-ResMisc-MiscFaithData)
    - [ResModNicknameTime](#lq-ResModNicknameTime)
    - [ResMonthTicketInfo](#lq-ResMonthTicketInfo)
    - [ResMoveCombiningCraft](#lq-ResMoveCombiningCraft)
    - [ResMoveCombiningCraft.BonusData](#lq-ResMoveCombiningCraft-BonusData)
    - [ResMultiAccountBrief](#lq-ResMultiAccountBrief)
    - [ResMutiChallengeLevel](#lq-ResMutiChallengeLevel)
    - [ResMutiChallengeLevel.Item](#lq-ResMutiChallengeLevel-Item)
    - [ResNextGameRecordList](#lq-ResNextGameRecordList)
    - [ResNextRoundVillage](#lq-ResNextRoundVillage)
    - [ResOauth2Auth](#lq-ResOauth2Auth)
    - [ResOauth2Check](#lq-ResOauth2Check)
    - [ResOauth2Signup](#lq-ResOauth2Signup)
    - [ResOpenAllRewardItem](#lq-ResOpenAllRewardItem)
    - [ResOpenChest](#lq-ResOpenChest)
    - [ResOpenChest.ChestReplaceCountData](#lq-ResOpenChest-ChestReplaceCountData)
    - [ResOpenGacha](#lq-ResOpenGacha)
    - [ResOpenPreChestItem](#lq-ResOpenPreChestItem)
    - [ResOpenRandomRewardItem](#lq-ResOpenRandomRewardItem)
    - [ResPayMonthTicket](#lq-ResPayMonthTicket)
    - [ResPlatformBillingProducts](#lq-ResPlatformBillingProducts)
    - [ResProgressRewardActivityReceive](#lq-ResProgressRewardActivityReceive)
    - [ResQuestCrewActivityFeed](#lq-ResQuestCrewActivityFeed)
    - [ResQuestCrewActivityHire](#lq-ResQuestCrewActivityHire)
    - [ResQuestCrewActivityRefreshMarket](#lq-ResQuestCrewActivityRefreshMarket)
    - [ResQuestCrewActivityStartQuest](#lq-ResQuestCrewActivityStartQuest)
    - [ResQuestCrewActivityStartQuest.ActivityQuestCrewEffectInfo](#lq-ResQuestCrewActivityStartQuest-ActivityQuestCrewEffectInfo)
    - [ResRandomCharacter](#lq-ResRandomCharacter)
    - [ResReadSNS](#lq-ResReadSNS)
    - [ResReceiveAchievementGroupReward](#lq-ResReceiveAchievementGroupReward)
    - [ResReceiveAchievementReward](#lq-ResReceiveAchievementReward)
    - [ResReceiveActivityFlipTask](#lq-ResReceiveActivityFlipTask)
    - [ResReceiveActivityFlipTaskBatch](#lq-ResReceiveActivityFlipTaskBatch)
    - [ResReceiveActivitySpotReward](#lq-ResReceiveActivitySpotReward)
    - [ResReceiveActivitySpotReward.RewardItem](#lq-ResReceiveActivitySpotReward-RewardItem)
    - [ResReceiveAllActivityGift](#lq-ResReceiveAllActivityGift)
    - [ResReceiveAllActivityGift.ReceiveRewards](#lq-ResReceiveAllActivityGift-ReceiveRewards)
    - [ResReceiveChallengeRankReward](#lq-ResReceiveChallengeRankReward)
    - [ResReceiveChallengeRankReward.Reward](#lq-ResReceiveChallengeRankReward-Reward)
    - [ResReceiveCharacterRewards](#lq-ResReceiveCharacterRewards)
    - [ResReceiveCharacterRewards.RewardItem](#lq-ResReceiveCharacterRewards-RewardItem)
    - [ResReceiveRPGRewards](#lq-ResReceiveRPGRewards)
    - [ResReceiveRPGRewards.RewardItem](#lq-ResReceiveRPGRewards-RewardItem)
    - [ResReceiveUpgradeActivityReward](#lq-ResReceiveUpgradeActivityReward)
    - [ResReceiveVillageBuildingReward](#lq-ResReceiveVillageBuildingReward)
    - [ResReceiveVillageTripReward](#lq-ResReceiveVillageTripReward)
    - [ResRecoverCombiningRecycle](#lq-ResRecoverCombiningRecycle)
    - [ResRefreshChallenge](#lq-ResRefreshChallenge)
    - [ResRefreshDailyTask](#lq-ResRefreshDailyTask)
    - [ResRefreshGameObserveAuth](#lq-ResRefreshGameObserveAuth)
    - [ResRefreshZHPShop](#lq-ResRefreshZHPShop)
    - [ResRemoveCollectedGameRecord](#lq-ResRemoveCollectedGameRecord)
    - [ResReplySNS](#lq-ResReplySNS)
    - [ResResolveFestivalActivityEvent](#lq-ResResolveFestivalActivityEvent)
    - [ResResolveFestivalActivityProposal](#lq-ResResolveFestivalActivityProposal)
    - [ResReviveCoinInfo](#lq-ResReviveCoinInfo)
    - [ResRichmanChestInfo](#lq-ResRichmanChestInfo)
    - [ResRichmanChestInfo.ItemData](#lq-ResRichmanChestInfo-ItemData)
    - [ResRichmanNextMove](#lq-ResRichmanNextMove)
    - [ResRichmanNextMove.BuffData](#lq-ResRichmanNextMove-BuffData)
    - [ResRichmanNextMove.PathData](#lq-ResRichmanNextMove-PathData)
    - [ResRichmanNextMove.RewardData](#lq-ResRichmanNextMove-RewardData)
    - [ResSearchAccountById](#lq-ResSearchAccountById)
    - [ResSearchAccountByPattern](#lq-ResSearchAccountByPattern)
    - [ResSearchAccountbyEidLobby](#lq-ResSearchAccountbyEidLobby)
    - [ResSelfRoom](#lq-ResSelfRoom)
    - [ResSendActivityGiftToFriend](#lq-ResSendActivityGiftToFriend)
    - [ResSendGiftToCharacter](#lq-ResSendGiftToCharacter)
    - [ResServerSettings](#lq-ResServerSettings)
    - [ResServerTime](#lq-ResServerTime)
    - [ResSetHiddenCharacter](#lq-ResSetHiddenCharacter)
    - [ResSetVillageWorker](#lq-ResSetVillageWorker)
    - [ResShootActivityAttackEnemies](#lq-ResShootActivityAttackEnemies)
    - [ResShootActivityAttackEnemies.ActivityShootAttackRecord](#lq-ResShootActivityAttackEnemies-ActivityShootAttackRecord)
    - [ResShopInfo](#lq-ResShopInfo)
    - [ResShopPurchase](#lq-ResShopPurchase)
    - [ResSignupAccount](#lq-ResSignupAccount)
    - [ResSignupCustomizedContest](#lq-ResSignupCustomizedContest)
    - [ResSimV2ActivityEndMatch](#lq-ResSimV2ActivityEndMatch)
    - [ResSimV2ActivityEndMatch.SimulationV2MatchReward](#lq-ResSimV2ActivityEndMatch-SimulationV2MatchReward)
    - [ResSimV2ActivityFetchInfo](#lq-ResSimV2ActivityFetchInfo)
    - [ResSimV2ActivitySelectEvent](#lq-ResSimV2ActivitySelectEvent)
    - [ResSimV2ActivityStartMatch](#lq-ResSimV2ActivityStartMatch)
    - [ResSimV2ActivityStartSeason](#lq-ResSimV2ActivityStartSeason)
    - [ResSimV2ActivityTrain](#lq-ResSimV2ActivityTrain)
    - [ResSimulationActivityTrain](#lq-ResSimulationActivityTrain)
    - [ResSnowballActivityFinishBattle](#lq-ResSnowballActivityFinishBattle)
    - [ResSnowballActivityReceiveReward](#lq-ResSnowballActivityReceiveReward)
    - [ResSnowballActivityStartBattle](#lq-ResSnowballActivityStartBattle)
    - [ResSnowballActivityUpgrade](#lq-ResSnowballActivityUpgrade)
    - [ResStartSimulationActivityGame](#lq-ResStartSimulationActivityGame)
    - [ResStoryActivityUnlockEndingAndReceive](#lq-ResStoryActivityUnlockEndingAndReceive)
    - [ResStoryReward](#lq-ResStoryReward)
    - [ResTitleList](#lq-ResTitleList)
    - [ResUpgradeActivityLevel](#lq-ResUpgradeActivityLevel)
    - [ResUpgradeChallenge](#lq-ResUpgradeChallenge)
    - [ResUpgradeCharacter](#lq-ResUpgradeCharacter)
    - [ResUseGiftCode](#lq-ResUseGiftCode)
    - [ResUseSpecialGiftCode](#lq-ResUseSpecialGiftCode)
    - [ResVerfiyCodeForSecure](#lq-ResVerfiyCodeForSecure)
    - [ResVerificationIAPOrder](#lq-ResVerificationIAPOrder)
    - [ResVipReward](#lq-ResVipReward)
    - [ResVoteActivity](#lq-ResVoteActivity)
    - [ResYostarDeleteAccount](#lq-ResYostarDeleteAccount)
    - [SNSBlog](#lq-SNSBlog)
    - [SNSReply](#lq-SNSReply)

- [cli_route.proto](#cli_route-proto)
    - [ReqHeartbeat](#lq-ReqHeartbeat)
    - [ReqRequestConnection](#lq-ReqRequestConnection)
    - [ReqRequestRouteChange](#lq-ReqRequestRouteChange)
    - [ResHeartbeat](#lq-ResHeartbeat)
    - [ResRequestConnection](#lq-ResRequestConnection)
    - [ResRequestRouteChange](#lq-ResRequestRouteChange)

- [client.proto](#client-proto)
- [com_const.proto](#com_const-proto)
    - [EnErrorCode](#lq-EnErrorCode)

- [com_struct.proto](#com_struct-proto)
    - [AccSn](#lq-AccSn)
    - [AccSnDa](#lq-AccSnDa)
    - [Account](#lq-Account)
    - [Account.AchievementCount](#lq-Account-AchievementCount)
    - [Account.Badge](#lq-Account-Badge)
    - [Account.ChallengeLevel](#lq-Account-ChallengeLevel)
    - [Account.PlatformDiamond](#lq-Account-PlatformDiamond)
    - [Account.PlatformSkinTicket](#lq-Account-PlatformSkinTicket)
    - [AccountAchievementSnapshot](#lq-AccountAchievementSnapshot)
    - [AccountAchievementSnapshot.AchievementVersion](#lq-AccountAchievementSnapshot-AchievementVersion)
    - [AccountAchievementSnapshot.RewardedGroupSnapshot](#lq-AccountAchievementSnapshot-RewardedGroupSnapshot)
    - [AccountActiveState](#lq-AccountActiveState)
    - [AccountActivityUpdate](#lq-AccountActivityUpdate)
    - [AccountActivityUpdate.ActivityBuffDataArrayDirty](#lq-AccountActivityUpdate-ActivityBuffDataArrayDirty)
    - [AccountCacheView](#lq-AccountCacheView)
    - [AccountCharacterSnapshot](#lq-AccountCharacterSnapshot)
    - [AccountCharacterSnapshot.HiddenCharacter](#lq-AccountCharacterSnapshot-HiddenCharacter)
    - [AccountCharacterSnapshot.MainCharacterSnapshot](#lq-AccountCharacterSnapshot-MainCharacterSnapshot)
    - [AccountCharacterSnapshot.SkinsSnapshot](#lq-AccountCharacterSnapshot-SkinsSnapshot)
    - [AccountDetailStatistic](#lq-AccountDetailStatistic)
    - [AccountDetailStatisticByCategory](#lq-AccountDetailStatisticByCategory)
    - [AccountDetailStatisticV2](#lq-AccountDetailStatisticV2)
    - [AccountDetailStatisticV2.ChallengeStatistic](#lq-AccountDetailStatisticV2-ChallengeStatistic)
    - [AccountDetailStatisticV2.ChallengeStatistic.SeasonData](#lq-AccountDetailStatisticV2-ChallengeStatistic-SeasonData)
    - [AccountDetailStatisticV2.CustomizedContestStatistic](#lq-AccountDetailStatisticV2-CustomizedContestStatistic)
    - [AccountDetailStatisticV2.RankStatistic](#lq-AccountDetailStatisticV2-RankStatistic)
    - [AccountDetailStatisticV2.RankStatistic.RankData](#lq-AccountDetailStatisticV2-RankStatistic-RankData)
    - [AccountDetailStatisticV2.RankStatistic.RankData.RankLevelData](#lq-AccountDetailStatisticV2-RankStatistic-RankData-RankLevelData)
    - [AccountFanAchieved](#lq-AccountFanAchieved)
    - [AccountGiftCodeRecord](#lq-AccountGiftCodeRecord)
    - [AccountLevel](#lq-AccountLevel)
    - [AccountMahjongStatistic](#lq-AccountMahjongStatistic)
    - [AccountMahjongStatistic.GameResult](#lq-AccountMahjongStatistic-GameResult)
    - [AccountMahjongStatistic.HuSummary](#lq-AccountMahjongStatistic-HuSummary)
    - [AccountMahjongStatistic.LiQi10Summary](#lq-AccountMahjongStatistic-LiQi10Summary)
    - [AccountMahjongStatistic.Liqi20Summary](#lq-AccountMahjongStatistic-Liqi20Summary)
    - [AccountMahjongStatistic.RoundSummary](#lq-AccountMahjongStatistic-RoundSummary)
    - [AccountMailRecord](#lq-AccountMailRecord)
    - [AccountMailRecord.MailSnapshot](#lq-AccountMailRecord-MailSnapshot)
    - [AccountMiscSnapshot](#lq-AccountMiscSnapshot)
    - [AccountMiscSnapshot.AccountMonthTicketSnapshot](#lq-AccountMiscSnapshot-AccountMonthTicketSnapshot)
    - [AccountMiscSnapshot.AccountMonthTicketSnapshotV2](#lq-AccountMiscSnapshot-AccountMonthTicketSnapshotV2)
    - [AccountMiscSnapshot.AccountRechargeInfo](#lq-AccountMiscSnapshot-AccountRechargeInfo)
    - [AccountMiscSnapshot.AccountRechargeInfo.RechargeRecord](#lq-AccountMiscSnapshot-AccountRechargeInfo-RechargeRecord)
    - [AccountMiscSnapshot.AccountVIP](#lq-AccountMiscSnapshot-AccountVIP)
    - [AccountMiscSnapshot.AccountVIPRewardSnapshot](#lq-AccountMiscSnapshot-AccountVIPRewardSnapshot)
    - [AccountMiscSnapshot.MonthTicketInfo](#lq-AccountMiscSnapshot-MonthTicketInfo)
    - [AccountOwnerData](#lq-AccountOwnerData)
    - [AccountPlayingGame](#lq-AccountPlayingGame)
    - [AccountResourceSnapshot](#lq-AccountResourceSnapshot)
    - [AccountResourceSnapshot.BagItemSnapshot](#lq-AccountResourceSnapshot-BagItemSnapshot)
    - [AccountResourceSnapshot.CurrencySnapshot](#lq-AccountResourceSnapshot-CurrencySnapshot)
    - [AccountResourceSnapshot.TitleSnapshot](#lq-AccountResourceSnapshot-TitleSnapshot)
    - [AccountResourceSnapshot.UsedTitleSnapshot](#lq-AccountResourceSnapshot-UsedTitleSnapshot)
    - [AccountSetting](#lq-AccountSetting)
    - [AccountShiLian](#lq-AccountShiLian)
    - [AccountStatisticByFan](#lq-AccountStatisticByFan)
    - [AccountStatisticByGameMode](#lq-AccountStatisticByGameMode)
    - [AccountStatisticByGameMode.RankScore](#lq-AccountStatisticByGameMode-RankScore)
    - [AccountStatisticByGameMode.RoundEndData](#lq-AccountStatisticByGameMode-RoundEndData)
    - [AccountStatisticData](#lq-AccountStatisticData)
    - [AccountUpdate](#lq-AccountUpdate)
    - [AccountUpdate.AccountABMatchUpdate](#lq-AccountUpdate-AccountABMatchUpdate)
    - [AccountUpdate.AccountABMatchUpdate.MatchPoint](#lq-AccountUpdate-AccountABMatchUpdate-MatchPoint)
    - [AccountUpdate.AccountChallengeUpdate](#lq-AccountUpdate-AccountChallengeUpdate)
    - [AccountUpdate.AchievementUpdate](#lq-AccountUpdate-AchievementUpdate)
    - [AccountUpdate.BadgeUpdate](#lq-AccountUpdate-BadgeUpdate)
    - [AccountUpdate.CharacterUpdate](#lq-AccountUpdate-CharacterUpdate)
    - [AccountUpdate.DailyTaskUpdate](#lq-AccountUpdate-DailyTaskUpdate)
    - [AccountUpdate.MainCharacterUpdate](#lq-AccountUpdate-MainCharacterUpdate)
    - [AccountUpdate.MonthTicketUpdate](#lq-AccountUpdate-MonthTicketUpdate)
    - [AccountUpdate.NumericalUpdate](#lq-AccountUpdate-NumericalUpdate)
    - [AccountUpdate.SegmentTaskUpdate](#lq-AccountUpdate-SegmentTaskUpdate)
    - [AccountUpdate.TaskUpdate](#lq-AccountUpdate-TaskUpdate)
    - [AccountUpdate.TitleUpdate](#lq-AccountUpdate-TitleUpdate)
    - [AchievementProgress](#lq-AchievementProgress)
    - [Activity](#lq-Activity)
    - [ActivityAccumulatedPointData](#lq-ActivityAccumulatedPointData)
    - [ActivityArenaData](#lq-ActivityArenaData)
    - [ActivityBingoCardData](#lq-ActivityBingoCardData)
    - [ActivityBingoCardData.BingoAchievedRecord](#lq-ActivityBingoCardData-BingoAchievedRecord)
    - [ActivityBingoCardData.BingoRewardRecord](#lq-ActivityBingoCardData-BingoRewardRecord)
    - [ActivityBingoData](#lq-ActivityBingoData)
    - [ActivityBuffData](#lq-ActivityBuffData)
    - [ActivityChooseGroupData](#lq-ActivityChooseGroupData)
    - [ActivityChooseUpData](#lq-ActivityChooseUpData)
    - [ActivityCombiningData](#lq-ActivityCombiningData)
    - [ActivityCombiningData.BonusData](#lq-ActivityCombiningData-BonusData)
    - [ActivityCombiningLQData](#lq-ActivityCombiningLQData)
    - [ActivityCombiningMenuData](#lq-ActivityCombiningMenuData)
    - [ActivityCombiningMenuData.MenuRequire](#lq-ActivityCombiningMenuData-MenuRequire)
    - [ActivityCombiningOrderData](#lq-ActivityCombiningOrderData)
    - [ActivityCombiningPoolData](#lq-ActivityCombiningPoolData)
    - [ActivityCombiningWorkbench](#lq-ActivityCombiningWorkbench)
    - [ActivityFeedData](#lq-ActivityFeedData)
    - [ActivityFeedData.CountWithTimeData](#lq-ActivityFeedData-CountWithTimeData)
    - [ActivityFeedData.GiftBoxData](#lq-ActivityFeedData-GiftBoxData)
    - [ActivityFestivalData](#lq-ActivityFestivalData)
    - [ActivityFriendGiftData](#lq-ActivityFriendGiftData)
    - [ActivityFriendGiftData.CountWithTimeData](#lq-ActivityFriendGiftData-CountWithTimeData)
    - [ActivityFriendGiftData.GiftBoxData](#lq-ActivityFriendGiftData-GiftBoxData)
    - [ActivityGachaData](#lq-ActivityGachaData)
    - [ActivityGachaUpdateData](#lq-ActivityGachaUpdateData)
    - [ActivityIdTimeRecord](#lq-ActivityIdTimeRecord)
    - [ActivityIslandData](#lq-ActivityIslandData)
    - [ActivityMMOData](#lq-ActivityMMOData)
    - [ActivityMMOData.ActivityMMOBagData](#lq-ActivityMMOData-ActivityMMOBagData)
    - [ActivityMMOData.ActivityMMOBagData.ActivityMMORandomRecord](#lq-ActivityMMOData-ActivityMMOBagData-ActivityMMORandomRecord)
    - [ActivityMMOData.ActivityMMOCharacterData](#lq-ActivityMMOData-ActivityMMOCharacterData)
    - [ActivityMMOData.ActivityMMOMapData](#lq-ActivityMMOData-ActivityMMOMapData)
    - [ActivityMMOData.ActivityMMOSupportData](#lq-ActivityMMOData-ActivityMMOSupportData)
    - [ActivityMMOData.ActivityMMOTeamData](#lq-ActivityMMOData-ActivityMMOTeamData)
    - [ActivityMMODataChanges](#lq-ActivityMMODataChanges)
    - [ActivityMMODataChanges.ActivityMMOBagDataChanges](#lq-ActivityMMODataChanges-ActivityMMOBagDataChanges)
    - [ActivityMMODataChanges.ActivityMMOCharacterDataChanges](#lq-ActivityMMODataChanges-ActivityMMOCharacterDataChanges)
    - [ActivityMMODataChanges.ActivityMMOEquipmentsArrayDirty](#lq-ActivityMMODataChanges-ActivityMMOEquipmentsArrayDirty)
    - [ActivityMMODataChanges.ActivityMMOMapDataChanges](#lq-ActivityMMODataChanges-ActivityMMOMapDataChanges)
    - [ActivityMMODataChanges.ActivityMMOSupportDataChanges](#lq-ActivityMMODataChanges-ActivityMMOSupportDataChanges)
    - [ActivityMMODataChanges.ActivityMMOTeamDataChanges](#lq-ActivityMMODataChanges-ActivityMMOTeamDataChanges)
    - [ActivityMMODataChanges.ActivityMMOTeamMemberArrayDirty](#lq-ActivityMMODataChanges-ActivityMMOTeamMemberArrayDirty)
    - [ActivityMMOEquipmentData](#lq-ActivityMMOEquipmentData)
    - [ActivityMMOSupportRecord](#lq-ActivityMMOSupportRecord)
    - [ActivityMMOSupportRecordDirty](#lq-ActivityMMOSupportRecordDirty)
    - [ActivityMMOTeamMember](#lq-ActivityMMOTeamMember)
    - [ActivityMarathonCheckData](#lq-ActivityMarathonCheckData)
    - [ActivityMarathonData](#lq-ActivityMarathonData)
    - [ActivityMarathonData.MarathonRaceData](#lq-ActivityMarathonData-MarathonRaceData)
    - [ActivityMarathonData.MarathonRaceHistory](#lq-ActivityMarathonData-MarathonRaceHistory)
    - [ActivityProgressRewardData](#lq-ActivityProgressRewardData)
    - [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges)
    - [ActivityQuestCrewChanges.QCMemberArrayDirty](#lq-ActivityQuestCrewChanges-QCMemberArrayDirty)
    - [ActivityQuestCrewChanges.QCQuestArrayDirty](#lq-ActivityQuestCrewChanges-QCQuestArrayDirty)
    - [ActivityQuestCrewData](#lq-ActivityQuestCrewData)
    - [ActivityQuestCrewEffectResult](#lq-ActivityQuestCrewEffectResult)
    - [ActivityQuestCrewEffectResult.QCItemReward](#lq-ActivityQuestCrewEffectResult-QCItemReward)
    - [ActivityQuestCrewEffectResult.QCQuestConsumeChange](#lq-ActivityQuestCrewEffectResult-QCQuestConsumeChange)
    - [ActivityQuestCrewEffectResult.QCQuestResultChange](#lq-ActivityQuestCrewEffectResult-QCQuestResultChange)
    - [ActivityRankPointData](#lq-ActivityRankPointData)
    - [ActivityShootData](#lq-ActivityShootData)
    - [ActivityShootEnemyInfo](#lq-ActivityShootEnemyInfo)
    - [ActivityShootEnemyInfoDirty](#lq-ActivityShootEnemyInfoDirty)
    - [ActivityShootRewardRecord](#lq-ActivityShootRewardRecord)
    - [ActivityShootValueChange](#lq-ActivityShootValueChange)
    - [ActivityShootValueChange.RewardArrayDirty](#lq-ActivityShootValueChange-RewardArrayDirty)
    - [ActivityShootValueChange.Uint32ValueDirty](#lq-ActivityShootValueChange-Uint32ValueDirty)
    - [ActivitySimulationDailyContest](#lq-ActivitySimulationDailyContest)
    - [ActivitySimulationData](#lq-ActivitySimulationData)
    - [ActivitySimulationGameRecord](#lq-ActivitySimulationGameRecord)
    - [ActivitySimulationGameRecordMessage](#lq-ActivitySimulationGameRecordMessage)
    - [ActivitySimulationTrainRecord](#lq-ActivitySimulationTrainRecord)
    - [ActivitySnowballData](#lq-ActivitySnowballData)
    - [ActivitySnowballPlayerAction](#lq-ActivitySnowballPlayerAction)
    - [ActivitySnowballPlayerAttackedInfo](#lq-ActivitySnowballPlayerAttackedInfo)
    - [ActivitySnowballPlayerState](#lq-ActivitySnowballPlayerState)
    - [ActivitySnowballUpgrade](#lq-ActivitySnowballUpgrade)
    - [ActivitySnowballUpgradeDirty](#lq-ActivitySnowballUpgradeDirty)
    - [ActivitySnowballValueChanges](#lq-ActivitySnowballValueChanges)
    - [ActivitySpotData](#lq-ActivitySpotData)
    - [ActivitySpotData.SpotData](#lq-ActivitySpotData-SpotData)
    - [ActivityStoryData](#lq-ActivityStoryData)
    - [ActivityUpgradeData](#lq-ActivityUpgradeData)
    - [ActivityUpgradeData.LevelGroup](#lq-ActivityUpgradeData-LevelGroup)
    - [ActivityVillageData](#lq-ActivityVillageData)
    - [Announcement](#lq-Announcement)
    - [AntiAddiction](#lq-AntiAddiction)
    - [BadgeAchieveProgress](#lq-BadgeAchieveProgress)
    - [Bag](#lq-Bag)
    - [BagUpdate](#lq-BagUpdate)
    - [BannerActivityData](#lq-BannerActivityData)
    - [BillShortcut](#lq-BillShortcut)
    - [BillingGoods](#lq-BillingGoods)
    - [BillingProduct](#lq-BillingProduct)
    - [BuyRecord](#lq-BuyRecord)
    - [ChangeNicknameRecord](#lq-ChangeNicknameRecord)
    - [Character](#lq-Character)
    - [ChestData](#lq-ChestData)
    - [ChestDataV2](#lq-ChestDataV2)
    - [ClientDeviceInfo](#lq-ClientDeviceInfo)
    - [ClientDeviceInfoLog](#lq-ClientDeviceInfoLog)
    - [ClientVersionInfo](#lq-ClientVersionInfo)
    - [CommentItem](#lq-CommentItem)
    - [ContestDetailRule](#lq-ContestDetailRule)
    - [ContestDetailRuleV2](#lq-ContestDetailRuleV2)
    - [ContestDetailRuleV2.ExtraRule](#lq-ContestDetailRuleV2-ExtraRule)
    - [ContestGameMetaData](#lq-ContestGameMetaData)
    - [ContestGameMetaData.ContestTypeZoneData](#lq-ContestGameMetaData-ContestTypeZoneData)
    - [CustomizedContestAbstract](#lq-CustomizedContestAbstract)
    - [CustomizedContestBase](#lq-CustomizedContestBase)
    - [CustomizedContestDetail](#lq-CustomizedContestDetail)
    - [CustomizedContestExtend](#lq-CustomizedContestExtend)
    - [CustomizedContestGameEnd](#lq-CustomizedContestGameEnd)
    - [CustomizedContestGameEnd.Item](#lq-CustomizedContestGameEnd-Item)
    - [CustomizedContestGamePlan](#lq-CustomizedContestGamePlan)
    - [CustomizedContestGameStart](#lq-CustomizedContestGameStart)
    - [CustomizedContestGameStart.Item](#lq-CustomizedContestGameStart-Item)
    - [CustomizedContestPlayerReport](#lq-CustomizedContestPlayerReport)
    - [Error](#lq-Error)
    - [ExchangeRecord](#lq-ExchangeRecord)
    - [ExecuteResult](#lq-ExecuteResult)
    - [ExecuteReward](#lq-ExecuteReward)
    - [FaithData](#lq-FaithData)
    - [FakeRandomRecords](#lq-FakeRandomRecords)
    - [FavoriteHu](#lq-FavoriteHu)
    - [FeedActivityData](#lq-FeedActivityData)
    - [FeedActivityData.CountWithTimeData](#lq-FeedActivityData-CountWithTimeData)
    - [FeedActivityData.GiftBoxData](#lq-FeedActivityData-GiftBoxData)
    - [FestivalProposalData](#lq-FestivalProposalData)
    - [Friend](#lq-Friend)
    - [GachaRecord](#lq-GachaRecord)
    - [GameConfig](#lq-GameConfig)
    - [GameConnectInfo](#lq-GameConnectInfo)
    - [GameDetailRule](#lq-GameDetailRule)
    - [GameEndAction](#lq-GameEndAction)
    - [GameEndResult](#lq-GameEndResult)
    - [GameEndResult.PlayerItem](#lq-GameEndResult-PlayerItem)
    - [GameFinalSnapshot](#lq-GameFinalSnapshot)
    - [GameFinalSnapshot.AFKInfo](#lq-GameFinalSnapshot-AFKInfo)
    - [GameFinalSnapshot.CalculateParam](#lq-GameFinalSnapshot-CalculateParam)
    - [GameFinalSnapshot.FinalPlayer](#lq-GameFinalSnapshot-FinalPlayer)
    - [GameFinalSnapshot.GameSeat](#lq-GameFinalSnapshot-GameSeat)
    - [GameLiveHead](#lq-GameLiveHead)
    - [GameLiveSegment](#lq-GameLiveSegment)
    - [GameLiveSegmentUri](#lq-GameLiveSegmentUri)
    - [GameLiveUnit](#lq-GameLiveUnit)
    - [GameMetaData](#lq-GameMetaData)
    - [GameMode](#lq-GameMode)
    - [GameNewRoundState](#lq-GameNewRoundState)
    - [GameNoopAction](#lq-GameNoopAction)
    - [GameRoundHuData](#lq-GameRoundHuData)
    - [GameRoundHuData.Fan](#lq-GameRoundHuData-Fan)
    - [GameRoundHuData.HuPai](#lq-GameRoundHuData-HuPai)
    - [GameRoundPlayer](#lq-GameRoundPlayer)
    - [GameRoundPlayerFangChongInfo](#lq-GameRoundPlayerFangChongInfo)
    - [GameRoundPlayerResult](#lq-GameRoundPlayerResult)
    - [GameRoundSnapshot](#lq-GameRoundSnapshot)
    - [GameRuleSetting](#lq-GameRuleSetting)
    - [GameSetting](#lq-GameSetting)
    - [GameTestingEnvironmentSet](#lq-GameTestingEnvironmentSet)
    - [HighestHuRecord](#lq-HighestHuRecord)
    - [I18nContext](#lq-I18nContext)
    - [IslandBagData](#lq-IslandBagData)
    - [IslandBagItemData](#lq-IslandBagItemData)
    - [IslandGoodsData](#lq-IslandGoodsData)
    - [IslandZoneData](#lq-IslandZoneData)
    - [Item](#lq-Item)
    - [ItemGainRecord](#lq-ItemGainRecord)
    - [ItemGainRecords](#lq-ItemGainRecords)
    - [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData)
    - [Mail](#lq-Mail)
    - [MaintainNotice](#lq-MaintainNotice)
    - [MarathonGameRecord](#lq-MarathonGameRecord)
    - [MineActivityData](#lq-MineActivityData)
    - [MineReward](#lq-MineReward)
    - [MonthTicketInfo](#lq-MonthTicketInfo)
    - [NetworkEndpoint](#lq-NetworkEndpoint)
    - [NicknameSetting](#lq-NicknameSetting)
    - [OpenResult](#lq-OpenResult)
    - [PaymentSetting](#lq-PaymentSetting)
    - [PaymentSetting.AlipayData](#lq-PaymentSetting-AlipayData)
    - [PaymentSetting.WechatData](#lq-PaymentSetting-WechatData)
    - [PaymentSettingV2](#lq-PaymentSettingV2)
    - [PaymentSettingV2.PaymentMaintain](#lq-PaymentSettingV2-PaymentMaintain)
    - [PaymentSettingV2.PaymentSettingUnit](#lq-PaymentSettingV2-PaymentSettingUnit)
    - [PlayerBaseView](#lq-PlayerBaseView)
    - [PlayerGameView](#lq-PlayerGameView)
    - [Point](#lq-Point)
    - [QCMember](#lq-QCMember)
    - [QCQuest](#lq-QCQuest)
    - [QuestionnaireBrief](#lq-QuestionnaireBrief)
    - [QuestionnaireDetail](#lq-QuestionnaireDetail)
    - [QuestionnaireQuestion](#lq-QuestionnaireQuestion)
    - [QuestionnaireQuestion.NextQuestionData](#lq-QuestionnaireQuestion-NextQuestionData)
    - [QuestionnaireQuestion.NextQuestionData.QuestionCondition](#lq-QuestionnaireQuestion-NextQuestionData-QuestionCondition)
    - [QuestionnaireQuestion.NextQuestionData.QuestionconditionWrapper](#lq-QuestionnaireQuestion-NextQuestionData-QuestionconditionWrapper)
    - [QuestionnaireQuestion.QuestionOption](#lq-QuestionnaireQuestion-QuestionOption)
    - [QuestionnaireReward](#lq-QuestionnaireReward)
    - [RPGActivity](#lq-RPGActivity)
    - [RPGState](#lq-RPGState)
    - [RandomCharacter](#lq-RandomCharacter)
    - [RecordAnalysisedData](#lq-RecordAnalysisedData)
    - [RecordBaBeiInfo](#lq-RecordBaBeiInfo)
    - [RecordCollectedData](#lq-RecordCollectedData)
    - [RecordGame](#lq-RecordGame)
    - [RecordGame.AccountInfo](#lq-RecordGame-AccountInfo)
    - [RecordGangInfo](#lq-RecordGangInfo)
    - [RecordHuleInfo](#lq-RecordHuleInfo)
    - [RecordHuleInfo.RecordFanInfo](#lq-RecordHuleInfo-RecordFanInfo)
    - [RecordHulesInfo](#lq-RecordHulesInfo)
    - [RecordLiqiInfo](#lq-RecordLiqiInfo)
    - [RecordListEntry](#lq-RecordListEntry)
    - [RecordLiujuInfo](#lq-RecordLiujuInfo)
    - [RecordNoTileInfo](#lq-RecordNoTileInfo)
    - [RecordNoTilePlayerInfo](#lq-RecordNoTilePlayerInfo)
    - [RecordPeiPaiInfo](#lq-RecordPeiPaiInfo)
    - [RecordPlayerResult](#lq-RecordPlayerResult)
    - [RecordRoundInfo](#lq-RecordRoundInfo)
    - [RecordTingPaiInfo](#lq-RecordTingPaiInfo)
    - [ReqCommon](#lq-ReqCommon)
    - [ResAccountUpdate](#lq-ResAccountUpdate)
    - [ResCommon](#lq-ResCommon)
    - [RewardPlusResult](#lq-RewardPlusResult)
    - [RewardPlusResult.Exchange](#lq-RewardPlusResult-Exchange)
    - [RewardSlot](#lq-RewardSlot)
    - [RollingNotice](#lq-RollingNotice)
    - [Room](#lq-Room)
    - [SeerBrief](#lq-SeerBrief)
    - [SeerEvent](#lq-SeerEvent)
    - [SeerPrediction](#lq-SeerPrediction)
    - [SeerRecommend](#lq-SeerRecommend)
    - [SeerReport](#lq-SeerReport)
    - [SeerRound](#lq-SeerRound)
    - [SeerScore](#lq-SeerScore)
    - [SegmentTaskProgress](#lq-SegmentTaskProgress)
    - [ServerSettings](#lq-ServerSettings)
    - [ShopInfo](#lq-ShopInfo)
    - [ShopInfo.SelectedPackageBuyRecord](#lq-ShopInfo-SelectedPackageBuyRecord)
    - [SignedTimeCounterData](#lq-SignedTimeCounterData)
    - [SimulationActionData](#lq-SimulationActionData)
    - [SimulationActionData.ActionDealTileData](#lq-SimulationActionData-ActionDealTileData)
    - [SimulationActionData.ActionDiscardData](#lq-SimulationActionData-ActionDiscardData)
    - [SimulationActionData.ActionFuluData](#lq-SimulationActionData-ActionFuluData)
    - [SimulationActionData.ActionHuleData](#lq-SimulationActionData-ActionHuleData)
    - [SimulationActionData.ActionHuleData.HuleInfo](#lq-SimulationActionData-ActionHuleData-HuleInfo)
    - [SimulationActionData.ActionRiichiData](#lq-SimulationActionData-ActionRiichiData)
    - [SimulationV2Ability](#lq-SimulationV2Ability)
    - [SimulationV2Buff](#lq-SimulationV2Buff)
    - [SimulationV2Data](#lq-SimulationV2Data)
    - [SimulationV2Effect](#lq-SimulationV2Effect)
    - [SimulationV2Event](#lq-SimulationV2Event)
    - [SimulationV2Event.SimulationV2EventSelection](#lq-SimulationV2Event-SimulationV2EventSelection)
    - [SimulationV2Event.SimulationV2EventSelection.SimulationV2EventResult](#lq-SimulationV2Event-SimulationV2EventSelection-SimulationV2EventResult)
    - [SimulationV2EventHistory](#lq-SimulationV2EventHistory)
    - [SimulationV2Match](#lq-SimulationV2Match)
    - [SimulationV2Match.SimulationV2Player](#lq-SimulationV2Match-SimulationV2Player)
    - [SimulationV2MatchHistory](#lq-SimulationV2MatchHistory)
    - [SimulationV2MatchHistory.FindTingArgs](#lq-SimulationV2MatchHistory-FindTingArgs)
    - [SimulationV2MatchHistory.FuluArgs](#lq-SimulationV2MatchHistory-FuluArgs)
    - [SimulationV2MatchHistory.HuleArgs](#lq-SimulationV2MatchHistory-HuleArgs)
    - [SimulationV2MatchHistory.LiujuArgs](#lq-SimulationV2MatchHistory-LiujuArgs)
    - [SimulationV2MatchHistory.PushTingArgs](#lq-SimulationV2MatchHistory-PushTingArgs)
    - [SimulationV2MatchHistory.RiichiArgs](#lq-SimulationV2MatchHistory-RiichiArgs)
    - [SimulationV2MatchHistory.RoundStartArgs](#lq-SimulationV2MatchHistory-RoundStartArgs)
    - [SimulationV2MatchHistory.StoryArgs](#lq-SimulationV2MatchHistory-StoryArgs)
    - [SimulationV2MatchInfo](#lq-SimulationV2MatchInfo)
    - [SimulationV2MatchRecord](#lq-SimulationV2MatchRecord)
    - [SimulationV2PlayerRecord](#lq-SimulationV2PlayerRecord)
    - [SimulationV2Record](#lq-SimulationV2Record)
    - [SimulationV2SeasonData](#lq-SimulationV2SeasonData)
    - [SnowballActivityBossAction](#lq-SnowballActivityBossAction)
    - [SnowballActivityBossAction.SnowballActivityBossAttackInfo](#lq-SnowballActivityBossAction-SnowballActivityBossAttackInfo)
    - [SnowballActivityBossAction.SnowballActivityBossMPConsumeInfo](#lq-SnowballActivityBossAction-SnowballActivityBossMPConsumeInfo)
    - [StringArrayDirty](#lq-StringArrayDirty)
    - [StringDirty](#lq-StringDirty)
    - [TaskProgress](#lq-TaskProgress)
    - [TimeCounterData](#lq-TimeCounterData)
    - [TransparentData](#lq-TransparentData)
    - [UInt32ArrayDirty](#lq-UInt32ArrayDirty)
    - [UInt32Dirty](#lq-UInt32Dirty)
    - [UnlockedStoryData](#lq-UnlockedStoryData)
    - [ViewSlot](#lq-ViewSlot)
    - [VillageBuildingData](#lq-VillageBuildingData)
    - [VillageReward](#lq-VillageReward)
    - [VillageTargetInfo](#lq-VillageTargetInfo)
    - [VillageTaskData](#lq-VillageTaskData)
    - [VillageTripData](#lq-VillageTripData)
    - [VoteData](#lq-VoteData)
    - [Wrapper](#lq-Wrapper)
    - [ZHPShop](#lq-ZHPShop)
    - [ZHPShop.RefreshCount](#lq-ZHPShop-RefreshCount)

    - [GamePlayerState](#lq-GamePlayerState)

- [config.proto](#config-proto)
    - [ConfigTables](#lq-config-ConfigTables)
    - [Field](#lq-config-Field)
    - [SheetData](#lq-config-SheetData)
    - [SheetMeta](#lq-config-SheetMeta)
    - [SheetSchema](#lq-config-SheetSchema)
    - [TableSchema](#lq-config-TableSchema)

- [excel.proto](#excel-proto)
    - [Sheet_AbMatch_ConsumeSeq](#lqc-Sheet_AbMatch_ConsumeSeq)
    - [Sheet_AbMatch_MatchInfo](#lqc-Sheet_AbMatch_MatchInfo)
    - [Sheet_AbMatch_Point](#lqc-Sheet_AbMatch_Point)
    - [Sheet_AbMatch_RewardSeq](#lqc-Sheet_AbMatch_RewardSeq)
    - [Sheet_Achievement_Achievement](#lqc-Sheet_Achievement_Achievement)
    - [Sheet_Achievement_AchievementGroup](#lqc-Sheet_Achievement_AchievementGroup)
    - [Sheet_Achievement_Badge](#lqc-Sheet_Achievement_Badge)
    - [Sheet_Achievement_BadgeGroup](#lqc-Sheet_Achievement_BadgeGroup)
    - [Sheet_Activity_Activity](#lqc-Sheet_Activity_Activity)
    - [Sheet_Activity_ActivityBanner](#lqc-Sheet_Activity_ActivityBanner)
    - [Sheet_Activity_ActivityBuff](#lqc-Sheet_Activity_ActivityBuff)
    - [Sheet_Activity_ActivityDesktop](#lqc-Sheet_Activity_ActivityDesktop)
    - [Sheet_Activity_ActivityGuide](#lqc-Sheet_Activity_ActivityGuide)
    - [Sheet_Activity_ActivityItem](#lqc-Sheet_Activity_ActivityItem)
    - [Sheet_Activity_ActivityRoom](#lqc-Sheet_Activity_ActivityRoom)
    - [Sheet_Activity_AmuletUpgrade](#lqc-Sheet_Activity_AmuletUpgrade)
    - [Sheet_Activity_ArenaActivity](#lqc-Sheet_Activity_ArenaActivity)
    - [Sheet_Activity_ArenaReward](#lqc-Sheet_Activity_ArenaReward)
    - [Sheet_Activity_ArenaRewardDisplay](#lqc-Sheet_Activity_ArenaRewardDisplay)
    - [Sheet_Activity_BuffCondition](#lqc-Sheet_Activity_BuffCondition)
    - [Sheet_Activity_ChestReplaceUp](#lqc-Sheet_Activity_ChestReplaceUp)
    - [Sheet_Activity_ChestUp](#lqc-Sheet_Activity_ChestUp)
    - [Sheet_Activity_ChooseUpActivity](#lqc-Sheet_Activity_ChooseUpActivity)
    - [Sheet_Activity_ChooseUpReplace](#lqc-Sheet_Activity_ChooseUpReplace)
    - [Sheet_Activity_CombiningActivityInfo](#lqc-Sheet_Activity_CombiningActivityInfo)
    - [Sheet_Activity_CombiningCraft](#lqc-Sheet_Activity_CombiningCraft)
    - [Sheet_Activity_CombiningCraftPool](#lqc-Sheet_Activity_CombiningCraftPool)
    - [Sheet_Activity_CombiningCustomer](#lqc-Sheet_Activity_CombiningCustomer)
    - [Sheet_Activity_CombiningMap](#lqc-Sheet_Activity_CombiningMap)
    - [Sheet_Activity_CombiningOrder](#lqc-Sheet_Activity_CombiningOrder)
    - [Sheet_Activity_DailySign](#lqc-Sheet_Activity_DailySign)
    - [Sheet_Activity_Exchange](#lqc-Sheet_Activity_Exchange)
    - [Sheet_Activity_FeedActivityInfo](#lqc-Sheet_Activity_FeedActivityInfo)
    - [Sheet_Activity_FeedActivityReward](#lqc-Sheet_Activity_FeedActivityReward)
    - [Sheet_Activity_FestivalActivity](#lqc-Sheet_Activity_FestivalActivity)
    - [Sheet_Activity_FestivalEnding](#lqc-Sheet_Activity_FestivalEnding)
    - [Sheet_Activity_FestivalEvent](#lqc-Sheet_Activity_FestivalEvent)
    - [Sheet_Activity_FestivalLevel](#lqc-Sheet_Activity_FestivalLevel)
    - [Sheet_Activity_FestivalProposal](#lqc-Sheet_Activity_FestivalProposal)
    - [Sheet_Activity_FlipInfo](#lqc-Sheet_Activity_FlipInfo)
    - [Sheet_Activity_FlipTask](#lqc-Sheet_Activity_FlipTask)
    - [Sheet_Activity_FriendGiftActivity](#lqc-Sheet_Activity_FriendGiftActivity)
    - [Sheet_Activity_GachaActivityInfo](#lqc-Sheet_Activity_GachaActivityInfo)
    - [Sheet_Activity_GachaControl](#lqc-Sheet_Activity_GachaControl)
    - [Sheet_Activity_GachaPool](#lqc-Sheet_Activity_GachaPool)
    - [Sheet_Activity_GamePoint](#lqc-Sheet_Activity_GamePoint)
    - [Sheet_Activity_GamePointFilter](#lqc-Sheet_Activity_GamePointFilter)
    - [Sheet_Activity_GamePointInfo](#lqc-Sheet_Activity_GamePointInfo)
    - [Sheet_Activity_GamePointRank](#lqc-Sheet_Activity_GamePointRank)
    - [Sheet_Activity_GameTask](#lqc-Sheet_Activity_GameTask)
    - [Sheet_Activity_IslandActivity](#lqc-Sheet_Activity_IslandActivity)
    - [Sheet_Activity_IslandBag](#lqc-Sheet_Activity_IslandBag)
    - [Sheet_Activity_IslandGoods](#lqc-Sheet_Activity_IslandGoods)
    - [Sheet_Activity_IslandMap](#lqc-Sheet_Activity_IslandMap)
    - [Sheet_Activity_IslandNews](#lqc-Sheet_Activity_IslandNews)
    - [Sheet_Activity_IslandShop](#lqc-Sheet_Activity_IslandShop)
    - [Sheet_Activity_LiverEventInfo](#lqc-Sheet_Activity_LiverEventInfo)
    - [Sheet_Activity_LiverTextInfo](#lqc-Sheet_Activity_LiverTextInfo)
    - [Sheet_Activity_MineActivity](#lqc-Sheet_Activity_MineActivity)
    - [Sheet_Activity_MineReward](#lqc-Sheet_Activity_MineReward)
    - [Sheet_Activity_PeriodTask](#lqc-Sheet_Activity_PeriodTask)
    - [Sheet_Activity_ProgressReward](#lqc-Sheet_Activity_ProgressReward)
    - [Sheet_Activity_RandomTaskInfo](#lqc-Sheet_Activity_RandomTaskInfo)
    - [Sheet_Activity_RandomTaskPool](#lqc-Sheet_Activity_RandomTaskPool)
    - [Sheet_Activity_Rank](#lqc-Sheet_Activity_Rank)
    - [Sheet_Activity_RankReward](#lqc-Sheet_Activity_RankReward)
    - [Sheet_Activity_RewardMail](#lqc-Sheet_Activity_RewardMail)
    - [Sheet_Activity_RichmanEvent](#lqc-Sheet_Activity_RichmanEvent)
    - [Sheet_Activity_RichmanInfo](#lqc-Sheet_Activity_RichmanInfo)
    - [Sheet_Activity_RichmanLevel](#lqc-Sheet_Activity_RichmanLevel)
    - [Sheet_Activity_RichmanMap](#lqc-Sheet_Activity_RichmanMap)
    - [Sheet_Activity_RichmanRewardSeq](#lqc-Sheet_Activity_RichmanRewardSeq)
    - [Sheet_Activity_RpgActivity](#lqc-Sheet_Activity_RpgActivity)
    - [Sheet_Activity_RpgMonsterGroup](#lqc-Sheet_Activity_RpgMonsterGroup)
    - [Sheet_Activity_RpgV2Activity](#lqc-Sheet_Activity_RpgV2Activity)
    - [Sheet_Activity_SegmentTask](#lqc-Sheet_Activity_SegmentTask)
    - [Sheet_Activity_SimulationActivityInfo](#lqc-Sheet_Activity_SimulationActivityInfo)
    - [Sheet_Activity_SnsActivity](#lqc-Sheet_Activity_SnsActivity)
    - [Sheet_Activity_SpotActivity](#lqc-Sheet_Activity_SpotActivity)
    - [Sheet_Activity_StoryActivity](#lqc-Sheet_Activity_StoryActivity)
    - [Sheet_Activity_StoryEnding](#lqc-Sheet_Activity_StoryEnding)
    - [Sheet_Activity_SummerStory](#lqc-Sheet_Activity_SummerStory)
    - [Sheet_Activity_SummerStoryReward](#lqc-Sheet_Activity_SummerStoryReward)
    - [Sheet_Activity_Task](#lqc-Sheet_Activity_Task)
    - [Sheet_Activity_TaskDisplay](#lqc-Sheet_Activity_TaskDisplay)
    - [Sheet_Activity_UpgradeActivity](#lqc-Sheet_Activity_UpgradeActivity)
    - [Sheet_Activity_UpgradeActivityDisplay](#lqc-Sheet_Activity_UpgradeActivityDisplay)
    - [Sheet_Activity_UpgradeActivityReward](#lqc-Sheet_Activity_UpgradeActivityReward)
    - [Sheet_Activity_VillageActivityInfo](#lqc-Sheet_Activity_VillageActivityInfo)
    - [Sheet_Activity_VillageBuilding](#lqc-Sheet_Activity_VillageBuilding)
    - [Sheet_Activity_VillageTask](#lqc-Sheet_Activity_VillageTask)
    - [Sheet_Activity_VoteActivity](#lqc-Sheet_Activity_VoteActivity)
    - [Sheet_Amulet_AmuletActivity](#lqc-Sheet_Amulet_AmuletActivity)
    - [Sheet_Amulet_AmuletBadge](#lqc-Sheet_Amulet_AmuletBadge)
    - [Sheet_Amulet_AmuletBuff](#lqc-Sheet_Amulet_AmuletBuff)
    - [Sheet_Amulet_AmuletEffect](#lqc-Sheet_Amulet_AmuletEffect)
    - [Sheet_Amulet_AmuletEffectGroup](#lqc-Sheet_Amulet_AmuletEffectGroup)
    - [Sheet_Amulet_AmuletFan](#lqc-Sheet_Amulet_AmuletFan)
    - [Sheet_Amulet_AmuletGames](#lqc-Sheet_Amulet_AmuletGames)
    - [Sheet_Amulet_AmuletGoods](#lqc-Sheet_Amulet_AmuletGoods)
    - [Sheet_Amulet_AmuletPool](#lqc-Sheet_Amulet_AmuletPool)
    - [Sheet_Amulet_AmuletRewards](#lqc-Sheet_Amulet_AmuletRewards)
    - [Sheet_Amulet_AmuletShopUpgrade](#lqc-Sheet_Amulet_AmuletShopUpgrade)
    - [Sheet_Amulet_AmuletTag](#lqc-Sheet_Amulet_AmuletTag)
    - [Sheet_Amulet_AmuletTask](#lqc-Sheet_Amulet_AmuletTask)
    - [Sheet_Amulet_AmuletUpgrade](#lqc-Sheet_Amulet_AmuletUpgrade)
    - [Sheet_Animation_Animation](#lqc-Sheet_Animation_Animation)
    - [Sheet_Audio_Audio](#lqc-Sheet_Audio_Audio)
    - [Sheet_Audio_Bgm](#lqc-Sheet_Audio_Bgm)
    - [Sheet_Character_Cutin](#lqc-Sheet_Character_Cutin)
    - [Sheet_Character_Emoji](#lqc-Sheet_Character_Emoji)
    - [Sheet_Character_Skin](#lqc-Sheet_Character_Skin)
    - [Sheet_Chest_Chest](#lqc-Sheet_Chest_Chest)
    - [Sheet_Chest_ChestShop](#lqc-Sheet_Chest_ChestShop)
    - [Sheet_Chest_ItemPool](#lqc-Sheet_Chest_ItemPool)
    - [Sheet_Chest_ItemPrice](#lqc-Sheet_Chest_ItemPrice)
    - [Sheet_Chest_Pool](#lqc-Sheet_Chest_Pool)
    - [Sheet_Chest_PoolSeq](#lqc-Sheet_Chest_PoolSeq)
    - [Sheet_Chest_Preview](#lqc-Sheet_Chest_Preview)
    - [Sheet_Chest_ReplacePool](#lqc-Sheet_Chest_ReplacePool)
    - [Sheet_Chest_ReplaceUp](#lqc-Sheet_Chest_ReplaceUp)
    - [Sheet_Chest_Up](#lqc-Sheet_Chest_Up)
    - [Sheet_Compose_Characompose](#lqc-Sheet_Compose_Characompose)
    - [Sheet_Contest_Contest](#lqc-Sheet_Contest_Contest)
    - [Sheet_Desktop_Chest](#lqc-Sheet_Desktop_Chest)
    - [Sheet_Desktop_FieldSpell](#lqc-Sheet_Desktop_FieldSpell)
    - [Sheet_Desktop_FriendRoom](#lqc-Sheet_Desktop_FriendRoom)
    - [Sheet_Desktop_Matchmode](#lqc-Sheet_Desktop_Matchmode)
    - [Sheet_Desktop_Settings](#lqc-Sheet_Desktop_Settings)
    - [Sheet_Desktop_TourPresetRule](#lqc-Sheet_Desktop_TourPresetRule)
    - [Sheet_Events_BaseTask](#lqc-Sheet_Events_BaseTask)
    - [Sheet_Events_Dailyevent](#lqc-Sheet_Events_Dailyevent)
    - [Sheet_Events_Soscoin](#lqc-Sheet_Events_Soscoin)
    - [Sheet_Exchange_Exchange](#lqc-Sheet_Exchange_Exchange)
    - [Sheet_Exchange_Fushiquanexchange](#lqc-Sheet_Exchange_Fushiquanexchange)
    - [Sheet_Exchange_Searchexchange](#lqc-Sheet_Exchange_Searchexchange)
    - [Sheet_Fan_Fan](#lqc-Sheet_Fan_Fan)
    - [Sheet_Fandesc_Fandesc](#lqc-Sheet_Fandesc_Fandesc)
    - [Sheet_GameLive_SelectFilters](#lqc-Sheet_GameLive_SelectFilters)
    - [Sheet_Global_Global](#lqc-Sheet_Global_Global)
    - [Sheet_Info_Error](#lqc-Sheet_Info_Error)
    - [Sheet_Info_Forbidden](#lqc-Sheet_Info_Forbidden)
    - [Sheet_Info_Near](#lqc-Sheet_Info_Near)
    - [Sheet_Info_Translate](#lqc-Sheet_Info_Translate)
    - [Sheet_ItemDefinition_Character](#lqc-Sheet_ItemDefinition_Character)
    - [Sheet_ItemDefinition_Currency](#lqc-Sheet_ItemDefinition_Currency)
    - [Sheet_ItemDefinition_FakeRandomPool](#lqc-Sheet_ItemDefinition_FakeRandomPool)
    - [Sheet_ItemDefinition_FunctionItem](#lqc-Sheet_ItemDefinition_FunctionItem)
    - [Sheet_ItemDefinition_Item](#lqc-Sheet_ItemDefinition_Item)
    - [Sheet_ItemDefinition_ItemManualPool](#lqc-Sheet_ItemDefinition_ItemManualPool)
    - [Sheet_ItemDefinition_ItemPackage](#lqc-Sheet_ItemDefinition_ItemPackage)
    - [Sheet_ItemDefinition_ItemRecovery](#lqc-Sheet_ItemDefinition_ItemRecovery)
    - [Sheet_ItemDefinition_LoadingImage](#lqc-Sheet_ItemDefinition_LoadingImage)
    - [Sheet_ItemDefinition_Skin](#lqc-Sheet_ItemDefinition_Skin)
    - [Sheet_ItemDefinition_SourceLimit](#lqc-Sheet_ItemDefinition_SourceLimit)
    - [Sheet_ItemDefinition_Title](#lqc-Sheet_ItemDefinition_Title)
    - [Sheet_ItemDefinition_View](#lqc-Sheet_ItemDefinition_View)
    - [Sheet_Leaderboard_Leaderboard](#lqc-Sheet_Leaderboard_Leaderboard)
    - [Sheet_LevelDefinition_Character](#lqc-Sheet_LevelDefinition_Character)
    - [Sheet_LevelDefinition_LevelDefinition](#lqc-Sheet_LevelDefinition_LevelDefinition)
    - [Sheet_LevelDefinition_TopRank](#lqc-Sheet_LevelDefinition_TopRank)
    - [Sheet_LevelDefinition_Trail](#lqc-Sheet_LevelDefinition_Trail)
    - [Sheet_Mall_ChannelConfig](#lqc-Sheet_Mall_ChannelConfig)
    - [Sheet_Mall_Goods](#lqc-Sheet_Mall_Goods)
    - [Sheet_Mall_GoodsShelves](#lqc-Sheet_Mall_GoodsShelves)
    - [Sheet_Mall_MonthTicket](#lqc-Sheet_Mall_MonthTicket)
    - [Sheet_Mall_MonthTicketInfo](#lqc-Sheet_Mall_MonthTicketInfo)
    - [Sheet_Mall_Product](#lqc-Sheet_Mall_Product)
    - [Sheet_Mall_ZoneParams](#lqc-Sheet_Mall_ZoneParams)
    - [Sheet_MatchShilian_Shilian](#lqc-Sheet_MatchShilian_Shilian)
    - [Sheet_MatchShilian_ShilianReward](#lqc-Sheet_MatchShilian_ShilianReward)
    - [Sheet_MatchShilian_ShilianTime](#lqc-Sheet_MatchShilian_ShilianTime)
    - [Sheet_MiscFunction_DailySignIn](#lqc-Sheet_MiscFunction_DailySignIn)
    - [Sheet_OutfitConfig_EffectLiqi](#lqc-Sheet_OutfitConfig_EffectLiqi)
    - [Sheet_OutfitConfig_Hand](#lqc-Sheet_OutfitConfig_Hand)
    - [Sheet_OutfitConfig_Headframe](#lqc-Sheet_OutfitConfig_Headframe)
    - [Sheet_OutfitConfig_Liqi](#lqc-Sheet_OutfitConfig_Liqi)
    - [Sheet_OutfitConfig_Mjp](#lqc-Sheet_OutfitConfig_Mjp)
    - [Sheet_OutfitConfig_Mjpface](#lqc-Sheet_OutfitConfig_Mjpface)
    - [Sheet_OutfitConfig_Mpzs](#lqc-Sheet_OutfitConfig_Mpzs)
    - [Sheet_OutfitConfig_Ron](#lqc-Sheet_OutfitConfig_Ron)
    - [Sheet_OutfitConfig_Tablecloth](#lqc-Sheet_OutfitConfig_Tablecloth)
    - [Sheet_RankIntroduce_Rank](#lqc-Sheet_RankIntroduce_Rank)
    - [Sheet_RankIntroduce_Rank3](#lqc-Sheet_RankIntroduce_Rank3)
    - [Sheet_Season_LevelTicket](#lqc-Sheet_Season_LevelTicket)
    - [Sheet_Season_LevelTicketPool](#lqc-Sheet_Season_LevelTicketPool)
    - [Sheet_Season_Season](#lqc-Sheet_Season_Season)
    - [Sheet_Season_SeasonReward](#lqc-Sheet_Season_SeasonReward)
    - [Sheet_Season_TicketRetry](#lqc-Sheet_Season_TicketRetry)
    - [Sheet_Shops_Goods](#lqc-Sheet_Shops_Goods)
    - [Sheet_Shops_GoodsPackage](#lqc-Sheet_Shops_GoodsPackage)
    - [Sheet_Shops_IntervalRefreshGoods](#lqc-Sheet_Shops_IntervalRefreshGoods)
    - [Sheet_Shops_ItemPackage](#lqc-Sheet_Shops_ItemPackage)
    - [Sheet_Shops_ZhpGoods](#lqc-Sheet_Shops_ZhpGoods)
    - [Sheet_Shops_ZhpRefreshGroup](#lqc-Sheet_Shops_ZhpRefreshGroup)
    - [Sheet_Shops_ZhpRefreshPrice](#lqc-Sheet_Shops_ZhpRefreshPrice)
    - [Sheet_Simulation_SimV2Buff](#lqc-Sheet_Simulation_SimV2Buff)
    - [Sheet_Simulation_SimV2Character](#lqc-Sheet_Simulation_SimV2Character)
    - [Sheet_Simulation_SimV2Effect](#lqc-Sheet_Simulation_SimV2Effect)
    - [Sheet_Simulation_SimV2Event](#lqc-Sheet_Simulation_SimV2Event)
    - [Sheet_Simulation_SimV2Info](#lqc-Sheet_Simulation_SimV2Info)
    - [Sheet_Simulation_SimV2Reward](#lqc-Sheet_Simulation_SimV2Reward)
    - [Sheet_Simulation_SimV2Roll](#lqc-Sheet_Simulation_SimV2Roll)
    - [Sheet_Simulation_SimV2Round](#lqc-Sheet_Simulation_SimV2Round)
    - [Sheet_Simulation_SimV2Selection](#lqc-Sheet_Simulation_SimV2Selection)
    - [Sheet_Simulation_SimV2SelectionResult](#lqc-Sheet_Simulation_SimV2SelectionResult)
    - [Sheet_Simulation_SimV2Story](#lqc-Sheet_Simulation_SimV2Story)
    - [Sheet_Simulation_SimV2Trigger](#lqc-Sheet_Simulation_SimV2Trigger)
    - [Sheet_Simulation_SimV2Upgrade](#lqc-Sheet_Simulation_SimV2Upgrade)
    - [Sheet_Spot_AudioSpot](#lqc-Sheet_Spot_AudioSpot)
    - [Sheet_Spot_CharacterSpot](#lqc-Sheet_Spot_CharacterSpot)
    - [Sheet_Spot_Event](#lqc-Sheet_Spot_Event)
    - [Sheet_Spot_Rewards](#lqc-Sheet_Spot_Rewards)
    - [Sheet_Spot_SkinSpot](#lqc-Sheet_Spot_SkinSpot)
    - [Sheet_Spot_Spot](#lqc-Sheet_Spot_Spot)
    - [Sheet_Str_Event](#lqc-Sheet_Str_Event)
    - [Sheet_Str_Str](#lqc-Sheet_Str_Str)
    - [Sheet_Tournament_Tournaments](#lqc-Sheet_Tournament_Tournaments)
    - [Sheet_Tutorial_Init](#lqc-Sheet_Tutorial_Init)
    - [Sheet_Tutorial_Step](#lqc-Sheet_Tutorial_Step)
    - [Sheet_Vip_Vip](#lqc-Sheet_Vip_Vip)
    - [Sheet_Voice_Event](#lqc-Sheet_Voice_Event)
    - [Sheet_Voice_Sound](#lqc-Sheet_Voice_Sound)
    - [Sheet_Voice_Spot](#lqc-Sheet_Voice_Spot)

- [liqi_struct.proto](#liqi_struct-proto)
    - [ActionAnGangAddGang](#lq-ActionAnGangAddGang)
    - [ActionBaBei](#lq-ActionBaBei)
    - [ActionChangeTile](#lq-ActionChangeTile)
    - [ActionChiPengGang](#lq-ActionChiPengGang)
    - [ActionDealTile](#lq-ActionDealTile)
    - [ActionDiscardTile](#lq-ActionDiscardTile)
    - [ActionFillAwaitingTiles](#lq-ActionFillAwaitingTiles)
    - [ActionGangResult](#lq-ActionGangResult)
    - [ActionGangResultEnd](#lq-ActionGangResultEnd)
    - [ActionHule](#lq-ActionHule)
    - [ActionHuleXueZhanEnd](#lq-ActionHuleXueZhanEnd)
    - [ActionHuleXueZhanMid](#lq-ActionHuleXueZhanMid)
    - [ActionLiuJu](#lq-ActionLiuJu)
    - [ActionLockTile](#lq-ActionLockTile)
    - [ActionMJStart](#lq-ActionMJStart)
    - [ActionNewCard](#lq-ActionNewCard)
    - [ActionNewRound](#lq-ActionNewRound)
    - [ActionNoTile](#lq-ActionNoTile)
    - [ActionPrototype](#lq-ActionPrototype)
    - [ActionRevealTile](#lq-ActionRevealTile)
    - [ActionSelectGap](#lq-ActionSelectGap)
    - [ActionSubmit](#lq-ActionSubmit)
    - [ActionTake](#lq-ActionTake)
    - [ActionUnveilTile](#lq-ActionUnveilTile)
    - [ChuanmaGang](#lq-ChuanmaGang)
    - [FanInfo](#lq-FanInfo)
    - [GameAction](#lq-GameAction)
    - [GameChiPengGang](#lq-GameChiPengGang)
    - [GameDetailRecords](#lq-GameDetailRecords)
    - [GameEnd](#lq-GameEnd)
    - [GameSelfOperation](#lq-GameSelfOperation)
    - [GameSnapshot](#lq-GameSnapshot)
    - [GameSnapshot.PlayerSnapshot](#lq-GameSnapshot-PlayerSnapshot)
    - [GameSnapshot.PlayerSnapshot.Fulu](#lq-GameSnapshot-PlayerSnapshot-Fulu)
    - [GameUserEvent](#lq-GameUserEvent)
    - [GameUserInput](#lq-GameUserInput)
    - [GameVoteGameEnd](#lq-GameVoteGameEnd)
    - [HuInfoXueZhanMid](#lq-HuInfoXueZhanMid)
    - [HuleInfo](#lq-HuleInfo)
    - [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo)
    - [LiQiSuccess](#lq-LiQiSuccess)
    - [MuyuInfo](#lq-MuyuInfo)
    - [NewRoundOpenedTiles](#lq-NewRoundOpenedTiles)
    - [NoTilePlayerInfo](#lq-NoTilePlayerInfo)
    - [NoTileScoreInfo](#lq-NoTileScoreInfo)
    - [OptionalOperation](#lq-OptionalOperation)
    - [OptionalOperationList](#lq-OptionalOperationList)
    - [PlayerLeaving](#lq-PlayerLeaving)
    - [RecordAnGangAddGang](#lq-RecordAnGangAddGang)
    - [RecordBaBei](#lq-RecordBaBei)
    - [RecordChangeTile](#lq-RecordChangeTile)
    - [RecordChangeTile.ChangeTile](#lq-RecordChangeTile-ChangeTile)
    - [RecordChangeTile.TingPai](#lq-RecordChangeTile-TingPai)
    - [RecordChiPengGang](#lq-RecordChiPengGang)
    - [RecordDealTile](#lq-RecordDealTile)
    - [RecordDiscardTile](#lq-RecordDiscardTile)
    - [RecordFillAwaitingTiles](#lq-RecordFillAwaitingTiles)
    - [RecordGangResult](#lq-RecordGangResult)
    - [RecordGangResultEnd](#lq-RecordGangResultEnd)
    - [RecordHule](#lq-RecordHule)
    - [RecordHuleXueZhanEnd](#lq-RecordHuleXueZhanEnd)
    - [RecordHuleXueZhanMid](#lq-RecordHuleXueZhanMid)
    - [RecordLiuJu](#lq-RecordLiuJu)
    - [RecordLockTile](#lq-RecordLockTile)
    - [RecordNewCard](#lq-RecordNewCard)
    - [RecordNewRound](#lq-RecordNewRound)
    - [RecordNewRound.TingPai](#lq-RecordNewRound-TingPai)
    - [RecordNoTile](#lq-RecordNoTile)
    - [RecordRevealTile](#lq-RecordRevealTile)
    - [RecordSelectGap](#lq-RecordSelectGap)
    - [RecordSelectGap.TingPai](#lq-RecordSelectGap-TingPai)
    - [RecordSubmit](#lq-RecordSubmit)
    - [RecordTake](#lq-RecordTake)
    - [RecordTake.TingPai](#lq-RecordTake-TingPai)
    - [RecordUnveilTile](#lq-RecordUnveilTile)
    - [SubmitGroup](#lq-SubmitGroup)
    - [SubmitInfo](#lq-SubmitInfo)
    - [TakeInfo](#lq-TakeInfo)
    - [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo)
    - [TingPaiInfo](#lq-TingPaiInfo)
    - [XiaKeShangInfo](#lq-XiaKeShangInfo)
    - [YongchangInfo](#lq-YongchangInfo)

- [notify_lobby.proto](#notify_lobby-proto)
    - [NotifyAFKResult](#lq-NotifyAFKResult)
    - [NotifyAccountChallengeTaskUpdate](#lq-NotifyAccountChallengeTaskUpdate)
    - [NotifyAccountLogout](#lq-NotifyAccountLogout)
    - [NotifyAccountRandomTaskUpdate](#lq-NotifyAccountRandomTaskUpdate)
    - [NotifyAccountUpdate](#lq-NotifyAccountUpdate)
    - [NotifyActivityChange](#lq-NotifyActivityChange)
    - [NotifyActivityPeriodTaskUpdate](#lq-NotifyActivityPeriodTaskUpdate)
    - [NotifyActivityPointV2](#lq-NotifyActivityPointV2)
    - [NotifyActivityPointV2.ActivityPoint](#lq-NotifyActivityPointV2-ActivityPoint)
    - [NotifyActivityRewardV2](#lq-NotifyActivityRewardV2)
    - [NotifyActivityRewardV2.ActivityReward](#lq-NotifyActivityRewardV2-ActivityReward)
    - [NotifyActivitySegmentTaskUpdate](#lq-NotifyActivitySegmentTaskUpdate)
    - [NotifyActivityTaskUpdate](#lq-NotifyActivityTaskUpdate)
    - [NotifyActivityUpdate](#lq-NotifyActivityUpdate)
    - [NotifyActivityUpdate.FeedActivityData](#lq-NotifyActivityUpdate-FeedActivityData)
    - [NotifyActivityUpdate.FeedActivityData.CountWithTimeData](#lq-NotifyActivityUpdate-FeedActivityData-CountWithTimeData)
    - [NotifyActivityUpdate.FeedActivityData.GiftBoxData](#lq-NotifyActivityUpdate-FeedActivityData-GiftBoxData)
    - [NotifyAnnouncementUpdate](#lq-NotifyAnnouncementUpdate)
    - [NotifyAnnouncementUpdate.AnnouncementUpdate](#lq-NotifyAnnouncementUpdate-AnnouncementUpdate)
    - [NotifyAnotherLogin](#lq-NotifyAnotherLogin)
    - [NotifyClientMessage](#lq-NotifyClientMessage)
    - [NotifyConnectionShutdown](#lq-NotifyConnectionShutdown)
    - [NotifyCustomContestAccountMsg](#lq-NotifyCustomContestAccountMsg)
    - [NotifyCustomContestState](#lq-NotifyCustomContestState)
    - [NotifyCustomContestSystemMsg](#lq-NotifyCustomContestSystemMsg)
    - [NotifyCustomizedContestPlanCancel](#lq-NotifyCustomizedContestPlanCancel)
    - [NotifyCustomizedContestPlanReady](#lq-NotifyCustomizedContestPlanReady)
    - [NotifyCustomizedContestReady](#lq-NotifyCustomizedContestReady)
    - [NotifyCustomizedContestRuleModify](#lq-NotifyCustomizedContestRuleModify)
    - [NotifyDailyTaskUpdate](#lq-NotifyDailyTaskUpdate)
    - [NotifyDeleteMail](#lq-NotifyDeleteMail)
    - [NotifyFriendChange](#lq-NotifyFriendChange)
    - [NotifyFriendStateChange](#lq-NotifyFriendStateChange)
    - [NotifyFriendViewChange](#lq-NotifyFriendViewChange)
    - [NotifyGameFinishRewardV2](#lq-NotifyGameFinishRewardV2)
    - [NotifyGameFinishRewardV2.CharacterGift](#lq-NotifyGameFinishRewardV2-CharacterGift)
    - [NotifyGameFinishRewardV2.LevelChange](#lq-NotifyGameFinishRewardV2-LevelChange)
    - [NotifyGameFinishRewardV2.MainCharacter](#lq-NotifyGameFinishRewardV2-MainCharacter)
    - [NotifyGameFinishRewardV2.MatchChest](#lq-NotifyGameFinishRewardV2-MatchChest)
    - [NotifyGiftSendRefresh](#lq-NotifyGiftSendRefresh)
    - [NotifyIntervalUpdate](#lq-NotifyIntervalUpdate)
    - [NotifyLeaderboardPointV2](#lq-NotifyLeaderboardPointV2)
    - [NotifyLeaderboardPointV2.LeaderboardPoint](#lq-NotifyLeaderboardPointV2-LeaderboardPoint)
    - [NotifyLoginQueueFinished](#lq-NotifyLoginQueueFinished)
    - [NotifyMaintainNotice](#lq-NotifyMaintainNotice)
    - [NotifyMatchFailed](#lq-NotifyMatchFailed)
    - [NotifyMatchGameStart](#lq-NotifyMatchGameStart)
    - [NotifyMatchTimeout](#lq-NotifyMatchTimeout)
    - [NotifyNewComment](#lq-NotifyNewComment)
    - [NotifyNewFriendApply](#lq-NotifyNewFriendApply)
    - [NotifyNewMail](#lq-NotifyNewMail)
    - [NotifyPayResult](#lq-NotifyPayResult)
    - [NotifyPayResult.ResourceModify](#lq-NotifyPayResult-ResourceModify)
    - [NotifyReviveCoinUpdate](#lq-NotifyReviveCoinUpdate)
    - [NotifyRollingNotice](#lq-NotifyRollingNotice)
    - [NotifyRoomGameStart](#lq-NotifyRoomGameStart)
    - [NotifyRoomKickOut](#lq-NotifyRoomKickOut)
    - [NotifyRoomPlayerDressing](#lq-NotifyRoomPlayerDressing)
    - [NotifyRoomPlayerDressing.AccountDressingState](#lq-NotifyRoomPlayerDressing-AccountDressingState)
    - [NotifyRoomPlayerReady](#lq-NotifyRoomPlayerReady)
    - [NotifyRoomPlayerReady.AccountReadyState](#lq-NotifyRoomPlayerReady-AccountReadyState)
    - [NotifyRoomPlayerUpdate](#lq-NotifyRoomPlayerUpdate)
    - [NotifySeerReport](#lq-NotifySeerReport)
    - [NotifyServerSetting](#lq-NotifyServerSetting)
    - [NotifyShopUpdate](#lq-NotifyShopUpdate)
    - [NotifyVipLevelChange](#lq-NotifyVipLevelChange)

- [services.proto](#services-proto)
    - [FastTest](#lq-FastTest)
    - [Lobby](#lq-Lobby)
    - [Route](#lq-Route)

- [Scalar Value Types](#scalar-value-types)



<a name="amulet_struct-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## amulet_struct.proto



<a name="lq-ActivityAmuletData"></a>

### ActivityAmuletData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| game | [AmuletGameData](#lq-AmuletGameData) |  |  |
| version | [uint32](#uint32) |  |  |
| upgrade | [ActivityAmuletUpgradeData](#lq-ActivityAmuletUpgradeData) |  |  |
| illustrated_book | [ActivityAmuletIllustratedBookData](#lq-ActivityAmuletIllustratedBookData) |  |  |
| book_effect_id | [uint32](#uint32) |  |  |
| game_records | [ActivityAmuletGameRecordData](#lq-ActivityAmuletGameRecordData) | repeated |  |
| statistic | [ActivityAmuletStatisticData](#lq-ActivityAmuletStatisticData) |  |  |






<a name="lq-ActivityAmuletEffectRecordData"></a>

### ActivityAmuletEffectRecordData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| badge_id | [uint32](#uint32) |  |  |
| volume | [uint32](#uint32) |  |  |






<a name="lq-ActivityAmuletGameRecordData"></a>

### ActivityAmuletGameRecordData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_builds | [ActivityAmuletEffectRecordData](#lq-ActivityAmuletEffectRecordData) | repeated |  |
| level | [uint32](#uint32) |  |  |
| highest_level_score | [string](#string) |  |  |
| highest_fan | [string](#string) |  |  |
| highest_score | [string](#string) |  |  |
| coin_consumed | [string](#string) |  |  |
| pack_count | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| highest_hu | [ActivityAmuletHuRecord](#lq-ActivityAmuletHuRecord) |  |  |
| level_node | [uint32](#uint32) |  |  |






<a name="lq-ActivityAmuletHuRecord"></a>

### ActivityAmuletHuRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| point | [string](#string) |  |  |
| pai | [string](#string) |  |  |
| fan | [string](#string) |  |  |
| base | [string](#string) |  |  |
| effect_builds | [ActivityAmuletEffectRecordData](#lq-ActivityAmuletEffectRecordData) | repeated |  |






<a name="lq-ActivityAmuletHuRecordDirty"></a>

### ActivityAmuletHuRecordDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [ActivityAmuletHuRecord](#lq-ActivityAmuletHuRecord) |  |  |






<a name="lq-ActivityAmuletIllustratedBookData"></a>

### ActivityAmuletIllustratedBookData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_collection | [uint32](#uint32) | repeated |  |
| badge_collection | [uint32](#uint32) | repeated |  |
| rune_stone_collection | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityAmuletMapNodeDataArrayDirty"></a>

### ActivityAmuletMapNodeDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletMapNodeData](#lq-AmuletMapNodeData) | repeated |  |






<a name="lq-ActivityAmuletStatisticData"></a>

### ActivityAmuletStatisticData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| highest_level | [uint32](#uint32) |  |  |
| highest_hu | [ActivityAmuletHuRecord](#lq-ActivityAmuletHuRecord) |  |  |
| highest_level_score | [string](#string) |  |  |
| highest_fan | [string](#string) |  |  |
| highest_score | [string](#string) |  |  |
| pass_game_count | [uint32](#uint32) |  |  |
| round_count | [uint32](#uint32) |  |  |
| open_pack_count | [uint32](#uint32) |  |  |
| highest_coin_consumed | [string](#string) |  |  |
| character_statistic | [CharacterStatistic](#lq-CharacterStatistic) | repeated |  |
| highest_level_node | [uint32](#uint32) |  |  |






<a name="lq-ActivityAmuletTradeItemArrayDirty"></a>

### ActivityAmuletTradeItemArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletTradeItem](#lq-AmuletTradeItem) | repeated |  |






<a name="lq-ActivityAmuletTradeRewardDirty"></a>

### ActivityAmuletTradeRewardDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletTradeReward](#lq-AmuletTradeReward) |  |  |






<a name="lq-ActivityAmuletUpgradeData"></a>

### ActivityAmuletUpgradeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skill | [AmuletSkillData](#lq-AmuletSkillData) | repeated |  |






<a name="lq-AmuletActivityTingInfo"></a>

### AmuletActivityTingInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| fan | [string](#string) |  |  |
| ting_tile | [string](#string) |  |  |






<a name="lq-AmuletAdvancedShopGoods"></a>

### AmuletAdvancedShopGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| effect | [AmuletEffectCandidate](#lq-AmuletEffectCandidate) |  |  |
| rune_stone | [uint32](#uint32) |  |  |
| sold | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-AmuletAdvancedShopGoodsArrayDirty"></a>

### AmuletAdvancedShopGoodsArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletAdvancedShopGoods](#lq-AmuletAdvancedShopGoods) | repeated |  |






<a name="lq-AmuletAdvancedShopUpgrade"></a>

### AmuletAdvancedShopUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| upgrade_id | [uint32](#uint32) |  |  |
| sold | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-AmuletAdvancedShopUpgradeArrayDirty"></a>

### AmuletAdvancedShopUpgradeArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletAdvancedShopUpgrade](#lq-AmuletAdvancedShopUpgrade) | repeated |  |






<a name="lq-AmuletBadgeData"></a>

### AmuletBadgeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| uid | [uint32](#uint32) |  |  |
| store | [string](#string) | repeated |  |
| random | [uint32](#uint32) |  |  |






<a name="lq-AmuletBuffData"></a>

### AmuletBuffData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| store | [string](#string) | repeated |  |






<a name="lq-AmuletBuffDataArrayDirty"></a>

### AmuletBuffDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletBuffData](#lq-AmuletBuffData) | repeated |  |






<a name="lq-AmuletCharacterData"></a>

### AmuletCharacterData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| max_hp | [uint32](#uint32) |  |  |
| hp | [uint32](#uint32) |  |  |






<a name="lq-AmuletCharacterDataChanges"></a>

### AmuletCharacterDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| hp | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| max_hp | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-AmuletEffectCandidate"></a>

### AmuletEffectCandidate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| badge_id | [uint32](#uint32) |  |  |






<a name="lq-AmuletEffectCandidatesArrayDirty"></a>

### AmuletEffectCandidatesArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletEffectCandidate](#lq-AmuletEffectCandidate) | repeated |  |






<a name="lq-AmuletEffectCounterData"></a>

### AmuletEffectCounterData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_id | [uint32](#uint32) |  |  |
| pack_candidate_count | [uint32](#uint32) |  |  |
| gain_count | [uint32](#uint32) |  |  |






<a name="lq-AmuletEffectCounterDataArrayDirty"></a>

### AmuletEffectCounterDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletEffectCounterData](#lq-AmuletEffectCounterData) | repeated |  |






<a name="lq-AmuletEffectData"></a>

### AmuletEffectData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| uid | [uint32](#uint32) |  |  |
| store | [string](#string) | repeated |  |
| badge | [AmuletBadgeData](#lq-AmuletBadgeData) |  |  |
| volume | [uint32](#uint32) |  |  |
| tags | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletEffectDataArrayDirty"></a>

### AmuletEffectDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletEffectData](#lq-AmuletEffectData) | repeated |  |






<a name="lq-AmuletEffectDataChanges"></a>

### AmuletEffectDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_list | [AmuletEffectDataArrayDirty](#lq-AmuletEffectDataArrayDirty) |  |  |
| buff_list | [AmuletBuffDataArrayDirty](#lq-AmuletBuffDataArrayDirty) |  |  |
| skill_buff_list | [AmuletBuffDataArrayDirty](#lq-AmuletBuffDataArrayDirty) |  |  |
| shop_buff_list | [AmuletBuffDataArrayDirty](#lq-AmuletBuffDataArrayDirty) |  |  |
| rune_stone_list | [AmuletRuneStoneArrayDirty](#lq-AmuletRuneStoneArrayDirty) |  |  |
| current_level_reward_pack | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| pack_candidates | [AmuletEffectCandidatesArrayDirty](#lq-AmuletEffectCandidatesArrayDirty) |  |  |
| pack_queue | [AmuletPackQueueArrayDirty](#lq-AmuletPackQueueArrayDirty) |  |  |
| pack_goods_id | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-AmuletEffectedHookData"></a>

### AmuletEffectedHookData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| result | [AmuletHookResult](#lq-AmuletHookResult) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-AmuletEnemyData"></a>

### AmuletEnemyData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| max_hp | [string](#string) |  |  |
| hp | [string](#string) |  |  |
| atk | [uint32](#uint32) |  |  |






<a name="lq-AmuletEnemyDirty"></a>

### AmuletEnemyDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletEnemyData](#lq-AmuletEnemyData) |  |  |






<a name="lq-AmuletEventData"></a>

### AmuletEventData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| effected_hooks | [AmuletEffectedHookData](#lq-AmuletEffectedHookData) | repeated |  |
| value_changes | [AmuletValueChanges](#lq-AmuletValueChanges) |  |  |
| result | [AmuletEventResult](#lq-AmuletEventResult) |  |  |
| event_hooks | [AmuletEventHookData](#lq-AmuletEventHookData) | repeated |  |
| state | [AmuletStateData](#lq-AmuletStateData) |  |  |






<a name="lq-AmuletEventHookData"></a>

### AmuletEventHookData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| remove_effect | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletEventResult"></a>

### AmuletEventResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| deal_result | [AmuletEventResult.DealResult](#lq-AmuletEventResult-DealResult) |  |  |
| hu_result | [AmuletEventResult.HuResult](#lq-AmuletEventResult-HuResult) |  |  |
| game_end_result | [AmuletEventResult.GameEndResult](#lq-AmuletEventResult-GameEndResult) |  |  |
| gang_result | [AmuletEventResult.GangResult](#lq-AmuletEventResult-GangResult) |  |  |
| upgrade_result | [AmuletEventResult.UpgradeResult](#lq-AmuletEventResult-UpgradeResult) |  |  |
| new_game_result | [AmuletGameData](#lq-AmuletGameData) |  |  |
| sell_effect_result | [AmuletEventResult.SellEffectResult](#lq-AmuletEventResult-SellEffectResult) |  |  |
| select_pack_result | [AmuletEventResult.SelectPackResult](#lq-AmuletEventResult-SelectPackResult) |  |  |
| gamble_result | [AmuletEventResult.GambleResult](#lq-AmuletEventResult-GambleResult) |  |  |
| advanced_shop_upgrade_result | [AmuletEventResult.AdvancedShopUpgradeResult](#lq-AmuletEventResult-AdvancedShopUpgradeResult) |  |  |






<a name="lq-AmuletEventResult-AdvancedShopUpgradeResult"></a>

### AmuletEventResult.AdvancedShopUpgradeResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| modify_tile_score | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |






<a name="lq-AmuletEventResult-DealResult"></a>

### AmuletEventResult.DealResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [uint32](#uint32) |  |  |






<a name="lq-AmuletEventResult-GambleResult"></a>

### AmuletEventResult.GambleResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| destroyed | [uint32](#uint32) |  |  |
| result_selection | [uint32](#uint32) |  |  |
| modify_tile_score | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |






<a name="lq-AmuletEventResult-GameEndResult"></a>

### AmuletEventResult.GameEndResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reason | [uint32](#uint32) |  |  |






<a name="lq-AmuletEventResult-GangResult"></a>

### AmuletEventResult.GangResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new_dora | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletEventResult-HuResult"></a>

### AmuletEventResult.HuResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hu_final | [AmuletEventResult.HuResult.HuInfo](#lq-AmuletEventResult-HuResult-HuInfo) |  |  |
| hu_base | [AmuletEventResult.HuResult.HuInfo](#lq-AmuletEventResult-HuResult-HuInfo) |  |  |
| attack | [string](#string) |  |  |






<a name="lq-AmuletEventResult-HuResult-HuInfo"></a>

### AmuletEventResult.HuResult.HuInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [uint32](#uint32) |  |  |
| fan_list | [AmuletFan](#lq-AmuletFan) | repeated |  |
| fan | [string](#string) |  |  |
| base | [string](#string) |  |  |
| point | [string](#string) |  |  |






<a name="lq-AmuletEventResult-SelectPackResult"></a>

### AmuletEventResult.SelectPackResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| merge_type | [uint32](#uint32) |  |  |
| merged_list | [uint32](#uint32) | repeated |  |
| merged_result | [uint32](#uint32) |  |  |
| badge | [AmuletBadgeData](#lq-AmuletBadgeData) |  |  |






<a name="lq-AmuletEventResult-SellEffectResult"></a>

### AmuletEventResult.SellEffectResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| price | [string](#string) |  |  |






<a name="lq-AmuletEventResult-UpgradeResult"></a>

### AmuletEventResult.UpgradeResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level_coin | [string](#string) |  |  |






<a name="lq-AmuletFan"></a>

### AmuletFan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| val | [string](#string) |  |  |
| count | [uint32](#uint32) |  |  |
| yiman | [bool](#bool) |  |  |






<a name="lq-AmuletFanValue"></a>

### AmuletFanValue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| value | [string](#string) |  |  |






<a name="lq-AmuletFanValueArrayDirty"></a>

### AmuletFanValueArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletFanValue](#lq-AmuletFanValue) | repeated |  |






<a name="lq-AmuletGameData"></a>

### AmuletGameData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round | [AmuletGameRoundData](#lq-AmuletGameRoundData) |  |  |
| effect | [AmuletGameEffectData](#lq-AmuletGameEffectData) |  |  |
| game | [AmuletGameInfoData](#lq-AmuletGameInfoData) |  |  |
| shop | [AmuletShopData](#lq-AmuletShopData) |  |  |
| record | [AmuletGameRecordData](#lq-AmuletGameRecordData) |  |  |
| state | [AmuletStateData](#lq-AmuletStateData) |  |  |
| map | [AmuletMapData](#lq-AmuletMapData) |  |  |
| character | [AmuletCharacterData](#lq-AmuletCharacterData) |  |  |
| node_event | [AmuletNodeEventData](#lq-AmuletNodeEventData) |  |  |






<a name="lq-AmuletGameEffectData"></a>

### AmuletGameEffectData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_list | [AmuletEffectData](#lq-AmuletEffectData) | repeated |  |
| buff_list | [AmuletBuffData](#lq-AmuletBuffData) | repeated |  |
| skill_buff_list | [AmuletBuffData](#lq-AmuletBuffData) | repeated |  |
| shop_buff_list | [AmuletBuffData](#lq-AmuletBuffData) | repeated |  |
| rune_stone_list | [AmuletRuneStoneData](#lq-AmuletRuneStoneData) | repeated |  |
| max_effect_volume | [uint32](#uint32) |  |  |
| pack_candidates | [AmuletEffectCandidate](#lq-AmuletEffectCandidate) | repeated |  |
| pack_goods_id | [uint32](#uint32) |  |  |
| pack_queue | [AmuletPackQueue](#lq-AmuletPackQueue) | repeated |  |
| pack_disable_skip | [uint32](#uint32) |  |  |






<a name="lq-AmuletGameInfoData"></a>

### AmuletGameInfoData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| coin | [string](#string) |  |  |
| max_effect_volume | [uint32](#uint32) |  |  |
| tile_score_map | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |
| book_effect_id | [uint32](#uint32) |  |  |
| fan_value_map | [AmuletFanValue](#lq-AmuletFanValue) | repeated |  |
| init_change_hand_count | [uint32](#uint32) |  |  |






<a name="lq-AmuletGameInfoDataChanges"></a>

### AmuletGameInfoDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| coin | [StringDirty](#lq-StringDirty) |  |  |
| max_effect_volume | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| tile_score_map | [AmuletTileScoreArrayDirty](#lq-AmuletTileScoreArrayDirty) |  |  |
| fan_value_map | [AmuletFanValueArrayDirty](#lq-AmuletFanValueArrayDirty) |  |  |






<a name="lq-AmuletGameOperation"></a>

### AmuletGameOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| gang | [AmuletGameOperation.GangTiles](#lq-AmuletGameOperation-GangTiles) | repeated |  |
| value | [int32](#int32) |  |  |






<a name="lq-AmuletGameOperation-GangTiles"></a>

### AmuletGameOperation.GangTiles



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tiles | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletGameOperationArrayDirty"></a>

### AmuletGameOperationArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletGameOperation](#lq-AmuletGameOperation) | repeated |  |






<a name="lq-AmuletGameRecordData"></a>

### AmuletGameRecordData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| yiman_count | [uint32](#uint32) |  |  |
| level_hu_count | [uint32](#uint32) |  |  |
| game_hu_count | [uint32](#uint32) |  |  |
| effect_gain | [uint32](#uint32) |  |  |
| coin_consume | [string](#string) |  |  |
| coin_gain | [string](#string) |  |  |
| highest_hu | [ActivityAmuletHuRecord](#lq-ActivityAmuletHuRecord) |  |  |
| highest_level_score | [string](#string) |  |  |
| highest_fan | [string](#string) |  |  |
| pack_count | [uint32](#uint32) |  |  |
| round_count | [uint32](#uint32) |  |  |
| effect_counter | [AmuletEffectCounterData](#lq-AmuletEffectCounterData) | repeated |  |
| hu_tiles_id | [uint32](#uint32) | repeated |  |
| effect_upgrade_count | [uint32](#uint32) |  |  |






<a name="lq-AmuletGameRoundData"></a>

### AmuletGameRoundData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pool | [AmuletTile](#lq-AmuletTile) | repeated |  |
| tile_replace | [AmuletTile](#lq-AmuletTile) | repeated |  |
| tian_dora | [string](#string) | repeated |  |
| dora | [uint32](#uint32) | repeated |  |
| hands | [uint32](#uint32) | repeated |  |
| used_desktop | [uint32](#uint32) | repeated |  |
| ming | [AmuletMingInfo](#lq-AmuletMingInfo) | repeated |  |
| locked_tile | [uint32](#uint32) | repeated |  |
| change_tile_count | [uint32](#uint32) |  |  |
| total_change_tile_count | [uint32](#uint32) |  |  |
| next_operation | [AmuletGameOperation](#lq-AmuletGameOperation) | repeated |  |
| ting_list | [AmuletActivityTingInfo](#lq-AmuletActivityTingInfo) | repeated |  |
| locked_tile_count | [uint32](#uint32) |  |  |
| enemy | [AmuletEnemyData](#lq-AmuletEnemyData) |  |  |
| mountain | [uint32](#uint32) | repeated |  |
| used | [uint32](#uint32) | repeated |  |
| desktop | [uint32](#uint32) | repeated |  |
| show_desktop | [uint32](#uint32) | repeated |  |
| after_gang | [uint32](#uint32) |  |  |
| berserk_tile | [uint32](#uint32) | repeated |  |
| delay_round | [uint32](#uint32) |  |  |
| desktop_remain | [uint32](#uint32) |  |  |
| show_desktop_tiles | [AmuletShowDesktopTileData](#lq-AmuletShowDesktopTileData) | repeated |  |
| berserk_tile_pos | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletGameShopGoods"></a>

### AmuletGameShopGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| sold | [bool](#bool) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult"></a>

### AmuletHookResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| add_effect | [AmuletHookResult.AddEffectResult](#lq-AmuletHookResult-AddEffectResult) | repeated |  |
| remove_effect | [uint32](#uint32) | repeated |  |
| add_buff | [uint32](#uint32) | repeated |  |
| remove_buff | [uint32](#uint32) | repeated |  |
| add_tian_dora | [string](#string) | repeated |  |
| add_dora | [AmuletHookResult.AddDoraResult](#lq-AmuletHookResult-AddDoraResult) |  |  |
| coin_modify | [AmuletHookResult.BigIntValueResult](#lq-AmuletHookResult-BigIntValueResult) |  |  |
| tile_replace | [AmuletTile](#lq-AmuletTile) | repeated |  |
| add_show_tile | [uint32](#uint32) | repeated |  |
| modify_tile_score | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |
| calc_desktop_count | [int32](#int32) |  |  |
| modify_desktop_count | [int32](#int32) |  |  |
| modify_show_desktop_count | [int32](#int32) |  |  |
| modify_lock_tile_count | [int32](#int32) |  |  |
| modify_change_hands_count | [int32](#int32) |  |  |
| modify_change_hands_tile_count | [int32](#int32) |  |  |
| force_moqie | [bool](#bool) |  |  |
| replace_hu | [bool](#bool) |  |  |
| modify_target_point | [string](#string) |  |  |
| upgrade_level | [bool](#bool) |  |  |
| modify_dora | [AmuletHookResult.ModifyDoraResult](#lq-AmuletHookResult-ModifyDoraResult) | repeated |  |
| modify_dora_max_count | [int32](#int32) |  |  |
| modify_shop_goods_count | [int32](#int32) |  |  |
| modify_shop_rare_weight | [bool](#bool) |  |  |
| modify_shop_goods_price | [bool](#bool) |  |  |
| modify_shop_pack_effect | [uint32](#uint32) | repeated |  |
| modify_effect_max_count | [int32](#int32) |  |  |
| modify_goods | [AmuletGameShopGoods](#lq-AmuletGameShopGoods) | repeated |  |
| remove_goods | [uint32](#uint32) | repeated |  |
| modify_base | [AmuletHookResult.BigIntValueResult](#lq-AmuletHookResult-BigIntValueResult) |  |  |
| modify_fan | [AmuletHookResult.BigIntValueResult](#lq-AmuletHookResult-BigIntValueResult) |  |  |
| modify_fan_info | [AmuletFan](#lq-AmuletFan) | repeated |  |
| transform_effect | [AmuletHookResult.TransformResult](#lq-AmuletHookResult-TransformResult) | repeated |  |
| add_badge | [AmuletHookResult.AddBadge](#lq-AmuletHookResult-AddBadge) | repeated |  |
| remove_badge | [uint32](#uint32) | repeated |  |
| modify_effect_price | [string](#string) |  |  |
| copy_effect | [AmuletHookResult.CopyEffect](#lq-AmuletHookResult-CopyEffect) | repeated |  |
| effect_growth | [bool](#bool) |  |  |
| modify_tile_score_aura | [string](#string) |  |  |
| modify_hule_count | [uint32](#uint32) |  |  |
| can_gang | [bool](#bool) |  |  |
| modify_change_hands_list | [uint32](#uint32) | repeated |  |
| modify_change_desktop | [AmuletHookResult.AmuletChangeDesktopResult](#lq-AmuletHookResult-AmuletChangeDesktopResult) |  |  |
| self_effect_id | [uint32](#uint32) |  |  |
| modify_change_coin | [string](#string) |  |  |
| set_tile_score | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |
| upgrade_effect | [AmuletHookResult.UpgradeEffectResult](#lq-AmuletHookResult-UpgradeEffectResult) | repeated |  |
| modify_tile_base_score | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |
| heal | [AmuletHookResult.UInt32ValueResult](#lq-AmuletHookResult-UInt32ValueResult) |  |  |
| damage | [AmuletHookResult.UInt32ValueResult](#lq-AmuletHookResult-UInt32ValueResult) |  |  |
| modify_berserk_tile_count | [uint32](#uint32) |  |  |
| modify_enemy_max_hp | [AmuletHookResult.BigIntValueResult](#lq-AmuletHookResult-BigIntValueResult) |  |  |
| add_fan_value | [AmuletFanValue](#lq-AmuletFanValue) | repeated |  |
| set_change_tile_count | [uint32](#uint32) |  |  |
| modify_shop_upgrade_goods_price | [bool](#bool) |  |  |






<a name="lq-AmuletHookResult-AddBadge"></a>

### AmuletHookResult.AddBadge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| badge_id | [uint32](#uint32) |  |  |
| badge_uid | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult-AddDoraResult"></a>

### AmuletHookResult.AddDoraResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| list | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletHookResult-AddEffectResult"></a>

### AmuletHookResult.AddEffectResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| merge_type | [uint32](#uint32) |  |  |
| merged_list | [uint32](#uint32) | repeated |  |
| merged_result | [uint32](#uint32) |  |  |
| badge | [AmuletBadgeData](#lq-AmuletBadgeData) |  |  |
| store | [string](#string) | repeated |  |
| volume | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult-AmuletChangeDesktopResult"></a>

### AmuletHookResult.AmuletChangeDesktopResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| show_desktop_tiles | [AmuletShowDesktopTileData](#lq-AmuletShowDesktopTileData) | repeated |  |
| desktop | [uint32](#uint32) | repeated |  |
| locked_tile_count | [uint32](#uint32) |  |  |
| desktop_remain | [uint32](#uint32) |  |  |
| locked_tile | [uint32](#uint32) | repeated |  |
| berserk_tile_pos | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletHookResult-BigIntValueResult"></a>

### AmuletHookResult.BigIntValueResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [string](#string) |  |  |
| modify | [string](#string) |  |  |
| final | [string](#string) |  |  |






<a name="lq-AmuletHookResult-CopyEffect"></a>

### AmuletHookResult.CopyEffect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| from_uid | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult-ModifyDoraResult"></a>

### AmuletHookResult.ModifyDoraResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| is_dora | [bool](#bool) |  |  |
| is_red_dora | [bool](#bool) |  |  |
| is_tian_dora | [bool](#bool) |  |  |
| dora_count | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult-TransformResult"></a>

### AmuletHookResult.TransformResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| effect_id | [uint32](#uint32) |  |  |
| add_result | [AmuletHookResult.AddEffectResult](#lq-AmuletHookResult-AddEffectResult) |  |  |






<a name="lq-AmuletHookResult-UInt32ValueResult"></a>

### AmuletHookResult.UInt32ValueResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [uint32](#uint32) |  |  |
| modify | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |






<a name="lq-AmuletHookResult-UpgradeEffectResult"></a>

### AmuletHookResult.UpgradeEffectResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uid | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| badge | [AmuletBadgeData](#lq-AmuletBadgeData) |  |  |
| store | [string](#string) | repeated |  |
| volume | [uint32](#uint32) |  |  |






<a name="lq-AmuletMapData"></a>

### AmuletMapData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| node | [uint32](#uint32) |  |  |
| map_nodes | [AmuletMapNodeData](#lq-AmuletMapNodeData) | repeated |  |
| transport_count | [uint32](#uint32) |  |  |






<a name="lq-AmuletMapDataChanges"></a>

### AmuletMapDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| node | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| map_nodes | [ActivityAmuletMapNodeDataArrayDirty](#lq-ActivityAmuletMapNodeDataArrayDirty) |  |  |
| transport_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-AmuletMapNodeData"></a>

### AmuletMapNodeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| sub_type | [uint32](#uint32) |  |  |
| args | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletMingInfo"></a>

### AmuletMingInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| tile_list | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletMingInfoArrayDirty"></a>

### AmuletMingInfoArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletMingInfo](#lq-AmuletMingInfo) | repeated |  |






<a name="lq-AmuletNodeEventChanges"></a>

### AmuletNodeEventChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| advanced_shop_goods | [AmuletAdvancedShopGoodsArrayDirty](#lq-AmuletAdvancedShopGoodsArrayDirty) |  |  |
| advanced_shop_refresh_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| advanced_shop_refresh_price | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| bonfire_selection | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| gamble_id | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| gamble_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| gamble_price | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| gamble_selections | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| trade_items | [ActivityAmuletTradeItemArrayDirty](#lq-ActivityAmuletTradeItemArrayDirty) |  |  |
| trade_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| trade_reward | [ActivityAmuletTradeRewardDirty](#lq-ActivityAmuletTradeRewardDirty) |  |  |
| advanced_shop_upgrade | [AmuletAdvancedShopUpgradeArrayDirty](#lq-AmuletAdvancedShopUpgradeArrayDirty) |  |  |






<a name="lq-AmuletNodeEventData"></a>

### AmuletNodeEventData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| advanced_shop_goods | [AmuletAdvancedShopGoods](#lq-AmuletAdvancedShopGoods) | repeated |  |
| advanced_shop_refresh_count | [uint32](#uint32) |  |  |
| bonfire_selection | [uint32](#uint32) | repeated |  |
| gamble_id | [uint32](#uint32) |  |  |
| gamble_count | [uint32](#uint32) |  |  |
| gamble_price | [uint32](#uint32) |  |  |
| gamble_selections | [uint32](#uint32) | repeated |  |
| trade_items | [AmuletTradeItem](#lq-AmuletTradeItem) | repeated |  |
| trade_count | [uint32](#uint32) |  |  |
| trade_reward | [AmuletTradeReward](#lq-AmuletTradeReward) |  |  |
| advanced_shop_upgrade | [AmuletAdvancedShopUpgrade](#lq-AmuletAdvancedShopUpgrade) | repeated |  |
| advanced_shop_refresh_price | [uint32](#uint32) |  |  |






<a name="lq-AmuletPackQueue"></a>

### AmuletPackQueue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pack_id | [uint32](#uint32) |  |  |
| sure_candidate | [uint32](#uint32) | repeated |  |
| count | [uint32](#uint32) |  |  |
| disable_skip | [uint32](#uint32) |  |  |
| source | [uint32](#uint32) |  |  |






<a name="lq-AmuletPackQueueArrayDirty"></a>

### AmuletPackQueueArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletPackQueue](#lq-AmuletPackQueue) | repeated |  |






<a name="lq-AmuletRecordDataChanges"></a>

### AmuletRecordDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| yiman_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| level_hu_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| game_hu_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| effect_gain | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| coin_consume | [StringDirty](#lq-StringDirty) |  |  |
| coin_gain | [StringDirty](#lq-StringDirty) |  |  |
| highest_hu | [ActivityAmuletHuRecordDirty](#lq-ActivityAmuletHuRecordDirty) |  |  |
| highest_level_score | [StringDirty](#lq-StringDirty) |  |  |
| highest_fan | [StringDirty](#lq-StringDirty) |  |  |
| pack_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| round_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| effect_counter | [AmuletEffectCounterDataArrayDirty](#lq-AmuletEffectCounterDataArrayDirty) |  |  |
| hu_tiles_id | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| effect_upgrade_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-AmuletRoundDataChanges"></a>

### AmuletRoundDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pool | [AmuletTileArrayDirty](#lq-AmuletTileArrayDirty) |  |  |
| tile_replace | [AmuletTileArrayDirty](#lq-AmuletTileArrayDirty) |  |  |
| tian_dora | [StringArrayDirty](#lq-StringArrayDirty) |  |  |
| dora | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| hands | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| used_desktop | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| used | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| ming | [AmuletMingInfoArrayDirty](#lq-AmuletMingInfoArrayDirty) |  |  |
| locked_tile | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| change_tile_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| total_change_tile_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| next_operation | [AmuletGameOperationArrayDirty](#lq-AmuletGameOperationArrayDirty) |  |  |
| ting_list | [AmuletTingInfoArrayDirty](#lq-AmuletTingInfoArrayDirty) |  |  |
| desktop_remain | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| show_desktop_tiles | [AmuletShowDesktopTileDataArrayDirty](#lq-AmuletShowDesktopTileDataArrayDirty) |  |  |
| locked_tile_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| berserk_tile_pos | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| enemy | [AmuletEnemyDirty](#lq-AmuletEnemyDirty) |  |  |
| delay_round | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-AmuletRuneStoneArrayDirty"></a>

### AmuletRuneStoneArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletRuneStoneData](#lq-AmuletRuneStoneData) | repeated |  |






<a name="lq-AmuletRuneStoneData"></a>

### AmuletRuneStoneData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| store | [string](#string) | repeated |  |






<a name="lq-AmuletShopData"></a>

### AmuletShopData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods | [AmuletGameShopGoods](#lq-AmuletGameShopGoods) | repeated |  |
| shop_refresh_count | [uint32](#uint32) |  |  |
| refresh_price | [uint32](#uint32) |  |  |
| upgrade_goods | [AmuletShopUpgradeGoods](#lq-AmuletShopUpgradeGoods) | repeated |  |






<a name="lq-AmuletShopDataChanges"></a>

### AmuletShopDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods | [AmuletShopGoodsArrayDirty](#lq-AmuletShopGoodsArrayDirty) |  |  |
| shop_refresh_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| refresh_price | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| upgrade_goods | [AmuletShopUpgradeGoodsArrayDirty](#lq-AmuletShopUpgradeGoodsArrayDirty) |  |  |






<a name="lq-AmuletShopGoodsArrayDirty"></a>

### AmuletShopGoodsArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletGameShopGoods](#lq-AmuletGameShopGoods) | repeated |  |






<a name="lq-AmuletShopUpgradeGoods"></a>

### AmuletShopUpgradeGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| upgrade_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-AmuletShopUpgradeGoodsArrayDirty"></a>

### AmuletShopUpgradeGoodsArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletShopUpgradeGoods](#lq-AmuletShopUpgradeGoods) | repeated |  |






<a name="lq-AmuletShowDesktopTileData"></a>

### AmuletShowDesktopTileData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-AmuletShowDesktopTileDataArrayDirty"></a>

### AmuletShowDesktopTileDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletShowDesktopTileData](#lq-AmuletShowDesktopTileData) | repeated |  |






<a name="lq-AmuletSkillData"></a>

### AmuletSkillData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-AmuletStateData"></a>

### AmuletStateData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| current | [uint32](#uint32) |  |  |
| interrupt | [uint32](#uint32) |  |  |






<a name="lq-AmuletTile"></a>

### AmuletTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |






<a name="lq-AmuletTileArrayDirty"></a>

### AmuletTileArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletTile](#lq-AmuletTile) | repeated |  |






<a name="lq-AmuletTileScore"></a>

### AmuletTileScore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| score | [string](#string) |  |  |






<a name="lq-AmuletTileScoreArrayDirty"></a>

### AmuletTileScoreArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletTileScore](#lq-AmuletTileScore) | repeated |  |






<a name="lq-AmuletTingInfoArrayDirty"></a>

### AmuletTingInfoArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [AmuletActivityTingInfo](#lq-AmuletActivityTingInfo) | repeated |  |






<a name="lq-AmuletTradeItem"></a>

### AmuletTradeItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| store | [uint32](#uint32) | repeated |  |






<a name="lq-AmuletTradeReward"></a>

### AmuletTradeReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| rune_stone_id | [uint32](#uint32) |  |  |
| effect_id | [uint32](#uint32) |  |  |
| badge_id | [uint32](#uint32) |  |  |






<a name="lq-AmuletValueChanges"></a>

### AmuletValueChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round | [AmuletRoundDataChanges](#lq-AmuletRoundDataChanges) |  |  |
| effect | [AmuletEffectDataChanges](#lq-AmuletEffectDataChanges) |  |  |
| game | [AmuletGameInfoDataChanges](#lq-AmuletGameInfoDataChanges) |  |  |
| shop | [AmuletShopDataChanges](#lq-AmuletShopDataChanges) |  |  |
| record | [AmuletRecordDataChanges](#lq-AmuletRecordDataChanges) |  |  |
| state | [AmuletStateData](#lq-AmuletStateData) |  |  |
| map | [AmuletMapDataChanges](#lq-AmuletMapDataChanges) |  |  |
| character | [AmuletCharacterDataChanges](#lq-AmuletCharacterDataChanges) |  |  |
| node_event | [AmuletNodeEventChanges](#lq-AmuletNodeEventChanges) |  |  |






<a name="lq-CharacterStatistic"></a>

### CharacterStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| highest_level | [uint32](#uint32) |  |  |
| highest_score | [string](#string) |  |  |
| highest_level_node | [uint32](#uint32) |  |  |















<a name="cli_game-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## cli_game.proto



<a name="lq-GameRestore"></a>

### GameRestore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| snapshot | [GameSnapshot](#lq-GameSnapshot) |  |  |
| actions | [ActionPrototype](#lq-ActionPrototype) | repeated |  |
| passed_waiting_time | [uint32](#uint32) |  |  |
| game_state | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| last_pause_time_ms | [uint32](#uint32) |  |  |






<a name="lq-NotifyAccountLevelChange"></a>

### NotifyAccountLevelChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [AccountLevel](#lq-AccountLevel) |  |  |
| final | [AccountLevel](#lq-AccountLevel) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-NotifyActivityPoint"></a>

### NotifyActivityPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_points | [NotifyActivityPoint.ActivityPoint](#lq-NotifyActivityPoint-ActivityPoint) | repeated |  |






<a name="lq-NotifyActivityPoint-ActivityPoint"></a>

### NotifyActivityPoint.ActivityPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-NotifyActivityReward"></a>

### NotifyActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_reward | [NotifyActivityReward.ActivityReward](#lq-NotifyActivityReward-ActivityReward) | repeated |  |






<a name="lq-NotifyActivityReward-ActivityReward"></a>

### NotifyActivityReward.ActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-NotifyEndGameVote"></a>

### NotifyEndGameVote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| results | [NotifyEndGameVote.VoteResult](#lq-NotifyEndGameVote-VoteResult) | repeated |  |
| start_time | [uint32](#uint32) |  |  |
| duration_time | [uint32](#uint32) |  |  |






<a name="lq-NotifyEndGameVote-VoteResult"></a>

### NotifyEndGameVote.VoteResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| yes | [bool](#bool) |  |  |






<a name="lq-NotifyGameBroadcast"></a>

### NotifyGameBroadcast



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| content | [string](#string) |  |  |






<a name="lq-NotifyGameEndResult"></a>

### NotifyGameEndResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| result | [GameEndResult](#lq-GameEndResult) |  |  |






<a name="lq-NotifyGameFinishReward"></a>

### NotifyGameFinishReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode_id | [uint32](#uint32) |  |  |
| level_change | [NotifyGameFinishReward.LevelChange](#lq-NotifyGameFinishReward-LevelChange) |  |  |
| match_chest | [NotifyGameFinishReward.MatchChest](#lq-NotifyGameFinishReward-MatchChest) |  |  |
| main_character | [NotifyGameFinishReward.MainCharacter](#lq-NotifyGameFinishReward-MainCharacter) |  |  |
| character_gift | [NotifyGameFinishReward.CharacterGift](#lq-NotifyGameFinishReward-CharacterGift) |  |  |
| badges | [BadgeAchieveProgress](#lq-BadgeAchieveProgress) | repeated |  |






<a name="lq-NotifyGameFinishReward-CharacterGift"></a>

### NotifyGameFinishReward.CharacterGift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |
| add | [uint32](#uint32) |  |  |
| is_graded | [bool](#bool) |  |  |






<a name="lq-NotifyGameFinishReward-LevelChange"></a>

### NotifyGameFinishReward.LevelChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [AccountLevel](#lq-AccountLevel) |  |  |
| final | [AccountLevel](#lq-AccountLevel) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-NotifyGameFinishReward-MainCharacter"></a>

### NotifyGameFinishReward.MainCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| add | [uint32](#uint32) |  |  |






<a name="lq-NotifyGameFinishReward-MatchChest"></a>

### NotifyGameFinishReward.MatchChest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| origin | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |
| is_graded | [bool](#bool) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-NotifyGamePause"></a>

### NotifyGamePause



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| paused | [bool](#bool) |  |  |






<a name="lq-NotifyGameTerminate"></a>

### NotifyGameTerminate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reason | [string](#string) |  |  |






<a name="lq-NotifyLeaderboardPoint"></a>

### NotifyLeaderboardPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_points | [NotifyLeaderboardPoint.LeaderboardPoint](#lq-NotifyLeaderboardPoint-LeaderboardPoint) | repeated |  |






<a name="lq-NotifyLeaderboardPoint-LeaderboardPoint"></a>

### NotifyLeaderboardPoint.LeaderboardPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-NotifyNewGame"></a>

### NotifyNewGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |
| player_list | [string](#string) | repeated |  |






<a name="lq-NotifyObserveData"></a>

### NotifyObserveData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unit | [GameLiveUnit](#lq-GameLiveUnit) |  |  |






<a name="lq-NotifyPlayerConnectionState"></a>

### NotifyPlayerConnectionState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| state | [GamePlayerState](#lq-GamePlayerState) |  |  |






<a name="lq-NotifyPlayerLoadGameReady"></a>

### NotifyPlayerLoadGameReady



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ready_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqAuthGame"></a>

### ReqAuthGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| token | [string](#string) |  |  |
| game_uuid | [string](#string) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |






<a name="lq-ReqAuthObserve"></a>

### ReqAuthObserve



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| token | [string](#string) |  |  |






<a name="lq-ReqBroadcastInGame"></a>

### ReqBroadcastInGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [string](#string) |  |  |
| except_self | [bool](#bool) |  |  |






<a name="lq-ReqChiPengGang"></a>

### ReqChiPengGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| index | [uint32](#uint32) |  |  |
| cancel_operation | [bool](#bool) |  |  |
| timeuse | [uint32](#uint32) |  |  |






<a name="lq-ReqGMCommandInGaming"></a>

### ReqGMCommandInGaming



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| json_data | [string](#string) |  |  |






<a name="lq-ReqSelfOperation"></a>

### ReqSelfOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| index | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| cancel_operation | [bool](#bool) |  |  |
| moqie | [bool](#bool) |  |  |
| timeuse | [uint32](#uint32) |  |  |
| tile_state | [int32](#int32) |  |  |
| change_tiles | [string](#string) | repeated |  |
| tile_states | [int32](#int32) | repeated |  |
| gap_type | [uint32](#uint32) |  |  |
| auto_operation | [bool](#bool) |  |  |






<a name="lq-ReqSyncGame"></a>

### ReqSyncGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round_id | [string](#string) |  |  |
| step | [uint32](#uint32) |  |  |






<a name="lq-ReqVoteGameEnd"></a>

### ReqVoteGameEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| yes | [bool](#bool) |  |  |






<a name="lq-ResAuthGame"></a>

### ResAuthGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| players | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| seat_list | [uint32](#uint32) | repeated |  |
| is_game_start | [bool](#bool) |  |  |
| game_config | [GameConfig](#lq-GameConfig) |  |  |
| ready_id_list | [uint32](#uint32) | repeated |  |
| robots | [PlayerGameView](#lq-PlayerGameView) | repeated |  |






<a name="lq-ResEnterGame"></a>

### ResEnterGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| is_end | [bool](#bool) |  |  |
| step | [uint32](#uint32) |  |  |
| game_restore | [GameRestore](#lq-GameRestore) |  |  |






<a name="lq-ResGameEndVote"></a>

### ResGameEndVote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [bool](#bool) |  |  |
| vote_cd_end_time | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResGamePlayerState"></a>

### ResGamePlayerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| state_list | [GamePlayerState](#lq-GamePlayerState) | repeated |  |






<a name="lq-ResStartObserve"></a>

### ResStartObserve



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| head | [GameLiveHead](#lq-GameLiveHead) |  |  |
| passed | [GameLiveSegment](#lq-GameLiveSegment) |  |  |






<a name="lq-ResSyncGame"></a>

### ResSyncGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| is_end | [bool](#bool) |  |  |
| step | [uint32](#uint32) |  |  |
| game_restore | [GameRestore](#lq-GameRestore) |  |  |















<a name="cli_lobby-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## cli_lobby.proto



<a name="lq-ContestSetting"></a>

### ContestSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level_limit | [ContestSetting.LevelLimit](#lq-ContestSetting-LevelLimit) | repeated |  |
| game_limit | [uint32](#uint32) |  |  |
| system_broadcast | [uint32](#uint32) |  |  |






<a name="lq-ContestSetting-LevelLimit"></a>

### ContestSetting.LevelLimit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |
| operate | [uint32](#uint32) |  |  |






<a name="lq-ReqAccountInfo"></a>

### ReqAccountInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAccountList"></a>

### ReqAccountList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqAccountStatisticInfo"></a>

### ReqAccountStatisticInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAddCollectedGameRecord"></a>

### ReqAddCollectedGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| remarks | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |






<a name="lq-ReqAddRoomRobot"></a>

### ReqAddRoomRobot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityBuy"></a>

### ReqAmuletActivityBuy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityEffectSort"></a>

### ReqAmuletActivityEffectSort



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| sorted_id | [uint32](#uint32) | repeated |  |






<a name="lq-ReqAmuletActivityEndShopping"></a>

### ReqAmuletActivityEndShopping



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityFetchBrief"></a>

### ReqAmuletActivityFetchBrief



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityFetchInfo"></a>

### ReqAmuletActivityFetchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityGameOperate"></a>

### ReqAmuletActivityGameOperate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| tile_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqAmuletActivityGiveup"></a>

### ReqAmuletActivityGiveup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityOperate"></a>

### ReqAmuletActivityOperate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| args | [uint32](#uint32) | repeated |  |






<a name="lq-ReqAmuletActivityRefreshShop"></a>

### ReqAmuletActivityRefreshShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySelectBookEffect"></a>

### ReqAmuletActivitySelectBookEffect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| effect_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySelectFreeEffect"></a>

### ReqAmuletActivitySelectFreeEffect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| selected_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySelectPack"></a>

### ReqAmuletActivitySelectPack



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySelectRewardPack"></a>

### ReqAmuletActivitySelectRewardPack



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySellEffect"></a>

### ReqAmuletActivitySellEffect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivitySetSkillLevel"></a>

### ReqAmuletActivitySetSkillLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| skill | [AmuletSkillData](#lq-AmuletSkillData) | repeated |  |






<a name="lq-ReqAmuletActivityStartGame"></a>

### ReqAmuletActivityStartGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityUpgrade"></a>

### ReqAmuletActivityUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqAmuletActivityUpgradeShopBuff"></a>

### ReqAmuletActivityUpgradeShopBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqApplyFriend"></a>

### ReqApplyFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |






<a name="lq-ReqArenaReward"></a>

### ReqArenaReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqBindAccount"></a>

### ReqBindAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account | [string](#string) |  |  |
| password | [string](#string) |  |  |






<a name="lq-ReqBindEmail"></a>

### ReqBindEmail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| email | [string](#string) |  |  |
| code | [string](#string) |  |  |
| password | [string](#string) |  |  |






<a name="lq-ReqBindOauth2"></a>

### ReqBindOauth2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| token | [string](#string) |  |  |






<a name="lq-ReqBindPhoneNumber"></a>

### ReqBindPhoneNumber



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [string](#string) |  |  |
| phone | [string](#string) |  |  |
| password | [string](#string) |  |  |
| multi_bind_version | [bool](#bool) |  |  |






<a name="lq-ReqBingoActivityReceiveReward"></a>

### ReqBingoActivityReceiveReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rewards | [ReqBingoActivityReceiveReward.BingoReward](#lq-ReqBingoActivityReceiveReward-BingoReward) | repeated |  |






<a name="lq-ReqBingoActivityReceiveReward-BingoReward"></a>

### ReqBingoActivityReceiveReward.BingoReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reward_id | [uint32](#uint32) |  |  |
| card_id | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyArenaTicket"></a>

### ReqBuyArenaTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyFestivalProposal"></a>

### ReqBuyFestivalProposal



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyFromChestShop"></a>

### ReqBuyFromChestShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyFromShop"></a>

### ReqBuyFromShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| ver_price | [ReqBuyFromShop.Item](#lq-ReqBuyFromShop-Item) | repeated |  |
| ver_goods | [ReqBuyFromShop.Item](#lq-ReqBuyFromShop-Item) | repeated |  |
| package_goods | [ReqBuyFromShop.Item](#lq-ReqBuyFromShop-Item) | repeated |  |






<a name="lq-ReqBuyFromShop-Item"></a>

### ReqBuyFromShop.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyFromZHP"></a>

### ReqBuyFromZHP



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyInABMatch"></a>

### ReqBuyInABMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_id | [uint32](#uint32) |  |  |






<a name="lq-ReqBuyShiLian"></a>

### ReqBuyShiLian



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqCancelGooglePlayOrder"></a>

### ReqCancelGooglePlayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |






<a name="lq-ReqCancelMatchQueue"></a>

### ReqCancelMatchQueue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_mode | [uint32](#uint32) |  |  |






<a name="lq-ReqCancelUnifiedMatch"></a>

### ReqCancelUnifiedMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_sid | [string](#string) |  |  |






<a name="lq-ReqChallangeLeaderboard"></a>

### ReqChallangeLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season | [uint32](#uint32) |  |  |






<a name="lq-ReqChangeAvatar"></a>

### ReqChangeAvatar



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| avatar_id | [uint32](#uint32) |  |  |






<a name="lq-ReqChangeCharacterSkin"></a>

### ReqChangeCharacterSkin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| skin | [uint32](#uint32) |  |  |






<a name="lq-ReqChangeCharacterView"></a>

### ReqChangeCharacterView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| slot | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |






<a name="lq-ReqChangeCollectedGameRecordRemarks"></a>

### ReqChangeCollectedGameRecordRemarks



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| remarks | [string](#string) |  |  |






<a name="lq-ReqChangeCommonView"></a>

### ReqChangeCommonView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| slot | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-ReqChangeMainCharacter"></a>

### ReqChangeMainCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |






<a name="lq-ReqCheckPrivacy"></a>

### ReqCheckPrivacy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_type | [string](#string) |  |  |
| versions | [ReqCheckPrivacy.Versions](#lq-ReqCheckPrivacy-Versions) | repeated |  |






<a name="lq-ReqCheckPrivacy-Versions"></a>

### ReqCheckPrivacy.Versions



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqClientMessage"></a>

### ReqClientMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [uint32](#uint32) |  |  |
| message | [string](#string) |  |  |






<a name="lq-ReqCombiningRecycleCraft"></a>

### ReqCombiningRecycleCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-ReqCommonViews"></a>

### ReqCommonViews



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint32](#uint32) |  |  |






<a name="lq-ReqCompleteActivityFlipTaskBatch"></a>

### ReqCompleteActivityFlipTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqCompleteActivityTask"></a>

### ReqCompleteActivityTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |






<a name="lq-ReqCompleteActivityTaskBatch"></a>

### ReqCompleteActivityTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqCompletePeriodActivityTaskBatch"></a>

### ReqCompletePeriodActivityTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqCompleteSegmentTaskReward"></a>

### ReqCompleteSegmentTaskReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqCompleteVillageTask"></a>

### ReqCompleteVillageTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqComposeShard"></a>

### ReqComposeShard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |






<a name="lq-ReqCreateAlipayAppOrder"></a>

### ReqCreateAlipayAppOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateAlipayOrder"></a>

### ReqCreateAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| alipay_trade_type | [string](#string) |  |  |
| return_url | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateAlipayScanOrder"></a>

### ReqCreateAlipayScanOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateBillingOrder"></a>

### ReqCreateBillingOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| payment_platform | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateCustomizedContest"></a>

### ReqCreateCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| open_show | [uint32](#uint32) |  |  |
| game_rule_setting | [GameMode](#lq-GameMode) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| auto_match | [uint32](#uint32) |  |  |
| rank_rule | [uint32](#uint32) |  |  |
| contest_setting | [ContestSetting](#lq-ContestSetting) |  |  |
| rank_type | [uint32](#uint32) |  |  |






<a name="lq-ReqCreateDMMOrder"></a>

### ReqCreateDMMOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateENAlipayOrder"></a>

### ReqCreateENAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateENJCBOrder"></a>

### ReqCreateENJCBOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateENMasterCardOrder"></a>

### ReqCreateENMasterCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateENPaypalOrder"></a>

### ReqCreateENPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateENVisaOrder"></a>

### ReqCreateENVisaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateEmailVerifyCode"></a>

### ReqCreateEmailVerifyCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| email | [string](#string) |  |  |
| usage | [uint32](#uint32) |  |  |






<a name="lq-ReqCreateGameObserveAuth"></a>

### ReqCreateGameObserveAuth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |






<a name="lq-ReqCreateGamePlan"></a>

### ReqCreateGamePlan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| account_list | [uint32](#uint32) | repeated |  |
| game_start_time | [uint32](#uint32) |  |  |
| shuffle_seats | [uint32](#uint32) |  |  |
| ai_level | [uint32](#uint32) |  |  |






<a name="lq-ReqCreateIAPOrder"></a>

### ReqCreateIAPOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| access_token | [string](#string) |  |  |
| debt_order_id | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPAuOrder"></a>

### ReqCreateJPAuOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPCreditCardOrder"></a>

### ReqCreateJPCreditCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPDocomoOrder"></a>

### ReqCreateJPDocomoOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPGMOOrder"></a>

### ReqCreateJPGMOOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPPayPayOrder"></a>

### ReqCreateJPPayPayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPPaypalOrder"></a>

### ReqCreateJPPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPSoftbankOrder"></a>

### ReqCreateJPSoftbankOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateJPWebMoneyOrder"></a>

### ReqCreateJPWebMoneyOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateKRAlipayOrder"></a>

### ReqCreateKRAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateKRJCBOrder"></a>

### ReqCreateKRJCBOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateKRMasterCardOrder"></a>

### ReqCreateKRMasterCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateKRPaypalOrder"></a>

### ReqCreateKRPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateKRVisaOrder"></a>

### ReqCreateKRVisaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| return_url | [string](#string) |  |  |
| access_token | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateMyCardOrder"></a>

### ReqCreateMyCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| debt_order_id | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateNickname"></a>

### ReqCreateNickname



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nickname | [string](#string) |  |  |
| advertise_str | [string](#string) |  |  |
| tag | [string](#string) |  |  |






<a name="lq-ReqCreatePaypalOrder"></a>

### ReqCreatePaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| debt_order_id | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreatePhoneLoginBind"></a>

### ReqCreatePhoneLoginBind



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| password | [string](#string) |  |  |






<a name="lq-ReqCreatePhoneVerifyCode"></a>

### ReqCreatePhoneVerifyCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| phone | [string](#string) |  |  |
| usage | [uint32](#uint32) |  |  |






<a name="lq-ReqCreateRoom"></a>

### ReqCreateRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| player_count | [uint32](#uint32) |  |  |
| mode | [GameMode](#lq-GameMode) |  |  |
| public_live | [bool](#bool) |  |  |
| client_version_string | [string](#string) |  |  |
| pre_rule | [string](#string) |  |  |






<a name="lq-ReqCreateSeerReport"></a>

### ReqCreateSeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |






<a name="lq-ReqCreateSteamOrder"></a>

### ReqCreateSteamOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| language | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| steam_id | [string](#string) |  |  |
| debt_order_id | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateWechatAppOrder"></a>

### ReqCreateWechatAppOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| account_ip | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateWechatNativeOrder"></a>

### ReqCreateWechatNativeOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| account_ip | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateXsollaOrder"></a>

### ReqCreateXsollaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| payment_method | [uint32](#uint32) |  |  |
| debt_order_id | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |
| account_ip | [string](#string) |  |  |






<a name="lq-ReqCreateYostarOrder"></a>

### ReqCreateYostarOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| order_type | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCreateYostarV4SDKOrder"></a>

### ReqCreateYostarV4SDKOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| client_type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| order_type | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqCurrentMatchInfo"></a>

### ReqCurrentMatchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqDMMPreLogin"></a>

### ReqDMMPreLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| finish_url | [string](#string) |  |  |






<a name="lq-ReqDeleteComment"></a>

### ReqDeleteComment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| delete_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqDeleteMail"></a>

### ReqDeleteMail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id | [uint32](#uint32) |  |  |






<a name="lq-ReqDeliverAA32Order"></a>

### ReqDeliverAA32Order



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nsa_id | [string](#string) |  |  |
| nsa_token | [string](#string) |  |  |






<a name="lq-ReqDigMine"></a>

### ReqDigMine



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| point | [Point](#lq-Point) |  |  |






<a name="lq-ReqDoActivitySignIn"></a>

### ReqDoActivitySignIn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqEmailLogin"></a>

### ReqEmailLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| email | [string](#string) |  |  |
| password | [string](#string) |  |  |
| reconnect | [bool](#bool) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| random_key | [string](#string) |  |  |
| client_version | [string](#string) |  |  |
| gen_access_token | [bool](#bool) |  |  |
| currency_platforms | [uint32](#uint32) | repeated |  |






<a name="lq-ReqEnterArena"></a>

### ReqEnterArena



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqEnterCustomizedContest"></a>

### ReqEnterCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| lang | [string](#string) |  |  |






<a name="lq-ReqExchangeActivityItem"></a>

### ReqExchangeActivityItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exchange_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqExchangeCurrency"></a>

### ReqExchangeCurrency



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqFastLogin"></a>

### ReqFastLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqFeedActivityFeed"></a>

### ReqFeedActivityFeed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchAccountGameHuRecords"></a>

### ReqFetchAccountGameHuRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchAccountInfoExtra"></a>

### ReqFetchAccountInfoExtra



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchActivityFlipInfo"></a>

### ReqFetchActivityFlipInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchActivityRank"></a>

### ReqFetchActivityRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| account_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqFetchAmuletActivityData"></a>

### ReqFetchAmuletActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchAnnouncement"></a>

### ReqFetchAnnouncement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |
| platform | [string](#string) |  |  |






<a name="lq-ReqFetchBannerActivityData"></a>

### ReqFetchBannerActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id_list | [uint32](#uint32) | repeated |  |
| lang | [string](#string) |  |  |






<a name="lq-ReqFetchBingoActivityData"></a>

### ReqFetchBingoActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchCommentContent"></a>

### ReqFetchCommentContent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| comment_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqFetchCommentList"></a>

### ReqFetchCommentList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchContestPlayerRank"></a>

### ReqFetchContestPlayerRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |
| offset | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchContestTeamMember"></a>

### ReqFetchContestTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| team_id | [uint32](#uint32) |  |  |
| offset | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchContestTeamPlayerRank"></a>

### ReqFetchContestTeamPlayerRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| offset | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchContestTeamRank"></a>

### ReqFetchContestTeamRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |
| offset | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchCustomizedContestAuthInfo"></a>

### ReqFetchCustomizedContestAuthInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchCustomizedContestByContestId"></a>

### ReqFetchCustomizedContestByContestId



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contest_id | [uint32](#uint32) |  |  |
| lang | [string](#string) |  |  |






<a name="lq-ReqFetchCustomizedContestGameLiveList"></a>

### ReqFetchCustomizedContestGameLiveList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchCustomizedContestGameRecords"></a>

### ReqFetchCustomizedContestGameRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| last_index | [uint32](#uint32) |  |  |
| season_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchCustomizedContestList"></a>

### ReqFetchCustomizedContestList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| lang | [string](#string) |  |  |






<a name="lq-ReqFetchCustomizedContestOnlineInfo"></a>

### ReqFetchCustomizedContestOnlineInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchDailySignActivityData"></a>

### ReqFetchDailySignActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqFetchFriendGiftActivityData"></a>

### ReqFetchFriendGiftActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| account_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqFetchJPCommonCreditCardOrder"></a>

### ReqFetchJPCommonCreditCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchLastPrivacy"></a>

### ReqFetchLastPrivacy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) | repeated |  |






<a name="lq-ReqFetchManagerCustomizedContest"></a>

### ReqFetchManagerCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchOBToken"></a>

### ReqFetchOBToken



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |






<a name="lq-ReqFetchOauth2"></a>

### ReqFetchOauth2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchProgressRewardActivityInfo"></a>

### ReqFetchProgressRewardActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchQuestionnaireDetail"></a>

### ReqFetchQuestionnaireDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| lang | [string](#string) |  |  |
| channel | [string](#string) |  |  |






<a name="lq-ReqFetchQuestionnaireList"></a>

### ReqFetchQuestionnaireList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |
| channel | [string](#string) |  |  |






<a name="lq-ReqFetchRPGBattleHistory"></a>

### ReqFetchRPGBattleHistory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchRankPointLeaderboard"></a>

### ReqFetchRankPointLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchReadyPlayerList"></a>

### ReqFetchReadyPlayerList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchRollingNotice"></a>

### ReqFetchRollingNotice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |






<a name="lq-ReqFetchSeerReport"></a>

### ReqFetchSeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |






<a name="lq-ReqFetchSimulationGameRank"></a>

### ReqFetchSimulationGameRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchSimulationGameRecord"></a>

### ReqFetchSimulationGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchVoteActivity"></a>

### ReqFetchVoteActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqFetchmanagerCustomizedContestList"></a>

### ReqFetchmanagerCustomizedContestList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |






<a name="lq-ReqFinishCombiningOrder"></a>

### ReqFinishCombiningOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| craft_pos | [uint32](#uint32) |  |  |
| order_pos | [uint32](#uint32) |  |  |






<a name="lq-ReqFinishedEnding"></a>

### ReqFinishedEnding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |






<a name="lq-ReqForceCompleteChallengeTask"></a>

### ReqForceCompleteChallengeTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGMCommand"></a>

### ReqGMCommand



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command | [string](#string) |  |  |






<a name="lq-ReqGainAccumulatedPointActivityReward"></a>

### ReqGainAccumulatedPointActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGainMultiPointActivityReward"></a>

### ReqGainMultiPointActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| reward_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqGainRankPointReward"></a>

### ReqGainRankPointReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGainVipReward"></a>

### ReqGainVipReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vip_level | [uint32](#uint32) |  |  |






<a name="lq-ReqGameLiveInfo"></a>

### ReqGameLiveInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |






<a name="lq-ReqGameLiveLeftSegment"></a>

### ReqGameLiveLeftSegment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |
| last_segment_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGameLiveList"></a>

### ReqGameLiveList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGamePointRank"></a>

### ReqGamePointRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGameRecord"></a>

### ReqGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqGameRecordList"></a>

### ReqGameRecordList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqGameRecordListV2"></a>

### ReqGameRecordListV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag | [uint32](#uint32) |  |  |
| begin_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| ranks | [uint32](#uint32) | repeated |  |
| modes | [uint32](#uint32) | repeated |  |
| max_hu_type | [uint32](#uint32) |  |  |
| level_mode | [uint32](#uint32) | repeated |  |






<a name="lq-ReqGameRecordsDetail"></a>

### ReqGameRecordsDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid_list | [string](#string) | repeated |  |






<a name="lq-ReqGameRecordsDetailV2"></a>

### ReqGameRecordsDetailV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid_list | [string](#string) | repeated |  |






<a name="lq-ReqGenerateAnnualReportToken"></a>

### ReqGenerateAnnualReportToken



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |






<a name="lq-ReqGenerateCombiningCraft"></a>

### ReqGenerateCombiningCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| bin_id | [uint32](#uint32) |  |  |






<a name="lq-ReqGetFriendVillageData"></a>

### ReqGetFriendVillageData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_list | [uint32](#uint32) | repeated |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqHandleFriendApply"></a>

### ReqHandleFriendApply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| method | [uint32](#uint32) |  |  |






<a name="lq-ReqHeatBeat"></a>

### ReqHeatBeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| no_operation_counter | [uint32](#uint32) |  |  |






<a name="lq-ReqIslandActivityBuy"></a>

### ReqIslandActivityBuy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| items | [ReqIslandActivityBuy.BuyItems](#lq-ReqIslandActivityBuy-BuyItems) | repeated |  |






<a name="lq-ReqIslandActivityBuy-BuyItems"></a>

### ReqIslandActivityBuy.BuyItems



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) | repeated |  |
| rotate | [uint32](#uint32) |  |  |
| bag_id | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-ReqIslandActivityMove"></a>

### ReqIslandActivityMove



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| zone_id | [uint32](#uint32) |  |  |






<a name="lq-ReqIslandActivitySell"></a>

### ReqIslandActivitySell



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| items | [ReqIslandActivitySell.SellItem](#lq-ReqIslandActivitySell-SellItem) | repeated |  |






<a name="lq-ReqIslandActivitySell-SellItem"></a>

### ReqIslandActivitySell.SellItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bag_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-ReqIslandActivityTidyBag"></a>

### ReqIslandActivityTidyBag



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| bag_data | [ReqIslandActivityTidyBag.BagData](#lq-ReqIslandActivityTidyBag-BagData) | repeated |  |






<a name="lq-ReqIslandActivityTidyBag-BagData"></a>

### ReqIslandActivityTidyBag.BagData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bag_id | [uint32](#uint32) |  |  |
| items | [ReqIslandActivityTidyBag.BagData.ITemData](#lq-ReqIslandActivityTidyBag-BagData-ITemData) | repeated |  |
| drops | [uint32](#uint32) | repeated |  |






<a name="lq-ReqIslandActivityTidyBag-BagData-ITemData"></a>

### ReqIslandActivityTidyBag.BagData.ITemData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) | repeated |  |
| rotate | [uint32](#uint32) |  |  |






<a name="lq-ReqIslandActivityUnlockBagGrid"></a>

### ReqIslandActivityUnlockBagGrid



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| bag_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) | repeated |  |






<a name="lq-ReqJoinCustomizedContestChatRoom"></a>

### ReqJoinCustomizedContestChatRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqJoinMatchQueue"></a>

### ReqJoinMatchQueue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_mode | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqJoinRoom"></a>

### ReqJoinRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| room_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqLeaveComment"></a>

### ReqLeaveComment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| content | [string](#string) |  |  |






<a name="lq-ReqLevelLeaderboard"></a>

### ReqLevelLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqLikeSNS"></a>

### ReqLikeSNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqLogReport"></a>

### ReqLogReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success | [uint32](#uint32) |  |  |
| failed | [uint32](#uint32) |  |  |






<a name="lq-ReqLogin"></a>

### ReqLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account | [string](#string) |  |  |
| password | [string](#string) |  |  |
| reconnect | [bool](#bool) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| random_key | [string](#string) |  |  |
| client_version | [ClientVersionInfo](#lq-ClientVersionInfo) |  |  |
| gen_access_token | [bool](#bool) |  |  |
| currency_platforms | [uint32](#uint32) | repeated |  |
| type | [uint32](#uint32) |  |  |
| version | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |
| tag | [string](#string) |  |  |






<a name="lq-ReqLoginBeat"></a>

### ReqLoginBeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| contract | [string](#string) |  |  |






<a name="lq-ReqLogout"></a>

### ReqLogout







<a name="lq-ReqMMOActivityDebugSetTeamCandidate"></a>

### ReqMMOActivityDebugSetTeamCandidate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| friend_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| random_friends | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| npc_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |






<a name="lq-ReqMMOActivityEquipFusion"></a>

### ReqMMOActivityEquipFusion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| equip_list | [uint32](#uint32) | repeated |  |
| target_type | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivityFetchData"></a>

### ReqMMOActivityFetchData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivityFinishBattle"></a>

### ReqMMOActivityFinishBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivityReceiveSupportReward"></a>

### ReqMMOActivityReceiveSupportReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivitySetCharacter"></a>

### ReqMMOActivitySetCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| character_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivitySetEquip"></a>

### ReqMMOActivitySetEquip



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |






<a name="lq-ReqMMOActivitySetTeamMember"></a>

### ReqMMOActivitySetTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| members | [ReqMMOActivitySetTeamMember.MMOActivityTeamMember](#lq-ReqMMOActivitySetTeamMember-MMOActivityTeamMember) | repeated |  |






<a name="lq-ReqMMOActivitySetTeamMember-MMOActivityTeamMember"></a>

### ReqMMOActivitySetTeamMember.MMOActivityTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivityStartBattle"></a>

### ReqMMOActivityStartBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMMOActivityUpdatehFriendList"></a>

### ReqMMOActivityUpdatehFriendList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqMarathonActivityFinishRace"></a>

### ReqMarathonActivityFinishRace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| race_data | [ActivityMarathonCheckData](#lq-ActivityMarathonCheckData) | repeated |  |
| record | [MarathonGameRecord](#lq-MarathonGameRecord) |  |  |
| race_id | [string](#string) |  |  |






<a name="lq-ReqMarathonActivityStartRace"></a>

### ReqMarathonActivityStartRace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqModifyBirthday"></a>

### ReqModifyBirthday



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| birthday | [int32](#int32) |  |  |






<a name="lq-ReqModifyNickname"></a>

### ReqModifyNickname



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nickname | [string](#string) |  |  |
| use_item_id | [uint32](#uint32) |  |  |






<a name="lq-ReqModifyPassword"></a>

### ReqModifyPassword



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new_password | [string](#string) |  |  |
| old_password | [string](#string) |  |  |
| secure_token | [string](#string) |  |  |






<a name="lq-ReqModifyRoom"></a>

### ReqModifyRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| robot_count | [uint32](#uint32) |  |  |






<a name="lq-ReqModifySignature"></a>

### ReqModifySignature



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| signature | [string](#string) |  |  |






<a name="lq-ReqMoveCombiningCraft"></a>

### ReqMoveCombiningCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| from | [uint32](#uint32) |  |  |
| to | [uint32](#uint32) |  |  |






<a name="lq-ReqMultiAccountId"></a>

### ReqMultiAccountId



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqMutiChallengeLevel"></a>

### ReqMutiChallengeLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id_list | [uint32](#uint32) | repeated |  |
| season | [uint32](#uint32) |  |  |






<a name="lq-ReqNextGameRecordList"></a>

### ReqNextGameRecordList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| iterator | [string](#string) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqNextRoundVillage"></a>

### ReqNextRoundVillage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqOauth2Auth"></a>

### ReqOauth2Auth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| code | [string](#string) |  |  |
| uid | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqOauth2Check"></a>

### ReqOauth2Check



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| access_token | [string](#string) |  |  |






<a name="lq-ReqOauth2Login"></a>

### ReqOauth2Login



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| access_token | [string](#string) |  |  |
| reconnect | [bool](#bool) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| random_key | [string](#string) |  |  |
| client_version | [ClientVersionInfo](#lq-ClientVersionInfo) |  |  |
| gen_access_token | [bool](#bool) |  |  |
| currency_platforms | [uint32](#uint32) | repeated |  |
| version | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |
| tag | [string](#string) |  |  |






<a name="lq-ReqOauth2Signup"></a>

### ReqOauth2Signup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| access_token | [string](#string) |  |  |
| email | [string](#string) |  |  |
| advertise_str | [string](#string) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| client_version | [ClientVersionInfo](#lq-ClientVersionInfo) |  |  |
| client_version_string | [string](#string) |  |  |
| tag | [string](#string) |  |  |






<a name="lq-ReqOpenAllRewardItem"></a>

### ReqOpenAllRewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenChest"></a>

### ReqOpenChest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| use_ticket | [bool](#bool) |  |  |
| choose_up_activity_id | [uint32](#uint32) |  |  |
| choose_group_activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenGacha"></a>

### ReqOpenGacha



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenManualItem"></a>

### ReqOpenManualItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| select_id | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenPreChestItem"></a>

### ReqOpenPreChestItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| pool_id | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenRandomRewardItem"></a>

### ReqOpenRandomRewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqOpenidCheck"></a>

### ReqOpenidCheck



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| token | [string](#string) |  |  |






<a name="lq-ReqPayMonthTicket"></a>

### ReqPayMonthTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ticket_id | [uint32](#uint32) |  |  |






<a name="lq-ReqPlatformBillingProducts"></a>

### ReqPlatformBillingProducts



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| shelves_id | [uint32](#uint32) |  |  |






<a name="lq-ReqPrepareLogin"></a>

### ReqPrepareLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| access_token | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqProgressRewardActivityReceive"></a>

### ReqProgressRewardActivityReceive



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| progresses | [uint32](#uint32) | repeated |  |






<a name="lq-ReqQuestCrewActivityFeed"></a>

### ReqQuestCrewActivityFeed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| member_id | [uint32](#uint32) | repeated |  |






<a name="lq-ReqQuestCrewActivityHire"></a>

### ReqQuestCrewActivityHire



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| member_id | [uint32](#uint32) |  |  |






<a name="lq-ReqQuestCrewActivityRefreshMarket"></a>

### ReqQuestCrewActivityRefreshMarket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqQuestCrewActivityStartQuest"></a>

### ReqQuestCrewActivityStartQuest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| joined_members | [uint32](#uint32) | repeated |  |
| quest_id | [uint32](#uint32) |  |  |






<a name="lq-ReqRandomCharacter"></a>

### ReqRandomCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enabled | [bool](#bool) |  |  |
| pool | [RandomCharacter](#lq-RandomCharacter) | repeated |  |






<a name="lq-ReqReadAnnouncement"></a>

### ReqReadAnnouncement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| announcement_id | [uint32](#uint32) |  |  |
| announcement_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqReadMail"></a>

### ReqReadMail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReadSNS"></a>

### ReqReadSNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveAchievementGroupReward"></a>

### ReqReceiveAchievementGroupReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveAchievementReward"></a>

### ReqReceiveAchievementReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| achievement_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveActivityFlipTask"></a>

### ReqReceiveActivityFlipTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveActivityFlipTaskBatch"></a>

### ReqReceiveActivityFlipTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqReceiveActivityGift"></a>

### ReqReceiveActivityGift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveActivitySpotReward"></a>

### ReqReceiveActivitySpotReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveAllActivityGift"></a>

### ReqReceiveAllActivityGift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveChallengeRankReward"></a>

### ReqReceiveChallengeRankReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveCharacterRewards"></a>

### ReqReceiveCharacterRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveRPGReward"></a>

### ReqReceiveRPGReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| monster_seq | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveRPGRewards"></a>

### ReqReceiveRPGRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveUpgradeActivityReward"></a>

### ReqReceiveUpgradeActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReceiveVillageBuildingReward"></a>

### ReqReceiveVillageBuildingReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| building_id | [uint32](#uint32) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-ReqReceiveVillageTripReward"></a>

### ReqReceiveVillageTripReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| dest_id | [uint32](#uint32) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-ReqRecoverCombiningRecycle"></a>

### ReqRecoverCombiningRecycle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqRefreshDailyTask"></a>

### ReqRefreshDailyTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| task_id | [uint32](#uint32) |  |  |






<a name="lq-ReqRefreshGameObserveAuth"></a>

### ReqRefreshGameObserveAuth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| token | [string](#string) |  |  |






<a name="lq-ReqRemarkFriend"></a>

### ReqRemarkFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| remark | [string](#string) |  |  |






<a name="lq-ReqRemoveCollectedGameRecord"></a>

### ReqRemoveCollectedGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |






<a name="lq-ReqRemoveFriend"></a>

### ReqRemoveFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |






<a name="lq-ReqReplySNS"></a>

### ReqReplySNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqReshZHPShop"></a>

### ReqReshZHPShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| free_refresh | [uint32](#uint32) |  |  |
| cost_refresh | [uint32](#uint32) |  |  |






<a name="lq-ReqResolveFestivalActivityEvent"></a>

### ReqResolveFestivalActivityEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| select | [uint32](#uint32) |  |  |






<a name="lq-ReqResolveFestivalActivityProposal"></a>

### ReqResolveFestivalActivityProposal



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| select | [uint32](#uint32) |  |  |






<a name="lq-ReqRichmanChestInfo"></a>

### ReqRichmanChestInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqRichmanNextMove"></a>

### ReqRichmanNextMove



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqRichmanSpecialMove"></a>

### ReqRichmanSpecialMove



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| step | [uint32](#uint32) |  |  |






<a name="lq-ReqRoomDressing"></a>

### ReqRoomDressing



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dressing | [bool](#bool) |  |  |






<a name="lq-ReqRoomKickPlayer"></a>

### ReqRoomKickPlayer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqRoomReady"></a>

### ReqRoomReady



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ready | [bool](#bool) |  |  |






<a name="lq-ReqRoomStart"></a>

### ReqRoomStart







<a name="lq-ReqSaveCommonViews"></a>

### ReqSaveCommonViews



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| views | [ViewSlot](#lq-ViewSlot) | repeated |  |
| save_index | [uint32](#uint32) |  |  |
| is_use | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |






<a name="lq-ReqSayChatMessage"></a>

### ReqSayChatMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [string](#string) |  |  |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSearchAccountByEidLobby"></a>

### ReqSearchAccountByEidLobby



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| eid | [uint32](#uint32) |  |  |






<a name="lq-ReqSearchAccountById"></a>

### ReqSearchAccountById



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSearchAccountByPattern"></a>

### ReqSearchAccountByPattern



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| search_next | [bool](#bool) |  |  |
| pattern | [string](#string) |  |  |






<a name="lq-ReqSelectChestChooseGroupActivity"></a>

### ReqSelectChestChooseGroupActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| selection | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSelectChestChooseUp"></a>

### ReqSelectChestChooseUp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| selection | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSellItem"></a>

### ReqSellItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sells | [ReqSellItem.Item](#lq-ReqSellItem-Item) | repeated |  |






<a name="lq-ReqSellItem-Item"></a>

### ReqSellItem.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqSendActivityGiftToFriend"></a>

### ReqSendActivityGiftToFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| target_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSendClientMessage"></a>

### ReqSendClientMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| content | [string](#string) |  |  |






<a name="lq-ReqSendGiftToCharacter"></a>

### ReqSendGiftToCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| gifts | [ReqSendGiftToCharacter.Gift](#lq-ReqSendGiftToCharacter-Gift) | repeated |  |






<a name="lq-ReqSendGiftToCharacter-Gift"></a>

### ReqSendGiftToCharacter.Gift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqSetAccountFavoriteHu"></a>

### ReqSetAccountFavoriteHu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode | [uint32](#uint32) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |






<a name="lq-ReqSetActivityBuff"></a>

### ReqSetActivityBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_list | [ReqSetActivityBuff.BuffInfo](#lq-ReqSetActivityBuff-BuffInfo) | repeated |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSetActivityBuff-BuffInfo"></a>

### ReqSetActivityBuff.BuffInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ReqSetFriendRoomRandomBotChar"></a>

### ReqSetFriendRoomRandomBotChar



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| disable_random_char | [uint32](#uint32) |  |  |






<a name="lq-ReqSetHiddenCharacter"></a>

### ReqSetHiddenCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chara_list | [uint32](#uint32) | repeated |  |






<a name="lq-ReqSetLoadingImage"></a>

### ReqSetLoadingImage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| images | [uint32](#uint32) | repeated |  |






<a name="lq-ReqSetVerifiedHidden"></a>

### ReqSetVerifiedHidden



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| verified_hidden | [uint32](#uint32) |  |  |






<a name="lq-ReqSetVillageWorker"></a>

### ReqSetVillageWorker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| building_id | [uint32](#uint32) |  |  |
| worker_pos | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqShootActivityAttackEnemies"></a>

### ReqShootActivityAttackEnemies



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| bullets_count | [uint32](#uint32) |  |  |
| position | [uint32](#uint32) |  |  |






<a name="lq-ReqShopPurchase"></a>

### ReqShopPurchase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-ReqSignupAccount"></a>

### ReqSignupAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account | [string](#string) |  |  |
| password | [string](#string) |  |  |
| code | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |
| device | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| client_version_string | [string](#string) |  |  |
| tag | [string](#string) |  |  |






<a name="lq-ReqSignupCustomizedContest"></a>

### ReqSignupCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqSimV2ActivityEndMatch"></a>

### ReqSimV2ActivityEndMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivityFetchInfo"></a>

### ReqSimV2ActivityFetchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivityGiveUp"></a>

### ReqSimV2ActivityGiveUp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivitySelectEvent"></a>

### ReqSimV2ActivitySelectEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| selection_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivitySetUpgrade"></a>

### ReqSimV2ActivitySetUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| upgrade | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |






<a name="lq-ReqSimV2ActivityStartMatch"></a>

### ReqSimV2ActivityStartMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivityStartSeason"></a>

### ReqSimV2ActivityStartSeason



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSimV2ActivityTrain"></a>

### ReqSimV2ActivityTrain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| ability | [uint32](#uint32) |  |  |
| skip | [uint32](#uint32) |  |  |






<a name="lq-ReqSimulationActivityTrain"></a>

### ReqSimulationActivityTrain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ReqSnowballActivityFinishBattle"></a>

### ReqSnowballActivityFinishBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| player_action | [ActivitySnowballPlayerAction](#lq-ActivitySnowballPlayerAction) | repeated |  |
| result | [uint32](#uint32) |  |  |
| battle_id | [string](#string) |  |  |






<a name="lq-ReqSnowballActivityReceiveReward"></a>

### ReqSnowballActivityReceiveReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) | repeated |  |






<a name="lq-ReqSnowballActivityStartBattle"></a>

### ReqSnowballActivityStartBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSnowballActivityUpgrade"></a>

### ReqSnowballActivityUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| upgrade | [ActivitySnowballUpgrade](#lq-ActivitySnowballUpgrade) | repeated |  |






<a name="lq-ReqSolveGooglePlayOrder"></a>

### ReqSolveGooglePlayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inapp_purchase_data | [string](#string) |  |  |
| inapp_data_signature | [string](#string) |  |  |






<a name="lq-ReqSolveGooglePlayOrderV3"></a>

### ReqSolveGooglePlayOrderV3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |
| transaction_id | [string](#string) |  |  |
| token | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStartCustomizedContest"></a>

### ReqStartCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqStartSimulationActivityGame"></a>

### ReqStartSimulationActivityGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStartUnifiedMatch"></a>

### ReqStartUnifiedMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_sid | [string](#string) |  |  |
| client_version_string | [string](#string) |  |  |






<a name="lq-ReqStartVillageTrip"></a>

### ReqStartVillageTrip



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dest | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStopCustomizedContest"></a>

### ReqStopCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityReceiveAllFinishReward"></a>

### ReqStoryActivityReceiveAllFinishReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityReceiveEndingReward"></a>

### ReqStoryActivityReceiveEndingReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityReceiveFinishReward"></a>

### ReqStoryActivityReceiveFinishReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityUnlock"></a>

### ReqStoryActivityUnlock



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityUnlockEnding"></a>

### ReqStoryActivityUnlockEnding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |






<a name="lq-ReqStoryActivityUnlockEndingAndReceive"></a>

### ReqStoryActivityUnlockEndingAndReceive



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |






<a name="lq-ReqSubmitQuestionnaire"></a>

### ReqSubmitQuestionnaire



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| questionnaire_id | [uint32](#uint32) |  |  |
| questionnaire_version_id | [uint32](#uint32) |  |  |
| answers | [ReqSubmitQuestionnaire.QuestionnaireAnswer](#lq-ReqSubmitQuestionnaire-QuestionnaireAnswer) | repeated |  |
| open_time | [uint32](#uint32) |  |  |
| finish_time | [uint32](#uint32) |  |  |
| client | [string](#string) |  |  |






<a name="lq-ReqSubmitQuestionnaire-QuestionnaireAnswer"></a>

### ReqSubmitQuestionnaire.QuestionnaireAnswer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| question_id | [uint32](#uint32) |  |  |
| values | [ReqSubmitQuestionnaire.QuestionnaireAnswer.QuestionnaireAnswerValue](#lq-ReqSubmitQuestionnaire-QuestionnaireAnswer-QuestionnaireAnswerValue) | repeated |  |






<a name="lq-ReqSubmitQuestionnaire-QuestionnaireAnswer-QuestionnaireAnswerValue"></a>

### ReqSubmitQuestionnaire.QuestionnaireAnswer.QuestionnaireAnswerValue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |
| custom_input | [string](#string) |  |  |






<a name="lq-ReqTakeAttachment"></a>

### ReqTakeAttachment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id | [uint32](#uint32) |  |  |






<a name="lq-ReqTargetCustomizedContest"></a>

### ReqTargetCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqTaskRequest"></a>

### ReqTaskRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| params | [uint32](#uint32) | repeated |  |






<a name="lq-ReqUnbindPhoneNumber"></a>

### ReqUnbindPhoneNumber



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [string](#string) |  |  |
| phone | [string](#string) |  |  |
| password | [string](#string) |  |  |






<a name="lq-ReqUnlockActivitySpot"></a>

### ReqUnlockActivitySpot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUnlockActivitySpotEnding"></a>

### ReqUnlockActivitySpotEnding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUpdateAccountSettings"></a>

### ReqUpdateAccountSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| setting | [AccountSetting](#lq-AccountSetting) |  |  |






<a name="lq-ReqUpdateCharacterSort"></a>

### ReqUpdateCharacterSort



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sort | [uint32](#uint32) | repeated |  |
| other_sort | [uint32](#uint32) | repeated |  |
| hidden_characters | [uint32](#uint32) | repeated |  |






<a name="lq-ReqUpdateClientValue"></a>

### ReqUpdateClientValue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-ReqUpdateCommentSetting"></a>

### ReqUpdateCommentSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| comment_allow | [uint32](#uint32) |  |  |






<a name="lq-ReqUpdateIDCardInfo"></a>

### ReqUpdateIDCardInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fullname | [string](#string) |  |  |
| card_no | [string](#string) |  |  |






<a name="lq-ReqUpdateManagerCustomizedContest"></a>

### ReqUpdateManagerCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| open_show | [uint32](#uint32) |  |  |
| game_rule_setting | [GameMode](#lq-GameMode) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| unique_id | [uint32](#uint32) |  |  |
| auto_match | [uint32](#uint32) |  |  |
| rank_rule | [uint32](#uint32) |  |  |
| contest_setting | [ContestSetting](#lq-ContestSetting) |  |  |






<a name="lq-ReqUpdateReadComment"></a>

### ReqUpdateReadComment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| read_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUpgradeActivityBuff"></a>

### ReqUpgradeActivityBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUpgradeActivityLevel"></a>

### ReqUpgradeActivityLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| group | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqUpgradeCharacter"></a>

### ReqUpgradeCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUpgradeVillageBuilding"></a>

### ReqUpgradeVillageBuilding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| building_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUseBagItem"></a>

### ReqUseBagItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |






<a name="lq-ReqUseCommonView"></a>

### ReqUseCommonView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint32](#uint32) |  |  |






<a name="lq-ReqUseGiftCode"></a>

### ReqUseGiftCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [string](#string) |  |  |






<a name="lq-ReqUseTitle"></a>

### ReqUseTitle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title | [uint32](#uint32) |  |  |






<a name="lq-ReqUserComplain"></a>

### ReqUserComplain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| content | [string](#string) |  |  |
| game_uuid | [string](#string) |  |  |
| round_info | [ReqUserComplain.GameRoundInfo](#lq-ReqUserComplain-GameRoundInfo) |  |  |






<a name="lq-ReqUserComplain-GameRoundInfo"></a>

### ReqUserComplain.GameRoundInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| seat | [uint32](#uint32) |  |  |
| xun | [uint32](#uint32) |  |  |






<a name="lq-ReqVerificationIAPOrder"></a>

### ReqVerificationIAPOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |
| transaction_id | [string](#string) |  |  |
| receipt_data | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqVerifyCodeForSecure"></a>

### ReqVerifyCodeForSecure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [string](#string) |  |  |
| operation | [uint32](#uint32) |  |  |






<a name="lq-ReqVerifyMyCardOrder"></a>

### ReqVerifyMyCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqVerifySteamOrder"></a>

### ReqVerifySteamOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| order_id | [string](#string) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ReqVoteActivity"></a>

### ReqVoteActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vote | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ReqYostarDeleteAccount"></a>

### ReqYostarDeleteAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| server | [uint32](#uint32) |  |  |






<a name="lq-ResAccountActivityData"></a>

### ResAccountActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| exchange_records | [ExchangeRecord](#lq-ExchangeRecord) | repeated |  |
| task_progress_list | [TaskProgress](#lq-TaskProgress) | repeated |  |
| accumulated_point_list | [ActivityAccumulatedPointData](#lq-ActivityAccumulatedPointData) | repeated |  |
| rank_data_list | [ActivityRankPointData](#lq-ActivityRankPointData) | repeated |  |
| flip_task_progress_list | [TaskProgress](#lq-TaskProgress) | repeated |  |
| sign_in_data | [ResAccountActivityData.ActivitySignInData](#lq-ResAccountActivityData-ActivitySignInData) | repeated |  |
| richman_data | [ResAccountActivityData.ActivityRichmanData](#lq-ResAccountActivityData-ActivityRichmanData) | repeated |  |
| period_task_progress_list | [TaskProgress](#lq-TaskProgress) | repeated |  |
| random_task_progress_list | [TaskProgress](#lq-TaskProgress) | repeated |  |
| chest_up_data | [ResAccountActivityData.ChestUpData](#lq-ResAccountActivityData-ChestUpData) | repeated |  |
| sns_data | [ResAccountActivityData.ActivitySNSData](#lq-ResAccountActivityData-ActivitySNSData) |  |  |
| mine_data | [MineActivityData](#lq-MineActivityData) | repeated |  |
| rpg_data | [RPGActivity](#lq-RPGActivity) | repeated |  |
| arena_data | [ActivityArenaData](#lq-ActivityArenaData) | repeated |  |
| feed_data | [FeedActivityData](#lq-FeedActivityData) | repeated |  |
| segment_task_progress_list | [SegmentTaskProgress](#lq-SegmentTaskProgress) | repeated |  |
| vote_records | [VoteData](#lq-VoteData) | repeated |  |
| spot_data | [ActivitySpotData](#lq-ActivitySpotData) | repeated |  |
| friend_gift_data | [ActivityFriendGiftData](#lq-ActivityFriendGiftData) | repeated |  |
| upgrade_data | [ActivityUpgradeData](#lq-ActivityUpgradeData) | repeated |  |
| gacha_data | [ActivityGachaUpdateData](#lq-ActivityGachaUpdateData) | repeated |  |
| simulation_data | [ActivitySimulationData](#lq-ActivitySimulationData) | repeated |  |
| combining_data | [ActivityCombiningLQData](#lq-ActivityCombiningLQData) | repeated |  |
| village_data | [ActivityVillageData](#lq-ActivityVillageData) | repeated |  |
| festival_data | [ActivityFestivalData](#lq-ActivityFestivalData) | repeated |  |
| island_data | [ActivityIslandData](#lq-ActivityIslandData) | repeated |  |
| story_data | [ActivityStoryData](#lq-ActivityStoryData) | repeated |  |
| choose_up_data | [ActivityChooseUpData](#lq-ActivityChooseUpData) | repeated |  |
| progress_reward_data | [ActivityProgressRewardData](#lq-ActivityProgressRewardData) | repeated |  |
| quest_crew_data | [ActivityQuestCrewData](#lq-ActivityQuestCrewData) | repeated |  |
| shoot_data | [ActivityShootData](#lq-ActivityShootData) | repeated |  |
| bingo_data | [ActivityBingoData](#lq-ActivityBingoData) | repeated |  |
| snowball_data | [ActivitySnowballData](#lq-ActivitySnowballData) | repeated |  |
| marathon_data | [ActivityMarathonData](#lq-ActivityMarathonData) | repeated |  |
| choose_group_up_data | [ActivityChooseGroupData](#lq-ActivityChooseGroupData) | repeated |  |
| mmo_data | [ActivityMMOData](#lq-ActivityMMOData) | repeated |  |






<a name="lq-ResAccountActivityData-ActivityRichmanData"></a>

### ResAccountActivityData.ActivityRichmanData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| location | [uint32](#uint32) |  |  |
| finished_count | [uint32](#uint32) |  |  |
| chest_position | [uint32](#uint32) |  |  |
| bank_save | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| buff | [ResAccountActivityData.BuffData](#lq-ResAccountActivityData-BuffData) | repeated |  |






<a name="lq-ResAccountActivityData-ActivitySNSData"></a>

### ResAccountActivityData.ActivitySNSData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| blog | [SNSBlog](#lq-SNSBlog) | repeated |  |
| liked_id | [uint32](#uint32) | repeated |  |
| reply | [SNSReply](#lq-SNSReply) | repeated |  |






<a name="lq-ResAccountActivityData-ActivitySignInData"></a>

### ResAccountActivityData.ActivitySignInData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| sign_in_count | [uint32](#uint32) |  |  |
| last_sign_in_time | [uint32](#uint32) |  |  |






<a name="lq-ResAccountActivityData-BuffData"></a>

### ResAccountActivityData.BuffData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| remain | [uint32](#uint32) |  |  |
| effect | [uint32](#uint32) |  |  |






<a name="lq-ResAccountActivityData-ChestUpData"></a>

### ResAccountActivityData.ChestUpData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResAccountChallengeRankInfo"></a>

### ResAccountChallengeRankInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| season_info | [ResAccountChallengeRankInfo.ChallengeRank](#lq-ResAccountChallengeRankInfo-ChallengeRank) | repeated |  |






<a name="lq-ResAccountChallengeRankInfo-ChallengeRank"></a>

### ResAccountChallengeRankInfo.ChallengeRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ResAccountCharacterInfo"></a>

### ResAccountCharacterInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unlock_list | [uint32](#uint32) | repeated |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResAccountInfo"></a>

### ResAccountInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| account | [Account](#lq-Account) |  |  |
| room | [Room](#lq-Room) |  |  |






<a name="lq-ResAccountSettings"></a>

### ResAccountSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| settings | [AccountSetting](#lq-AccountSetting) | repeated |  |






<a name="lq-ResAccountStates"></a>

### ResAccountStates



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| states | [AccountActiveState](#lq-AccountActiveState) | repeated |  |






<a name="lq-ResAccountStatisticInfo"></a>

### ResAccountStatisticInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| statistic_data | [AccountStatisticData](#lq-AccountStatisticData) | repeated |  |
| detail_data | [AccountDetailStatisticV2](#lq-AccountDetailStatisticV2) |  |  |






<a name="lq-ResAchievement"></a>

### ResAchievement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| progresses | [AchievementProgress](#lq-AchievementProgress) | repeated |  |
| rewarded_group | [uint32](#uint32) | repeated |  |






<a name="lq-ResActivityBuff"></a>

### ResActivityBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| buff_list | [ActivityBuffData](#lq-ActivityBuffData) | repeated |  |






<a name="lq-ResActivityList"></a>

### ResActivityList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| activities | [Activity](#lq-Activity) | repeated |  |






<a name="lq-ResAddCollectedGameRecord"></a>

### ResAddCollectedGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResAllcommonViews"></a>

### ResAllcommonViews



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| views | [ResAllcommonViews.Views](#lq-ResAllcommonViews-Views) | repeated |  |
| use | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResAllcommonViews-Views"></a>

### ResAllcommonViews.Views



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| values | [ViewSlot](#lq-ViewSlot) | repeated |  |
| index | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |






<a name="lq-ResAmuletActivityFetchBrief"></a>

### ResAmuletActivityFetchBrief



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| upgrade | [ActivityAmuletUpgradeData](#lq-ActivityAmuletUpgradeData) |  |  |
| illustrated_book | [ActivityAmuletIllustratedBookData](#lq-ActivityAmuletIllustratedBookData) |  |  |
| game_records | [ActivityAmuletGameRecordData](#lq-ActivityAmuletGameRecordData) | repeated |  |
| statistic | [ActivityAmuletStatisticData](#lq-ActivityAmuletStatisticData) |  |  |






<a name="lq-ResAmuletActivityFetchInfo"></a>

### ResAmuletActivityFetchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| data | [ActivityAmuletData](#lq-ActivityAmuletData) |  |  |






<a name="lq-ResAmuletActivityMaintainInfo"></a>

### ResAmuletActivityMaintainInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| mode | [string](#string) |  |  |






<a name="lq-ResAmuletEventResponse"></a>

### ResAmuletEventResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| events | [AmuletEventData](#lq-AmuletEventData) | repeated |  |






<a name="lq-ResAnnouncement"></a>

### ResAnnouncement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| announcements | [Announcement](#lq-Announcement) | repeated |  |
| sort | [uint32](#uint32) | repeated |  |
| read_list | [uint32](#uint32) | repeated |  |






<a name="lq-ResArenaReward"></a>

### ResArenaReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResArenaReward.RewardItem](#lq-ResArenaReward-RewardItem) | repeated |  |






<a name="lq-ResArenaReward-RewardItem"></a>

### ResArenaReward.RewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResBagInfo"></a>

### ResBagInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| bag | [Bag](#lq-Bag) |  |  |






<a name="lq-ResBingoActivityReceiveReward"></a>

### ResBingoActivityReceiveReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| execute_result | [ExecuteResult](#lq-ExecuteResult) | repeated |  |
| cards | [ActivityBingoCardData](#lq-ActivityBingoCardData) | repeated |  |






<a name="lq-ResBuyFestivalProposal"></a>

### ResBuyFestivalProposal



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| new_proposal | [FestivalProposalData](#lq-FestivalProposalData) |  |  |






<a name="lq-ResBuyFromChestShop"></a>

### ResBuyFromChestShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| consume_count | [uint32](#uint32) |  |  |
| faith_count | [int32](#int32) |  |  |






<a name="lq-ResBuyFromShop"></a>

### ResBuyFromShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-ResChallengeLeaderboard"></a>

### ResChallengeLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResChallengeLeaderboard.Item](#lq-ResChallengeLeaderboard-Item) | repeated |  |
| self_rank | [uint32](#uint32) |  |  |






<a name="lq-ResChallengeLeaderboard-Item"></a>

### ResChallengeLeaderboard.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |






<a name="lq-ResChallengeSeasonInfo"></a>

### ResChallengeSeasonInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| challenge_season_list | [ResChallengeSeasonInfo.ChallengeInfo](#lq-ResChallengeSeasonInfo-ChallengeInfo) | repeated |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResChallengeSeasonInfo-ChallengeInfo"></a>

### ResChallengeSeasonInfo.ChallengeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season_id | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| state | [uint32](#uint32) |  |  |






<a name="lq-ResChangeCollectedGameRecordRemarks"></a>

### ResChangeCollectedGameRecordRemarks



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResCharacterInfo"></a>

### ResCharacterInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| characters | [Character](#lq-Character) | repeated |  |
| skins | [uint32](#uint32) | repeated |  |
| main_character_id | [uint32](#uint32) |  |  |
| send_gift_count | [uint32](#uint32) |  |  |
| send_gift_limit | [uint32](#uint32) |  |  |
| finished_endings | [uint32](#uint32) | repeated |  |
| rewarded_endings | [uint32](#uint32) | repeated |  |
| character_sort | [uint32](#uint32) | repeated |  |
| hidden_characters | [uint32](#uint32) | repeated |  |
| other_character_sort | [uint32](#uint32) | repeated |  |






<a name="lq-ResClientValue"></a>

### ResClientValue



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| datas | [ResClientValue.Value](#lq-ResClientValue-Value) | repeated |  |
| recharged_count | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResClientValue-Value"></a>

### ResClientValue.Value



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-ResCollectedGameRecordList"></a>

### ResCollectedGameRecordList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| record_list | [RecordCollectedData](#lq-RecordCollectedData) | repeated |  |
| record_collect_limit | [uint32](#uint32) |  |  |






<a name="lq-ResCombiningRecycleCraft"></a>

### ResCombiningRecycleCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResCommentSetting"></a>

### ResCommentSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| comment_allow | [uint32](#uint32) |  |  |






<a name="lq-ResCommonView"></a>

### ResCommonView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| slots | [ResCommonView.Slot](#lq-ResCommonView-Slot) | repeated |  |






<a name="lq-ResCommonView-Slot"></a>

### ResCommonView.Slot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| slot | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-ResCommonViews"></a>

### ResCommonViews



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| views | [ViewSlot](#lq-ViewSlot) | repeated |  |
| error | [Error](#lq-Error) |  |  |
| name | [string](#string) |  |  |






<a name="lq-ResCompleteActivityFlipTaskBatch"></a>

### ResCompleteActivityFlipTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| total_rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResCompleteSegmentTaskReward"></a>

### ResCompleteSegmentTaskReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResCompleteVillageTask"></a>

### ResCompleteVillageTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResConnectionInfo"></a>

### ResConnectionInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| client_endpoint | [NetworkEndpoint](#lq-NetworkEndpoint) |  |  |






<a name="lq-ResCreateAlipayAppOrder"></a>

### ResCreateAlipayAppOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| alipay_url | [string](#string) |  |  |






<a name="lq-ResCreateAlipayOrder"></a>

### ResCreateAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| alipay_url | [string](#string) |  |  |






<a name="lq-ResCreateAlipayScanOrder"></a>

### ResCreateAlipayScanOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| qrcode_buffer | [string](#string) |  |  |
| order_id | [string](#string) |  |  |
| qr_code | [string](#string) |  |  |






<a name="lq-ResCreateBillingOrder"></a>

### ResCreateBillingOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateCustomizedContest"></a>

### ResCreateCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| unique_id | [uint32](#uint32) |  |  |






<a name="lq-ResCreateDmmOrder"></a>

### ResCreateDmmOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |
| transaction_id | [string](#string) |  |  |
| dmm_user_id | [string](#string) |  |  |
| token | [string](#string) |  |  |
| callback_url | [string](#string) |  |  |
| request_time | [string](#string) |  |  |
| dmm_app_id | [string](#string) |  |  |






<a name="lq-ResCreateENAlipayOrder"></a>

### ResCreateENAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateENJCBOrder"></a>

### ResCreateENJCBOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateENMasterCardOrder"></a>

### ResCreateENMasterCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateENPaypalOrder"></a>

### ResCreateENPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateENVisaOrder"></a>

### ResCreateENVisaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateGameObserveAuth"></a>

### ResCreateGameObserveAuth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| token | [string](#string) |  |  |
| location | [string](#string) |  |  |






<a name="lq-ResCreateIAPOrder"></a>

### ResCreateIAPOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPAuOrder"></a>

### ResCreateJPAuOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPCreditCardOrder"></a>

### ResCreateJPCreditCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPDocomoOrder"></a>

### ResCreateJPDocomoOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPGMOOrder"></a>

### ResCreateJPGMOOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPPayPayOrder"></a>

### ResCreateJPPayPayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPPaypalOrder"></a>

### ResCreateJPPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPSoftbankOrder"></a>

### ResCreateJPSoftbankOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateJPWebMoneyOrder"></a>

### ResCreateJPWebMoneyOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateKRAlipayOrder"></a>

### ResCreateKRAlipayOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateKRJCBOrder"></a>

### ResCreateKRJCBOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateKRMasterCardOrder"></a>

### ResCreateKRMasterCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateKRPaypalOrder"></a>

### ResCreateKRPaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateKRVisaOrder"></a>

### ResCreateKRVisaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateMyCardOrder"></a>

### ResCreateMyCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| auth_code | [string](#string) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreatePaypalOrder"></a>

### ResCreatePaypalOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |
| url | [string](#string) |  |  |






<a name="lq-ResCreateRoom"></a>

### ResCreateRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| room | [Room](#lq-Room) |  |  |






<a name="lq-ResCreateSeerReport"></a>

### ResCreateSeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| seer_report | [SeerBrief](#lq-SeerBrief) |  |  |






<a name="lq-ResCreateSteamOrder"></a>

### ResCreateSteamOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |
| platform_order_id | [string](#string) |  |  |






<a name="lq-ResCreateWechatAppOrder"></a>

### ResCreateWechatAppOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| call_wechat_app_param | [ResCreateWechatAppOrder.CallWechatAppParam](#lq-ResCreateWechatAppOrder-CallWechatAppParam) |  |  |






<a name="lq-ResCreateWechatAppOrder-CallWechatAppParam"></a>

### ResCreateWechatAppOrder.CallWechatAppParam



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| appid | [string](#string) |  |  |
| partnerid | [string](#string) |  |  |
| prepayid | [string](#string) |  |  |
| package | [string](#string) |  |  |
| noncestr | [string](#string) |  |  |
| timestamp | [string](#string) |  |  |
| sign | [string](#string) |  |  |






<a name="lq-ResCreateWechatNativeOrder"></a>

### ResCreateWechatNativeOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| qrcode_buffer | [string](#string) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateXsollaOrder"></a>

### ResCreateXsollaOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |
| url | [string](#string) |  |  |






<a name="lq-ResCreateYostarOrder"></a>

### ResCreateYostarOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResCreateYostarV4SDKOrder"></a>

### ResCreateYostarV4SDKOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| order_id | [string](#string) |  |  |
| notify_url | [string](#string) |  |  |
| extra_data | [string](#string) |  |  |






<a name="lq-ResCurrentMatchInfo"></a>

### ResCurrentMatchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| matches | [ResCurrentMatchInfo.CurrentMatchInfo](#lq-ResCurrentMatchInfo-CurrentMatchInfo) | repeated |  |






<a name="lq-ResCurrentMatchInfo-CurrentMatchInfo"></a>

### ResCurrentMatchInfo.CurrentMatchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode_id | [uint32](#uint32) |  |  |
| playing_count | [uint32](#uint32) |  |  |






<a name="lq-ResDMMPreLogin"></a>

### ResDMMPreLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| parameter | [string](#string) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResDailySignInInfo"></a>

### ResDailySignInInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| sign_in_days | [uint32](#uint32) |  |  |






<a name="lq-ResDailyTask"></a>

### ResDailyTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| has_refresh_count | [bool](#bool) |  |  |
| max_daily_task_count | [uint32](#uint32) |  |  |
| refresh_count | [uint32](#uint32) |  |  |






<a name="lq-ResDeleteAccount"></a>

### ResDeleteAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| delete_time | [uint32](#uint32) |  |  |






<a name="lq-ResDigMine"></a>

### ResDigMine



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| map | [MineReward](#lq-MineReward) | repeated |  |
| reward | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-ResDoActivitySignIn"></a>

### ResDoActivitySignIn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ResDoActivitySignIn.RewardData](#lq-ResDoActivitySignIn-RewardData) | repeated |  |
| sign_in_count | [uint32](#uint32) |  |  |






<a name="lq-ResDoActivitySignIn-RewardData"></a>

### ResDoActivitySignIn.RewardData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResEnterCustomizedContest"></a>

### ResEnterCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| detail_info | [CustomizedContestDetail](#lq-CustomizedContestDetail) |  |  |
| player_report | [CustomizedContestPlayerReport](#lq-CustomizedContestPlayerReport) |  |  |
| is_followed | [bool](#bool) |  |  |
| state | [uint32](#uint32) |  |  |
| is_admin | [bool](#bool) |  |  |
| game_plan | [CustomizedContestGamePlan](#lq-CustomizedContestGamePlan) |  |  |
| disable_chat_room | [bool](#bool) |  |  |






<a name="lq-ResExchangeActivityItem"></a>

### ResExchangeActivityItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| execute_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResFastLogin"></a>

### ResFastLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| game_info | [GameConnectInfo](#lq-GameConnectInfo) |  |  |
| room | [Room](#lq-Room) |  |  |






<a name="lq-ResFeedActivityFeed"></a>

### ResFeedActivityFeed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResFeedActivityFeed.RewardItem](#lq-ResFeedActivityFeed-RewardItem) | repeated |  |
| feed_count | [uint32](#uint32) |  |  |






<a name="lq-ResFeedActivityFeed-RewardItem"></a>

### ResFeedActivityFeed.RewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchABMatch"></a>

### ResFetchABMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| match_id | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| buy_in_count | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |
| rewarded | [bool](#bool) |  |  |
| match_max_point | [ResFetchABMatch.MatchPoint](#lq-ResFetchABMatch-MatchPoint) | repeated |  |
| quit | [bool](#bool) |  |  |






<a name="lq-ResFetchABMatch-MatchPoint"></a>

### ResFetchABMatch.MatchPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-ResFetchAccountGameHuRecords"></a>

### ResFetchAccountGameHuRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| records | [ResFetchAccountGameHuRecords.GameHuRecords](#lq-ResFetchAccountGameHuRecords-GameHuRecords) | repeated |  |






<a name="lq-ResFetchAccountGameHuRecords-GameHuRecords"></a>

### ResFetchAccountGameHuRecords.GameHuRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |
| hands | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| hupai | [string](#string) |  |  |
| hu_fans | [uint32](#uint32) | repeated |  |






<a name="lq-ResFetchAccountInfoExtra"></a>

### ResFetchAccountInfoExtra



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| recent_games | [ResFetchAccountInfoExtra.AccountInfoGameRecord](#lq-ResFetchAccountInfoExtra-AccountInfoGameRecord) | repeated |  |
| hu_type_details | [ResFetchAccountInfoExtra.GameHuTypeDetail](#lq-ResFetchAccountInfoExtra-GameHuTypeDetail) | repeated |  |
| game_rank_details | [ResFetchAccountInfoExtra.AccountGameRankDetail](#lq-ResFetchAccountInfoExtra-AccountGameRankDetail) | repeated |  |






<a name="lq-ResFetchAccountInfoExtra-AccountGameRankDetail"></a>

### ResFetchAccountInfoExtra.AccountGameRankDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchAccountInfoExtra-AccountInfoGameRecord"></a>

### ResFetchAccountInfoExtra.AccountInfoGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| tag | [uint32](#uint32) |  |  |
| sub_tag | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| final_point | [uint32](#uint32) |  |  |
| results | [ResFetchAccountInfoExtra.AccountInfoGameRecord.AccountGameResult](#lq-ResFetchAccountInfoExtra-AccountInfoGameRecord-AccountGameResult) | repeated |  |






<a name="lq-ResFetchAccountInfoExtra-AccountInfoGameRecord-AccountGameResult"></a>

### ResFetchAccountInfoExtra.AccountInfoGameRecord.AccountGameResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| verified | [uint32](#uint32) |  |  |
| grading_score | [int32](#int32) |  |  |
| final_point | [int32](#int32) |  |  |
| seat | [uint32](#uint32) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |






<a name="lq-ResFetchAccountInfoExtra-GameHuTypeDetail"></a>

### ResFetchAccountInfoExtra.GameHuTypeDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchAchievementRate"></a>

### ResFetchAchievementRate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rate | [ResFetchAchievementRate.AchievementRate](#lq-ResFetchAchievementRate-AchievementRate) | repeated |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResFetchAchievementRate-AchievementRate"></a>

### ResFetchAchievementRate.AchievementRate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| rate | [uint32](#uint32) |  |  |






<a name="lq-ResFetchActivityFlipInfo"></a>

### ResFetchActivityFlipInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rewards | [uint32](#uint32) | repeated |  |
| count | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResFetchActivityInterval"></a>

### ResFetchActivityInterval



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result | [ResFetchActivityInterval.ActivityInterval](#lq-ResFetchActivityInterval-ActivityInterval) | repeated |  |






<a name="lq-ResFetchActivityInterval-ActivityInterval"></a>

### ResFetchActivityInterval.ActivityInterval



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| interval | [uint32](#uint32) |  |  |






<a name="lq-ResFetchActivityRank"></a>

### ResFetchActivityRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResFetchActivityRank.ActivityRankItem](#lq-ResFetchActivityRank-ActivityRankItem) | repeated |  |
| self | [ResFetchActivityRank.ActivityRankItem](#lq-ResFetchActivityRank-ActivityRankItem) |  |  |






<a name="lq-ResFetchActivityRank-ActivityRankItem"></a>

### ResFetchActivityRank.ActivityRankItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| score | [uint64](#uint64) |  |  |
| data | [string](#string) |  |  |
| rank | [uint32](#uint32) |  |  |






<a name="lq-ResFetchAmuletActivityData"></a>

### ResFetchAmuletActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| data | [ActivityAmuletData](#lq-ActivityAmuletData) |  |  |






<a name="lq-ResFetchAnnualReportInfo"></a>

### ResFetchAnnualReportInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchBannerActivityData"></a>

### ResFetchBannerActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| activity_list | [BannerActivityData](#lq-BannerActivityData) | repeated |  |






<a name="lq-ResFetchBingoActivityData"></a>

### ResFetchBingoActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| data | [ActivityBingoData](#lq-ActivityBingoData) |  |  |






<a name="lq-ResFetchChallengeInfo"></a>

### ResFetchChallengeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| task_progress | [TaskProgress](#lq-TaskProgress) | repeated |  |
| refresh_count | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |
| rewarded_season | [uint32](#uint32) | repeated |  |






<a name="lq-ResFetchCommentContent"></a>

### ResFetchCommentContent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| comments | [CommentItem](#lq-CommentItem) | repeated |  |






<a name="lq-ResFetchCommentList"></a>

### ResFetchCommentList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| comment_allow | [uint32](#uint32) |  |  |
| comment_id_list | [uint32](#uint32) | repeated |  |
| last_read_id | [uint32](#uint32) |  |  |






<a name="lq-ResFetchContestPlayerRank"></a>

### ResFetchContestPlayerRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| total | [uint32](#uint32) |  |  |
| rank | [ResFetchContestPlayerRank.SeasonRank](#lq-ResFetchContestPlayerRank-SeasonRank) | repeated |  |
| player_data | [ResFetchContestPlayerRank.PlayerData](#lq-ResFetchContestPlayerRank-PlayerData) |  |  |






<a name="lq-ResFetchContestPlayerRank-ContestPlayerAccountData"></a>

### ResFetchContestPlayerRank.ContestPlayerAccountData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_game_count | [uint32](#uint32) |  |  |
| recent_games | [ResFetchContestPlayerRank.ContestPlayerAccountData.ContestGameResult](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestGameResult) | repeated |  |
| highest_series_points | [ResFetchContestPlayerRank.ContestPlayerAccountData.ContestSeriesGameResult](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestSeriesGameResult) | repeated |  |
| accumulate_point | [int32](#int32) |  |  |






<a name="lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestGameResult"></a>

### ResFetchContestPlayerRank.ContestPlayerAccountData.ContestGameResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| total_point | [int32](#int32) |  |  |






<a name="lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestSeriesGameResult"></a>

### ResFetchContestPlayerRank.ContestPlayerAccountData.ContestSeriesGameResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| results | [ResFetchContestPlayerRank.ContestPlayerAccountData.ContestGameResult](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData-ContestGameResult) | repeated |  |






<a name="lq-ResFetchContestPlayerRank-PlayerData"></a>

### ResFetchContestPlayerRank.PlayerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| data | [ResFetchContestPlayerRank.ContestPlayerAccountData](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData) |  |  |
| team_name | [string](#string) |  |  |
| modify_score | [int32](#int32) |  |  |
| rank_percent | [uint32](#uint32) |  |  |






<a name="lq-ResFetchContestPlayerRank-SeasonRank"></a>

### ResFetchContestPlayerRank.SeasonRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| data | [ResFetchContestPlayerRank.ContestPlayerAccountData](#lq-ResFetchContestPlayerRank-ContestPlayerAccountData) |  |  |
| team_name | [string](#string) |  |  |
| modify_score | [int32](#int32) |  |  |
| rank | [uint32](#uint32) |  |  |
| rank_percent | [uint32](#uint32) |  |  |






<a name="lq-ResFetchContestTeamMember"></a>

### ResFetchContestTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| total | [uint32](#uint32) |  |  |
| rank | [ResFetchContestTeamMember.ContestTeamMemberRank](#lq-ResFetchContestTeamMember-ContestTeamMemberRank) | repeated |  |






<a name="lq-ResFetchContestTeamMember-ContestTeamMemberRank"></a>

### ResFetchContestTeamMember.ContestTeamMemberRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| total_game_count | [uint32](#uint32) |  |  |
| total_score | [int32](#int32) |  |  |
| nickname | [string](#string) |  |  |






<a name="lq-ResFetchContestTeamRank"></a>

### ResFetchContestTeamRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| total | [uint32](#uint32) |  |  |
| rank | [ResFetchContestTeamRank.SeasonTeamRank](#lq-ResFetchContestTeamRank-SeasonTeamRank) | repeated |  |
| self_team_rank | [ResFetchContestTeamRank.SeasonTeamRank](#lq-ResFetchContestTeamRank-SeasonTeamRank) |  |  |






<a name="lq-ResFetchContestTeamRank-ContestTeamData"></a>

### ResFetchContestTeamRank.ContestTeamData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_point | [int32](#int32) |  |  |
| total_game_count | [uint32](#uint32) |  |  |
| member_count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchContestTeamRank-SeasonTeamRank"></a>

### ResFetchContestTeamRank.SeasonTeamRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| team_id | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| data | [ResFetchContestTeamRank.ContestTeamData](#lq-ResFetchContestTeamRank-ContestTeamData) |  |  |
| rank | [uint32](#uint32) |  |  |
| rank_percent | [uint32](#uint32) |  |  |






<a name="lq-ResFetchCustomizedContestAuthInfo"></a>

### ResFetchCustomizedContestAuthInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| observer_level | [uint32](#uint32) |  |  |






<a name="lq-ResFetchCustomizedContestByContestId"></a>

### ResFetchCustomizedContestByContestId



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| contest_info | [CustomizedContestAbstract](#lq-CustomizedContestAbstract) |  |  |






<a name="lq-ResFetchCustomizedContestGameLiveList"></a>

### ResFetchCustomizedContestGameLiveList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| live_list | [GameLiveHead](#lq-GameLiveHead) | repeated |  |






<a name="lq-ResFetchCustomizedContestGameRecords"></a>

### ResFetchCustomizedContestGameRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| next_index | [uint32](#uint32) |  |  |
| record_list | [RecordGame](#lq-RecordGame) | repeated |  |






<a name="lq-ResFetchCustomizedContestList"></a>

### ResFetchCustomizedContestList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| contests | [CustomizedContestBase](#lq-CustomizedContestBase) | repeated |  |
| follow_contests | [CustomizedContestBase](#lq-CustomizedContestBase) | repeated |  |






<a name="lq-ResFetchCustomizedContestOnlineInfo"></a>

### ResFetchCustomizedContestOnlineInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| online_player | [uint32](#uint32) |  |  |






<a name="lq-ResFetchDailySignActivityData"></a>

### ResFetchDailySignActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| activity_list | [ResFetchDailySignActivityData.DailySignActivityData](#lq-ResFetchDailySignActivityData-DailySignActivityData) | repeated |  |






<a name="lq-ResFetchDailySignActivityData-DailySignActivityData"></a>

### ResFetchDailySignActivityData.DailySignActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| days | [ResFetchDailySignActivityData.DailySignActivityDay](#lq-ResFetchDailySignActivityData-DailySignActivityDay) | repeated |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ResFetchDailySignActivityData-DailySignActivityDay"></a>

### ResFetchDailySignActivityData.DailySignActivityDay



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| day | [uint32](#uint32) |  |  |
| rewards | [ResFetchDailySignActivityData.DailySignActivityReward](#lq-ResFetchDailySignActivityData-DailySignActivityReward) | repeated |  |






<a name="lq-ResFetchDailySignActivityData-DailySignActivityReward"></a>

### ResFetchDailySignActivityData.DailySignActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchFriendGiftActivityData"></a>

### ResFetchFriendGiftActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| list | [ResFetchFriendGiftActivityData.FriendData](#lq-ResFetchFriendGiftActivityData-FriendData) | repeated |  |






<a name="lq-ResFetchFriendGiftActivityData-FriendData"></a>

### ResFetchFriendGiftActivityData.FriendData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| items | [ResFetchFriendGiftActivityData.ItemCountData](#lq-ResFetchFriendGiftActivityData-ItemCountData) | repeated |  |
| receive_count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchFriendGiftActivityData-ItemCountData"></a>

### ResFetchFriendGiftActivityData.ItemCountData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResFetchGamingInfo"></a>

### ResFetchGamingInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| game_info | [GameConnectInfo](#lq-GameConnectInfo) |  |  |






<a name="lq-ResFetchInfo"></a>

### ResFetchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| server_time | [ResServerTime](#lq-ResServerTime) |  |  |
| server_setting | [ResServerSettings](#lq-ResServerSettings) |  |  |
| client_value | [ResClientValue](#lq-ResClientValue) |  |  |
| friend_list | [ResFriendList](#lq-ResFriendList) |  |  |
| friend_apply_list | [ResFriendApplyList](#lq-ResFriendApplyList) |  |  |
| recent_friend | [ResFetchrecentFriend](#lq-ResFetchrecentFriend) |  |  |
| mail_info | [ResMailInfo](#lq-ResMailInfo) |  |  |
| receive_coin_info | [ResReviveCoinInfo](#lq-ResReviveCoinInfo) |  |  |
| title_list | [ResTitleList](#lq-ResTitleList) |  |  |
| bag_info | [ResBagInfo](#lq-ResBagInfo) |  |  |
| shop_info | [ResShopInfo](#lq-ResShopInfo) |  |  |
| shop_interval | [ResFetchShopInterval](#lq-ResFetchShopInterval) |  |  |
| activity_data | [ResAccountActivityData](#lq-ResAccountActivityData) |  |  |
| activity_interval | [ResFetchActivityInterval](#lq-ResFetchActivityInterval) |  |  |
| activity_buff | [ResActivityBuff](#lq-ResActivityBuff) |  |  |
| vip_reward | [ResVipReward](#lq-ResVipReward) |  |  |
| month_ticket_info | [ResMonthTicketInfo](#lq-ResMonthTicketInfo) |  |  |
| achievement | [ResAchievement](#lq-ResAchievement) |  |  |
| comment_setting | [ResCommentSetting](#lq-ResCommentSetting) |  |  |
| account_settings | [ResAccountSettings](#lq-ResAccountSettings) |  |  |
| mod_nickname_time | [ResModNicknameTime](#lq-ResModNicknameTime) |  |  |
| misc | [ResMisc](#lq-ResMisc) |  |  |
| announcement | [ResAnnouncement](#lq-ResAnnouncement) |  |  |
| activity_list | [ResActivityList](#lq-ResActivityList) |  |  |
| character_info | [ResCharacterInfo](#lq-ResCharacterInfo) |  |  |
| all_common_views | [ResAllcommonViews](#lq-ResAllcommonViews) |  |  |
| collected_game_record_list | [ResCollectedGameRecordList](#lq-ResCollectedGameRecordList) |  |  |
| maintain_notice | [ResFetchMaintainNotice](#lq-ResFetchMaintainNotice) |  |  |
| random_character | [ResRandomCharacter](#lq-ResRandomCharacter) |  |  |
| maintenance_info | [ResFetchServerMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo) |  |  |
| seer_info | [ResFetchSeerInfo](#lq-ResFetchSeerInfo) |  |  |
| annual_report_info | [ResFetchAnnualReportInfo](#lq-ResFetchAnnualReportInfo) |  |  |






<a name="lq-ResFetchJPCommonCreditCardOrder"></a>

### ResFetchJPCommonCreditCardOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResFetchLastPrivacy"></a>

### ResFetchLastPrivacy



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| privacy | [ResFetchLastPrivacy.PrivacyInfo](#lq-ResFetchLastPrivacy-PrivacyInfo) | repeated |  |






<a name="lq-ResFetchLastPrivacy-PrivacyInfo"></a>

### ResFetchLastPrivacy.PrivacyInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| version | [string](#string) |  |  |






<a name="lq-ResFetchMaintainNotice"></a>

### ResFetchMaintainNotice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| notice | [MaintainNotice](#lq-MaintainNotice) |  |  |






<a name="lq-ResFetchManagerCustomizedContest"></a>

### ResFetchManagerCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| name | [string](#string) |  |  |
| open_show | [uint32](#uint32) |  |  |
| game_rule_setting | [GameMode](#lq-GameMode) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| auto_match | [uint32](#uint32) |  |  |
| rank_rule | [uint32](#uint32) |  |  |
| check_state | [uint32](#uint32) |  |  |
| checking_name | [string](#string) |  |  |
| contest_setting | [ContestSetting](#lq-ContestSetting) |  |  |
| rank_type | [uint32](#uint32) |  |  |
| season | [ResFetchManagerCustomizedContest.SeasonInfo](#lq-ResFetchManagerCustomizedContest-SeasonInfo) |  |  |
| match_start_time | [uint32](#uint32) |  |  |
| match_end_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchManagerCustomizedContest-SeasonInfo"></a>

### ResFetchManagerCustomizedContest.SeasonInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| create_time | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchManagerCustomizedContestList"></a>

### ResFetchManagerCustomizedContestList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| contests | [CustomizedContestBase](#lq-CustomizedContestBase) | repeated |  |






<a name="lq-ResFetchOBToken"></a>

### ResFetchOBToken



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| token | [string](#string) |  |  |
| create_time | [uint32](#uint32) |  |  |
| delay | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchOauth2"></a>

### ResFetchOauth2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| openid | [string](#string) |  |  |






<a name="lq-ResFetchPhoneLoginBind"></a>

### ResFetchPhoneLoginBind



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| phone_login | [uint32](#uint32) |  |  |






<a name="lq-ResFetchProgressRewardActivityInfo"></a>

### ResFetchProgressRewardActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| progress | [uint32](#uint32) |  |  |






<a name="lq-ResFetchQuestionnaireDetail"></a>

### ResFetchQuestionnaireDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| detail | [QuestionnaireDetail](#lq-QuestionnaireDetail) |  |  |






<a name="lq-ResFetchQuestionnaireList"></a>

### ResFetchQuestionnaireList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| list | [QuestionnaireBrief](#lq-QuestionnaireBrief) | repeated |  |
| finished_list | [uint32](#uint32) | repeated |  |






<a name="lq-ResFetchQueueInfo"></a>

### ResFetchQueueInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| remain | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |






<a name="lq-ResFetchRPGBattleHistory"></a>

### ResFetchRPGBattleHistory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| battle_result | [ResFetchRPGBattleHistory.BattleResult](#lq-ResFetchRPGBattleHistory-BattleResult) | repeated |  |
| start_state | [RPGState](#lq-RPGState) |  |  |
| current_state | [RPGState](#lq-RPGState) |  |  |






<a name="lq-ResFetchRPGBattleHistory-BattleResult"></a>

### ResFetchRPGBattleHistory.BattleResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| target | [uint32](#uint32) |  |  |
| damage | [uint32](#uint32) |  |  |
| heal | [uint32](#uint32) |  |  |
| monster_seq | [uint32](#uint32) |  |  |
| chain_atk | [uint32](#uint32) |  |  |
| killed | [uint32](#uint32) |  |  |
| is_luk | [uint32](#uint32) |  |  |
| is_dex | [uint32](#uint32) |  |  |
| is_extra | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| uuid | [string](#string) |  |  |
| points | [uint32](#uint32) |  |  |
| is_zimo | [uint32](#uint32) |  |  |






<a name="lq-ResFetchRPGBattleHistoryV2"></a>

### ResFetchRPGBattleHistoryV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| battle_result | [ResFetchRPGBattleHistoryV2.BattleResultV2](#lq-ResFetchRPGBattleHistoryV2-BattleResultV2) | repeated |  |
| start_state | [RPGState](#lq-RPGState) |  |  |
| current_state | [RPGState](#lq-RPGState) |  |  |
| recent_battle_result | [ResFetchRPGBattleHistoryV2.BattleResultV2](#lq-ResFetchRPGBattleHistoryV2-BattleResultV2) | repeated |  |






<a name="lq-ResFetchRPGBattleHistoryV2-BattleResultV2"></a>

### ResFetchRPGBattleHistoryV2.BattleResultV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| damage | [uint32](#uint32) |  |  |
| monster_seq | [uint32](#uint32) |  |  |
| killed | [uint32](#uint32) |  |  |
| buff | [ActivityBuffData](#lq-ActivityBuffData) | repeated |  |
| points | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |






<a name="lq-ResFetchRankPointLeaderboard"></a>

### ResFetchRankPointLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResFetchRankPointLeaderboard.Item](#lq-ResFetchRankPointLeaderboard-Item) | repeated |  |
| last_refresh_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchRankPointLeaderboard-Item"></a>

### ResFetchRankPointLeaderboard.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| view | [PlayerBaseView](#lq-PlayerBaseView) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-ResFetchReadyPlayerList"></a>

### ResFetchReadyPlayerList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| list | [ResFetchReadyPlayerList.Player](#lq-ResFetchReadyPlayerList-Player) | repeated |  |






<a name="lq-ResFetchReadyPlayerList-Player"></a>

### ResFetchReadyPlayerList.Player



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| team_name | [string](#string) |  |  |






<a name="lq-ResFetchRefundOrder"></a>

### ResFetchRefundOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| orders | [ResFetchRefundOrder.OrderInfo](#lq-ResFetchRefundOrder-OrderInfo) | repeated |  |
| clear_deadline | [uint32](#uint32) |  |  |
| message | [I18nContext](#lq-I18nContext) | repeated |  |






<a name="lq-ResFetchRefundOrder-OrderInfo"></a>

### ResFetchRefundOrder.OrderInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success_time | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| cleared | [uint32](#uint32) |  |  |
| order_id | [string](#string) |  |  |






<a name="lq-ResFetchRollingNotice"></a>

### ResFetchRollingNotice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| notice | [RollingNotice](#lq-RollingNotice) |  |  |






<a name="lq-ResFetchSeerInfo"></a>

### ResFetchSeerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| remain_count | [uint32](#uint32) |  |  |
| date_limit | [uint32](#uint32) |  |  |
| expire_time | [uint32](#uint32) |  |  |






<a name="lq-ResFetchSeerReport"></a>

### ResFetchSeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| report | [SeerReport](#lq-SeerReport) |  |  |






<a name="lq-ResFetchSeerReportList"></a>

### ResFetchSeerReportList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| seer_report_list | [SeerBrief](#lq-SeerBrief) | repeated |  |






<a name="lq-ResFetchSelfGamePointRank"></a>

### ResFetchSelfGamePointRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| self_rate | [uint32](#uint32) |  |  |






<a name="lq-ResFetchServerMaintenanceInfo"></a>

### ResFetchServerMaintenanceInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| function_maintenance | [ResFetchServerMaintenanceInfo.ServerFunctionMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo-ServerFunctionMaintenanceInfo) | repeated |  |
| activity_maintenance | [ResFetchServerMaintenanceInfo.ServerActivityMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo-ServerActivityMaintenanceInfo) | repeated |  |






<a name="lq-ResFetchServerMaintenanceInfo-ServerActivityMaintenanceInfo"></a>

### ResFetchServerMaintenanceInfo.ServerActivityMaintenanceInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_type | [string](#string) |  |  |
| open | [bool](#bool) |  |  |






<a name="lq-ResFetchServerMaintenanceInfo-ServerFunctionMaintenanceInfo"></a>

### ResFetchServerMaintenanceInfo.ServerFunctionMaintenanceInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| open | [bool](#bool) |  |  |






<a name="lq-ResFetchShopInterval"></a>

### ResFetchShopInterval



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result | [ResFetchShopInterval.ShopInterval](#lq-ResFetchShopInterval-ShopInterval) | repeated |  |






<a name="lq-ResFetchShopInterval-ShopInterval"></a>

### ResFetchShopInterval.ShopInterval



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| interval | [uint32](#uint32) |  |  |






<a name="lq-ResFetchSimulationGameRank"></a>

### ResFetchSimulationGameRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rank | [ResFetchSimulationGameRank.RankInfo](#lq-ResFetchSimulationGameRank-RankInfo) | repeated |  |






<a name="lq-ResFetchSimulationGameRank-RankInfo"></a>

### ResFetchSimulationGameRank.RankInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character | [uint32](#uint32) |  |  |
| score | [float](#float) |  |  |






<a name="lq-ResFetchSimulationGameRecord"></a>

### ResFetchSimulationGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| messages | [ActivitySimulationGameRecordMessage](#lq-ActivitySimulationGameRecordMessage) | repeated |  |






<a name="lq-ResFetchVoteActivity"></a>

### ResFetchVoteActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| update_time | [uint32](#uint32) |  |  |
| data | [ResFetchVoteActivity.VoteRankData](#lq-ResFetchVoteActivity-VoteRankData) | repeated |  |






<a name="lq-ResFetchVoteActivity-VoteRankData"></a>

### ResFetchVoteActivity.VoteRankData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| share | [uint32](#uint32) |  |  |






<a name="lq-ResFetchrecentFriend"></a>

### ResFetchrecentFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| account_list | [uint32](#uint32) | repeated |  |






<a name="lq-ResFinishCombiningOrder"></a>

### ResFinishCombiningOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResFriendApplyList"></a>

### ResFriendApplyList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| applies | [ResFriendApplyList.FriendApply](#lq-ResFriendApplyList-FriendApply) | repeated |  |






<a name="lq-ResFriendApplyList-FriendApply"></a>

### ResFriendApplyList.FriendApply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| apply_time | [uint32](#uint32) |  |  |






<a name="lq-ResFriendList"></a>

### ResFriendList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| friends | [Friend](#lq-Friend) | repeated |  |
| friend_max_count | [uint32](#uint32) |  |  |
| friend_count | [uint32](#uint32) |  |  |






<a name="lq-ResGameLiveInfo"></a>

### ResGameLiveInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| left_start_seconds | [uint32](#uint32) |  |  |
| live_head | [GameLiveHead](#lq-GameLiveHead) |  |  |
| segments | [GameLiveSegmentUri](#lq-GameLiveSegmentUri) | repeated |  |
| now_millisecond | [uint32](#uint32) |  |  |






<a name="lq-ResGameLiveLeftSegment"></a>

### ResGameLiveLeftSegment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| live_state | [uint32](#uint32) |  |  |
| segments | [GameLiveSegmentUri](#lq-GameLiveSegmentUri) | repeated |  |
| now_millisecond | [uint32](#uint32) |  |  |
| segment_end_millisecond | [uint32](#uint32) |  |  |






<a name="lq-ResGameLiveList"></a>

### ResGameLiveList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| live_list | [GameLiveHead](#lq-GameLiveHead) | repeated |  |






<a name="lq-ResGamePointRank"></a>

### ResGamePointRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rank | [ResGamePointRank.RankInfo](#lq-ResGamePointRank-RankInfo) | repeated |  |
| self_rank | [uint32](#uint32) |  |  |






<a name="lq-ResGamePointRank-RankInfo"></a>

### ResGamePointRank.RankInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-ResGameRecord"></a>

### ResGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| head | [RecordGame](#lq-RecordGame) |  |  |
| data | [bytes](#bytes) |  |  |
| data_url | [string](#string) |  |  |






<a name="lq-ResGameRecordList"></a>

### ResGameRecordList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| total_count | [uint32](#uint32) |  |  |
| record_list | [RecordGame](#lq-RecordGame) | repeated |  |






<a name="lq-ResGameRecordListV2"></a>

### ResGameRecordListV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| iterator | [string](#string) |  |  |
| iterator_expire | [uint32](#uint32) |  |  |
| actual_begin_time | [uint32](#uint32) |  |  |
| actual_end_time | [uint32](#uint32) |  |  |






<a name="lq-ResGameRecordsDetail"></a>

### ResGameRecordsDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| record_list | [RecordGame](#lq-RecordGame) | repeated |  |






<a name="lq-ResGameRecordsDetailV2"></a>

### ResGameRecordsDetailV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| entries | [RecordListEntry](#lq-RecordListEntry) | repeated |  |






<a name="lq-ResGenerateAnnualReportToken"></a>

### ResGenerateAnnualReportToken



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| token | [string](#string) |  |  |
| url | [string](#string) |  |  |






<a name="lq-ResGenerateCombiningCraft"></a>

### ResGenerateCombiningCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| pos | [uint32](#uint32) |  |  |
| craft_id | [uint32](#uint32) |  |  |






<a name="lq-ResGenerateContestManagerLoginCode"></a>

### ResGenerateContestManagerLoginCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| code | [string](#string) |  |  |






<a name="lq-ResGetFriendVillageData"></a>

### ResGetFriendVillageData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| list | [ResGetFriendVillageData.FriendVillageData](#lq-ResGetFriendVillageData-FriendVillageData) | repeated |  |






<a name="lq-ResGetFriendVillageData-FriendVillageData"></a>

### ResGetFriendVillageData.FriendVillageData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ResIDCardInfo"></a>

### ResIDCardInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| is_authed | [bool](#bool) |  |  |
| country | [string](#string) |  |  |






<a name="lq-ResJoinCustomizedContestChatRoom"></a>

### ResJoinCustomizedContestChatRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| token | [string](#string) |  |  |






<a name="lq-ResJoinRoom"></a>

### ResJoinRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| room | [Room](#lq-Room) |  |  |






<a name="lq-ResLevelLeaderboard"></a>

### ResLevelLeaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResLevelLeaderboard.Item](#lq-ResLevelLeaderboard-Item) | repeated |  |
| self_rank | [uint32](#uint32) |  |  |






<a name="lq-ResLevelLeaderboard-Item"></a>

### ResLevelLeaderboard.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |






<a name="lq-ResLikeSNS"></a>

### ResLikeSNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| is_liked | [uint32](#uint32) |  |  |






<a name="lq-ResLogin"></a>

### ResLogin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| account_id | [uint32](#uint32) |  |  |
| account | [Account](#lq-Account) |  |  |
| game_info | [GameConnectInfo](#lq-GameConnectInfo) |  |  |
| has_unread_announcement | [bool](#bool) |  |  |
| access_token | [string](#string) |  |  |
| signup_time | [uint32](#uint32) |  |  |
| is_id_card_authed | [bool](#bool) |  |  |
| country | [string](#string) |  |  |
| logined_version | [uint32](#uint32) | repeated |  |
| rewarded_version | [uint32](#uint32) | repeated |  |






<a name="lq-ResLogout"></a>

### ResLogout



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResMMOActivityDebugSetTeamCandidate"></a>

### ResMMOActivityDebugSetTeamCandidate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMMOActivityEquipFusion"></a>

### ResMMOActivityEquipFusion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result | [uint32](#uint32) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMMOActivityFetchData"></a>

### ResMMOActivityFetchData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| mmo_data | [ActivityMMOData](#lq-ActivityMMOData) |  |  |






<a name="lq-ResMMOActivityFinishBattle"></a>

### ResMMOActivityFinishBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResMMOActivityReceiveSupportReward"></a>

### ResMMOActivityReceiveSupportReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |
| support_count | [uint32](#uint32) |  |  |
| total_support_count | [uint32](#uint32) |  |  |






<a name="lq-ResMMOActivitySetCharacter"></a>

### ResMMOActivitySetCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMMOActivitySetEquip"></a>

### ResMMOActivitySetEquip



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMMOActivitySetTeamMember"></a>

### ResMMOActivitySetTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMMOActivityStartBattle"></a>

### ResMMOActivityStartBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| actions | [ResMMOActivityStartBattle.MMOActivityBattleAction](#lq-ResMMOActivityStartBattle-MMOActivityBattleAction) | repeated |  |
| units | [ResMMOActivityStartBattle.MMOActivityBattleUnit](#lq-ResMMOActivityStartBattle-MMOActivityBattleUnit) | repeated |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |
| result | [uint32](#uint32) |  |  |






<a name="lq-ResMMOActivityStartBattle-MMOActivityBattleAction"></a>

### ResMMOActivityStartBattle.MMOActivityBattleAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| target | [uint32](#uint32) |  |  |
| from | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |
| tick | [uint32](#uint32) |  |  |
| critical | [uint32](#uint32) |  |  |






<a name="lq-ResMMOActivityStartBattle-MMOActivityBattleUnit"></a>

### ResMMOActivityStartBattle.MMOActivityBattleUnit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| hp | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |






<a name="lq-ResMMOActivityUpdatehFriendList"></a>

### ResMMOActivityUpdatehFriendList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| friend_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| random_friends | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| npc_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| expire_time | [uint32](#uint32) |  |  |
| changes | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) |  |  |






<a name="lq-ResMailInfo"></a>

### ResMailInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| mails | [Mail](#lq-Mail) | repeated |  |






<a name="lq-ResMarathonActivityFinishRace"></a>

### ResMarathonActivityFinishRace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| highest_record | [MarathonGameRecord](#lq-MarathonGameRecord) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResMarathonActivityStartRace"></a>

### ResMarathonActivityStartRace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| random_seed | [uint32](#uint32) |  |  |
| race_id | [string](#string) |  |  |






<a name="lq-ResMisc"></a>

### ResMisc



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| recharged_list | [uint32](#uint32) | repeated |  |
| faiths | [ResMisc.MiscFaithData](#lq-ResMisc-MiscFaithData) | repeated |  |
| verified_hidden | [uint32](#uint32) |  |  |
| verified_value | [uint32](#uint32) |  |  |
| disable_room_random_bot_char | [uint32](#uint32) |  |  |






<a name="lq-ResMisc-MiscFaithData"></a>

### ResMisc.MiscFaithData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| faith_id | [uint32](#uint32) |  |  |
| count | [int32](#int32) |  |  |






<a name="lq-ResModNicknameTime"></a>

### ResModNicknameTime



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| last_mod_time | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResMonthTicketInfo"></a>

### ResMonthTicketInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| month_ticket_info | [MonthTicketInfo](#lq-MonthTicketInfo) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResMoveCombiningCraft"></a>

### ResMoveCombiningCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| pos | [uint32](#uint32) |  |  |
| combined | [uint32](#uint32) |  |  |
| craft_id | [uint32](#uint32) |  |  |
| bonus | [ResMoveCombiningCraft.BonusData](#lq-ResMoveCombiningCraft-BonusData) |  |  |






<a name="lq-ResMoveCombiningCraft-BonusData"></a>

### ResMoveCombiningCraft.BonusData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| craft_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-ResMultiAccountBrief"></a>

### ResMultiAccountBrief



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| players | [PlayerBaseView](#lq-PlayerBaseView) | repeated |  |






<a name="lq-ResMutiChallengeLevel"></a>

### ResMutiChallengeLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResMutiChallengeLevel.Item](#lq-ResMutiChallengeLevel-Item) | repeated |  |






<a name="lq-ResMutiChallengeLevel-Item"></a>

### ResMutiChallengeLevel.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ResNextGameRecordList"></a>

### ResNextGameRecordList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| next | [bool](#bool) |  |  |
| entries | [RecordListEntry](#lq-RecordListEntry) | repeated |  |
| iterator_expire | [uint32](#uint32) |  |  |
| next_end_time | [uint32](#uint32) |  |  |






<a name="lq-ResNextRoundVillage"></a>

### ResNextRoundVillage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| activity_data | [ActivityVillageData](#lq-ActivityVillageData) |  |  |






<a name="lq-ResOauth2Auth"></a>

### ResOauth2Auth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| access_token | [string](#string) |  |  |






<a name="lq-ResOauth2Check"></a>

### ResOauth2Check



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| has_account | [bool](#bool) |  |  |






<a name="lq-ResOauth2Signup"></a>

### ResOauth2Signup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResOpenAllRewardItem"></a>

### ResOpenAllRewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| results | [OpenResult](#lq-OpenResult) | repeated |  |






<a name="lq-ResOpenChest"></a>

### ResOpenChest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| results | [OpenResult](#lq-OpenResult) | repeated |  |
| total_open_count | [uint32](#uint32) |  |  |
| faith_count | [uint32](#uint32) |  |  |
| chest_replace_up | [ResOpenChest.ChestReplaceCountData](#lq-ResOpenChest-ChestReplaceCountData) | repeated |  |






<a name="lq-ResOpenChest-ChestReplaceCountData"></a>

### ResOpenChest.ChestReplaceCountData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResOpenGacha"></a>

### ResOpenGacha



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result_list | [uint32](#uint32) | repeated |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| sp_reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| remain_count | [uint32](#uint32) |  |  |






<a name="lq-ResOpenPreChestItem"></a>

### ResOpenPreChestItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| results | [OpenResult](#lq-OpenResult) | repeated |  |






<a name="lq-ResOpenRandomRewardItem"></a>

### ResOpenRandomRewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| results | [OpenResult](#lq-OpenResult) | repeated |  |






<a name="lq-ResPayMonthTicket"></a>

### ResPayMonthTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| resource_id | [uint32](#uint32) |  |  |
| resource_count | [uint32](#uint32) |  |  |






<a name="lq-ResPlatformBillingProducts"></a>

### ResPlatformBillingProducts



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| products | [BillingProduct](#lq-BillingProduct) | repeated |  |






<a name="lq-ResProgressRewardActivityReceive"></a>

### ResProgressRewardActivityReceive



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResQuestCrewActivityFeed"></a>

### ResQuestCrewActivityFeed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| value_changes | [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges) |  |  |
| execute_result | [ExecuteResult](#lq-ExecuteResult) | repeated |  |






<a name="lq-ResQuestCrewActivityHire"></a>

### ResQuestCrewActivityHire



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| value_changes | [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges) |  |  |
| execute_result | [ExecuteResult](#lq-ExecuteResult) | repeated |  |






<a name="lq-ResQuestCrewActivityRefreshMarket"></a>

### ResQuestCrewActivityRefreshMarket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| value_changes | [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges) |  |  |
| execute_result | [ExecuteResult](#lq-ExecuteResult) | repeated |  |






<a name="lq-ResQuestCrewActivityStartQuest"></a>

### ResQuestCrewActivityStartQuest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result | [uint32](#uint32) |  |  |
| value_changes | [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges) |  |  |
| effect_info | [ResQuestCrewActivityStartQuest.ActivityQuestCrewEffectInfo](#lq-ResQuestCrewActivityStartQuest-ActivityQuestCrewEffectInfo) | repeated |  |






<a name="lq-ResQuestCrewActivityStartQuest-ActivityQuestCrewEffectInfo"></a>

### ResQuestCrewActivityStartQuest.ActivityQuestCrewEffectInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| member_id | [uint32](#uint32) |  |  |
| effect_id | [uint32](#uint32) |  |  |
| result | [ActivityQuestCrewEffectResult](#lq-ActivityQuestCrewEffectResult) |  |  |






<a name="lq-ResRandomCharacter"></a>

### ResRandomCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| enabled | [bool](#bool) |  |  |
| pool | [RandomCharacter](#lq-RandomCharacter) | repeated |  |






<a name="lq-ResReadSNS"></a>

### ResReadSNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| sns_content | [SNSBlog](#lq-SNSBlog) |  |  |






<a name="lq-ResReceiveAchievementGroupReward"></a>

### ResReceiveAchievementGroupReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| execute_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResReceiveAchievementReward"></a>

### ResReceiveAchievementReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| execute_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResReceiveActivityFlipTask"></a>

### ResReceiveActivityFlipTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResReceiveActivityFlipTaskBatch"></a>

### ResReceiveActivityFlipTaskBatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveActivitySpotReward"></a>

### ResReceiveActivitySpotReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResReceiveActivitySpotReward.RewardItem](#lq-ResReceiveActivitySpotReward-RewardItem) | repeated |  |






<a name="lq-ResReceiveActivitySpotReward-RewardItem"></a>

### ResReceiveActivitySpotReward.RewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveAllActivityGift"></a>

### ResReceiveAllActivityGift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| receive_gift | [ResReceiveAllActivityGift.ReceiveRewards](#lq-ResReceiveAllActivityGift-ReceiveRewards) | repeated |  |






<a name="lq-ResReceiveAllActivityGift-ReceiveRewards"></a>

### ResReceiveAllActivityGift.ReceiveRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| from_account_id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveChallengeRankReward"></a>

### ResReceiveChallengeRankReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rewards | [ResReceiveChallengeRankReward.Reward](#lq-ResReceiveChallengeRankReward-Reward) | repeated |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResReceiveChallengeRankReward-Reward"></a>

### ResReceiveChallengeRankReward.Reward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveCharacterRewards"></a>

### ResReceiveCharacterRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResReceiveCharacterRewards.RewardItem](#lq-ResReceiveCharacterRewards-RewardItem) | repeated |  |






<a name="lq-ResReceiveCharacterRewards-RewardItem"></a>

### ResReceiveCharacterRewards.RewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveRPGRewards"></a>

### ResReceiveRPGRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| items | [ResReceiveRPGRewards.RewardItem](#lq-ResReceiveRPGRewards-RewardItem) | repeated |  |






<a name="lq-ResReceiveRPGRewards-RewardItem"></a>

### ResReceiveRPGRewards.RewardItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResReceiveUpgradeActivityReward"></a>

### ResReceiveUpgradeActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResReceiveVillageBuildingReward"></a>

### ResReceiveVillageBuildingReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResReceiveVillageTripReward"></a>

### ResReceiveVillageTripReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResRecoverCombiningRecycle"></a>

### ResRecoverCombiningRecycle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| craft_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-ResRefreshChallenge"></a>

### ResRefreshChallenge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| task_progress | [TaskProgress](#lq-TaskProgress) | repeated |  |
| refresh_count | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |






<a name="lq-ResRefreshDailyTask"></a>

### ResRefreshDailyTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| progress | [TaskProgress](#lq-TaskProgress) |  |  |
| refresh_count | [uint32](#uint32) |  |  |






<a name="lq-ResRefreshGameObserveAuth"></a>

### ResRefreshGameObserveAuth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| ttl | [uint32](#uint32) |  |  |






<a name="lq-ResRefreshZHPShop"></a>

### ResRefreshZHPShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| zhp | [ZHPShop](#lq-ZHPShop) |  |  |






<a name="lq-ResRemoveCollectedGameRecord"></a>

### ResRemoveCollectedGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResReplySNS"></a>

### ResReplySNS



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| sns_reply | [SNSReply](#lq-SNSReply) |  |  |






<a name="lq-ResResolveFestivalActivityEvent"></a>

### ResResolveFestivalActivityEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| effected_buff | [uint32](#uint32) | repeated |  |
| reward_items | [ExecuteResult](#lq-ExecuteResult) | repeated |  |
| ending_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ResResolveFestivalActivityProposal"></a>

### ResResolveFestivalActivityProposal



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| effected_buff | [uint32](#uint32) | repeated |  |
| result | [uint32](#uint32) |  |  |
| reward_items | [ExecuteResult](#lq-ExecuteResult) | repeated |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ResReviveCoinInfo"></a>

### ResReviveCoinInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| has_gained | [bool](#bool) |  |  |






<a name="lq-ResRichmanChestInfo"></a>

### ResRichmanChestInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [ResRichmanChestInfo.ItemData](#lq-ResRichmanChestInfo-ItemData) | repeated |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResRichmanChestInfo-ItemData"></a>

### ResRichmanChestInfo.ItemData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ResRichmanNextMove"></a>

### ResRichmanNextMove



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| paths | [ResRichmanNextMove.PathData](#lq-ResRichmanNextMove-PathData) | repeated |  |
| dice | [uint32](#uint32) |  |  |
| location | [uint32](#uint32) |  |  |
| finished_count | [uint32](#uint32) |  |  |
| step | [uint32](#uint32) |  |  |
| buff | [ResRichmanNextMove.BuffData](#lq-ResRichmanNextMove-BuffData) | repeated |  |
| bank_save | [uint32](#uint32) |  |  |
| chest_position | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| bank_save_add | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResRichmanNextMove-BuffData"></a>

### ResRichmanNextMove.BuffData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| remain | [uint32](#uint32) |  |  |
| effect | [uint32](#uint32) |  |  |






<a name="lq-ResRichmanNextMove-PathData"></a>

### ResRichmanNextMove.PathData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| location | [uint32](#uint32) |  |  |
| rewards | [ResRichmanNextMove.RewardData](#lq-ResRichmanNextMove-RewardData) | repeated |  |
| events | [uint32](#uint32) | repeated |  |






<a name="lq-ResRichmanNextMove-RewardData"></a>

### ResRichmanNextMove.RewardData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| origin_count | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ResSearchAccountById"></a>

### ResSearchAccountById



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| player | [PlayerBaseView](#lq-PlayerBaseView) |  |  |






<a name="lq-ResSearchAccountByPattern"></a>

### ResSearchAccountByPattern



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| is_finished | [bool](#bool) |  |  |
| match_accounts | [uint32](#uint32) | repeated |  |
| decode_id | [uint32](#uint32) |  |  |






<a name="lq-ResSearchAccountbyEidLobby"></a>

### ResSearchAccountbyEidLobby



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ResSelfRoom"></a>

### ResSelfRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| room | [Room](#lq-Room) |  |  |






<a name="lq-ResSendActivityGiftToFriend"></a>

### ResSendActivityGiftToFriend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| send_gift_count | [uint32](#uint32) |  |  |






<a name="lq-ResSendGiftToCharacter"></a>

### ResSendGiftToCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| level | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |






<a name="lq-ResServerSettings"></a>

### ResServerSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| settings | [ServerSettings](#lq-ServerSettings) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResServerTime"></a>

### ResServerTime



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| server_time | [uint32](#uint32) |  |  |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResSetHiddenCharacter"></a>

### ResSetHiddenCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| hidden_characters | [uint32](#uint32) | repeated |  |






<a name="lq-ResSetVillageWorker"></a>

### ResSetVillageWorker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| building | [VillageBuildingData](#lq-VillageBuildingData) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-ResShootActivityAttackEnemies"></a>

### ResShootActivityAttackEnemies



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| records | [ResShootActivityAttackEnemies.ActivityShootAttackRecord](#lq-ResShootActivityAttackEnemies-ActivityShootAttackRecord) | repeated |  |
| value_change | [ActivityShootValueChange](#lq-ActivityShootValueChange) |  |  |






<a name="lq-ResShootActivityAttackEnemies-ActivityShootAttackRecord"></a>

### ResShootActivityAttackEnemies.ActivityShootAttackRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [uint32](#uint32) |  |  |
| enemy | [ActivityShootEnemyInfo](#lq-ActivityShootEnemyInfo) |  |  |
| level | [uint32](#uint32) |  |  |
| reward_ids | [uint32](#uint32) | repeated |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResShopInfo"></a>

### ResShopInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| shop_info | [ShopInfo](#lq-ShopInfo) |  |  |






<a name="lq-ResShopPurchase"></a>

### ResShopPurchase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| update | [AccountUpdate](#lq-AccountUpdate) |  |  |






<a name="lq-ResSignupAccount"></a>

### ResSignupAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResSignupCustomizedContest"></a>

### ResSignupCustomizedContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| state | [uint32](#uint32) |  |  |






<a name="lq-ResSimV2ActivityEndMatch"></a>

### ResSimV2ActivityEndMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| round | [uint32](#uint32) |  |  |
| is_end | [bool](#bool) |  |  |
| record | [SimulationV2Record](#lq-SimulationV2Record) |  |  |
| total_score | [int32](#int32) |  |  |
| match_history | [SimulationV2MatchRecord](#lq-SimulationV2MatchRecord) | repeated |  |
| rewards | [ResSimV2ActivityEndMatch.SimulationV2MatchReward](#lq-ResSimV2ActivityEndMatch-SimulationV2MatchReward) | repeated |  |
| effect_list | [SimulationV2Effect](#lq-SimulationV2Effect) | repeated |  |
| ability | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |






<a name="lq-ResSimV2ActivityEndMatch-SimulationV2MatchReward"></a>

### ResSimV2ActivityEndMatch.SimulationV2MatchReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| params | [uint32](#uint32) | repeated |  |






<a name="lq-ResSimV2ActivityFetchInfo"></a>

### ResSimV2ActivityFetchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| data | [SimulationV2Data](#lq-SimulationV2Data) |  |  |






<a name="lq-ResSimV2ActivitySelectEvent"></a>

### ResSimV2ActivitySelectEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| event | [SimulationV2Event](#lq-SimulationV2Event) |  |  |
| ability | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |
| match | [SimulationV2Match](#lq-SimulationV2Match) |  |  |
| effect_list | [SimulationV2Effect](#lq-SimulationV2Effect) | repeated |  |
| round | [uint32](#uint32) |  |  |
| is_end | [bool](#bool) |  |  |
| result_id | [uint32](#uint32) |  |  |
| record | [SimulationV2Record](#lq-SimulationV2Record) |  |  |
| effected_buff_list | [uint32](#uint32) | repeated |  |






<a name="lq-ResSimV2ActivityStartMatch"></a>

### ResSimV2ActivityStartMatch



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| event | [SimulationV2Event](#lq-SimulationV2Event) |  |  |
| match | [SimulationV2Match](#lq-SimulationV2Match) |  |  |
| effect_list | [SimulationV2Effect](#lq-SimulationV2Effect) | repeated |  |
| is_match_end | [bool](#bool) |  |  |






<a name="lq-ResSimV2ActivityStartSeason"></a>

### ResSimV2ActivityStartSeason



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| season | [SimulationV2SeasonData](#lq-SimulationV2SeasonData) |  |  |






<a name="lq-ResSimV2ActivityTrain"></a>

### ResSimV2ActivityTrain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| event | [SimulationV2Event](#lq-SimulationV2Event) |  |  |
| ability | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |
| round | [uint32](#uint32) |  |  |
| effect_list | [SimulationV2Effect](#lq-SimulationV2Effect) | repeated |  |
| train_result | [uint32](#uint32) |  |  |
| is_end | [bool](#bool) |  |  |
| record | [SimulationV2Record](#lq-SimulationV2Record) |  |  |






<a name="lq-ResSimulationActivityTrain"></a>

### ResSimulationActivityTrain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result_type | [uint32](#uint32) |  |  |
| final_stats | [uint32](#uint32) | repeated |  |






<a name="lq-ResSnowballActivityFinishBattle"></a>

### ResSnowballActivityFinishBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivitySnowballValueChanges](#lq-ActivitySnowballValueChanges) |  |  |






<a name="lq-ResSnowballActivityReceiveReward"></a>

### ResSnowballActivityReceiveReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivitySnowballValueChanges](#lq-ActivitySnowballValueChanges) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResSnowballActivityStartBattle"></a>

### ResSnowballActivityStartBattle



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| random_seed | [uint32](#uint32) |  |  |
| boss_action | [SnowballActivityBossAction](#lq-SnowballActivityBossAction) | repeated |  |
| battle_id | [string](#string) |  |  |
| player_state | [ActivitySnowballPlayerState](#lq-ActivitySnowballPlayerState) | repeated |  |
| random_seq | [uint32](#uint32) | repeated |  |






<a name="lq-ResSnowballActivityUpgrade"></a>

### ResSnowballActivityUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| changes | [ActivitySnowballValueChanges](#lq-ActivitySnowballValueChanges) |  |  |






<a name="lq-ResStartSimulationActivityGame"></a>

### ResStartSimulationActivityGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| records | [ActivitySimulationGameRecord](#lq-ActivitySimulationGameRecord) | repeated |  |






<a name="lq-ResStoryActivityUnlockEndingAndReceive"></a>

### ResStoryActivityUnlockEndingAndReceive



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| ending_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| finish_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |
| all_finish_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResStoryReward"></a>

### ResStoryReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| reward_items | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResTitleList"></a>

### ResTitleList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| title_list | [uint32](#uint32) | repeated |  |






<a name="lq-ResUpgradeActivityLevel"></a>

### ResUpgradeActivityLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResUpgradeChallenge"></a>

### ResUpgradeChallenge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| task_progress | [TaskProgress](#lq-TaskProgress) | repeated |  |
| refresh_count | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |






<a name="lq-ResUpgradeCharacter"></a>

### ResUpgradeCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| character | [Character](#lq-Character) |  |  |






<a name="lq-ResUseGiftCode"></a>

### ResUseGiftCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-ResUseSpecialGiftCode"></a>

### ResUseSpecialGiftCode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| rewards | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ResVerfiyCodeForSecure"></a>

### ResVerfiyCodeForSecure



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| secure_token | [string](#string) |  |  |






<a name="lq-ResVerificationIAPOrder"></a>

### ResVerificationIAPOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResVipReward"></a>

### ResVipReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| gained_vip_levels | [uint32](#uint32) | repeated |  |






<a name="lq-ResVoteActivity"></a>

### ResVoteActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| vote_records | [VoteData](#lq-VoteData) | repeated |  |






<a name="lq-ResYostarDeleteAccount"></a>

### ResYostarDeleteAccount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| notify_url | [string](#string) |  |  |






<a name="lq-SNSBlog"></a>

### SNSBlog



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| read_time | [uint32](#uint32) |  |  |






<a name="lq-SNSReply"></a>

### SNSReply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| reply_time | [uint32](#uint32) |  |  |















<a name="cli_route-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## cli_route.proto



<a name="lq-ReqHeartbeat"></a>

### ReqHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| delay | [uint32](#uint32) |  |  |
| no_operation_counter | [uint32](#uint32) |  |  |
| platform | [uint32](#uint32) |  |  |
| network_quality | [uint32](#uint32) |  |  |






<a name="lq-ReqRequestConnection"></a>

### ReqRequestConnection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| route_id | [string](#string) |  |  |
| timestamp | [uint64](#uint64) |  |  |
| platform | [string](#string) |  |  |






<a name="lq-ReqRequestRouteChange"></a>

### ReqRequestRouteChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| before | [string](#string) |  |  |
| route_id | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ResHeartbeat"></a>

### ResHeartbeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-ResRequestConnection"></a>

### ResRequestConnection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| timestamp | [uint64](#uint64) |  |  |
| result | [uint32](#uint32) |  |  |






<a name="lq-ResRequestRouteChange"></a>

### ResRequestRouteChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| result | [uint32](#uint32) |  |  |















<a name="client-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## client.proto












<a name="com_const-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## com_const.proto





<a name="lq-EnErrorCode"></a>

### EnErrorCode


| Name | Number | Description |
| ---- | ------ | ----------- |
| OK | 0 |  |
| EN_ERR_TIMEOUT | 101 |  |
| EN_ERR_INVALID_PARAM | 102 |  |
| EN_ERR_CANT_AFFORD | 103 |  |
| EN_ERR_NOT_LOGIN | 104 |  |
| EN_ERR_NOT_GM | 105 |  |
| EN_ERR_SYSTEM | 106 |  |
| EN_ERR_USER_NOT_FOUND | 107 |  |
| EN_ERR_REWARD_RECEIVED | 108 |  |
| EN_ERR_NOT_FOUND_UUID | 109 |  |
| EN_ERR_MANUAL_DISCONNECT | 110 |  |
| EN_ERR_LOST_CONNECTION | 111 |  |
| EN_ERR_CONNECT_FAILED | 112 |  |
| EN_ERR_MAINTENANCE | 113 |  |
| EN_ERR_ACCESS_DENY | 114 |  |
| ERR_UNKNOWN | 1 |  |
| ERR_SYSTEM_ERROR | 2 |  |
| ERR_DUPLICATE_SIGN_UP | 1001 |  |
| ERR_NOT_SIGN_UP | 1002 |  |
| ERR_PASSWORD | 1003 |  |
| ERR_NOT_LOGIN | 1004 |  |
| ERR_ALREADY_LOGIN | 1005 |  |
| ERR_ACCOUNT_NOT_EXIST | 1006 |  |
| ERR_ROOM_NOT_EXIST | 1007 |  |
| ERR_ROOM_IS_FULL | 1008 |  |
| ERR_ROOM_ALREADY_LEAVE | 1009 |  |
| ERR_ROOM_NOT_OWNER | 1010 |  |
| ERR_ROOM_NOT_ALL_READY | 1011 |  |
| ERR_TOKEN_NOT_EXIST | 1012 |  |
| ERR_TOKEN_INVALID | 1013 |  |
| ERR_GAME_NOT_EXIST | 1014 |  |
| ERR_GAME_REFUSED | 1015 |  |
| ERR_NOT_PLAYING_GAME | 1016 |  |










<a name="com_struct-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## com_struct.proto



<a name="lq-AccSn"></a>

### AccSn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource | [AccountResourceSnapshot](#lq-AccountResourceSnapshot) |  |  |
| character | [AccountCharacterSnapshot](#lq-AccountCharacterSnapshot) |  |  |
| mail | [AccountMailRecord](#lq-AccountMailRecord) |  |  |
| achievement | [AccountAchievementSnapshot](#lq-AccountAchievementSnapshot) |  |  |
| misc | [AccountMiscSnapshot](#lq-AccountMiscSnapshot) |  |  |
| gift_code | [AccountGiftCodeRecord](#lq-AccountGiftCodeRecord) |  |  |






<a name="lq-AccSnDa"></a>

### AccSnDa



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| snapshot | [bytes](#bytes) |  |  |






<a name="lq-Account"></a>

### Account



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| login_time | [uint32](#uint32) |  |  |
| logout_time | [uint32](#uint32) |  |  |
| room_id | [uint32](#uint32) |  |  |
| anti_addiction | [AntiAddiction](#lq-AntiAddiction) |  |  |
| title | [uint32](#uint32) |  |  |
| signature | [string](#string) |  |  |
| email | [string](#string) |  |  |
| email_verify | [uint32](#uint32) |  |  |
| gold | [uint32](#uint32) |  |  |
| diamond | [uint32](#uint32) |  |  |
| avatar_id | [uint32](#uint32) |  |  |
| vip | [uint32](#uint32) |  |  |
| birthday | [int32](#int32) |  |  |
| phone | [string](#string) |  |  |
| phone_verify | [uint32](#uint32) |  |  |
| platform_diamond | [Account.PlatformDiamond](#lq-Account-PlatformDiamond) | repeated |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| skin_ticket | [uint32](#uint32) |  |  |
| platform_skin_ticket | [Account.PlatformSkinTicket](#lq-Account-PlatformSkinTicket) | repeated |  |
| verified | [uint32](#uint32) |  |  |
| challenge_levels | [Account.ChallengeLevel](#lq-Account-ChallengeLevel) | repeated |  |
| achievement_count | [Account.AchievementCount](#lq-Account-AchievementCount) | repeated |  |
| frozen_state | [uint32](#uint32) |  |  |
| loading_image | [uint32](#uint32) | repeated |  |
| favorite_hu | [FavoriteHu](#lq-FavoriteHu) | repeated |  |
| badges | [Account.Badge](#lq-Account-Badge) | repeated |  |






<a name="lq-Account-AchievementCount"></a>

### Account.AchievementCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rare | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-Account-Badge"></a>

### Account.Badge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| achieved_time | [uint32](#uint32) |  |  |
| achieved_counter | [uint32](#uint32) |  |  |






<a name="lq-Account-ChallengeLevel"></a>

### Account.ChallengeLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |






<a name="lq-Account-PlatformDiamond"></a>

### Account.PlatformDiamond



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-Account-PlatformSkinTicket"></a>

### Account.PlatformSkinTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-AccountAchievementSnapshot"></a>

### AccountAchievementSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| achievements | [AchievementProgress](#lq-AchievementProgress) | repeated |  |
| rewarded_group | [AccountAchievementSnapshot.RewardedGroupSnapshot](#lq-AccountAchievementSnapshot-RewardedGroupSnapshot) |  |  |
| version | [AccountAchievementSnapshot.AchievementVersion](#lq-AccountAchievementSnapshot-AchievementVersion) |  |  |






<a name="lq-AccountAchievementSnapshot-AchievementVersion"></a>

### AccountAchievementSnapshot.AchievementVersion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [uint32](#uint32) |  |  |






<a name="lq-AccountAchievementSnapshot-RewardedGroupSnapshot"></a>

### AccountAchievementSnapshot.RewardedGroupSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rewarded_id | [uint32](#uint32) |  |  |






<a name="lq-AccountActiveState"></a>

### AccountActiveState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| login_time | [uint32](#uint32) |  |  |
| logout_time | [uint32](#uint32) |  |  |
| is_online | [bool](#bool) |  |  |
| playing | [AccountPlayingGame](#lq-AccountPlayingGame) |  |  |






<a name="lq-AccountActivityUpdate"></a>

### AccountActivityUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mine_data | [MineActivityData](#lq-MineActivityData) | repeated |  |
| rpg_data | [RPGActivity](#lq-RPGActivity) | repeated |  |
| feed_data | [ActivityFeedData](#lq-ActivityFeedData) | repeated |  |
| spot_data | [ActivitySpotData](#lq-ActivitySpotData) | repeated |  |
| friend_gift_data | [ActivityFriendGiftData](#lq-ActivityFriendGiftData) | repeated |  |
| upgrade_data | [ActivityUpgradeData](#lq-ActivityUpgradeData) | repeated |  |
| gacha_data | [ActivityGachaUpdateData](#lq-ActivityGachaUpdateData) | repeated |  |
| simulation_data | [ActivitySimulationData](#lq-ActivitySimulationData) | repeated |  |
| combining_data | [ActivityCombiningLQData](#lq-ActivityCombiningLQData) | repeated |  |
| village_data | [ActivityVillageData](#lq-ActivityVillageData) | repeated |  |
| festival_data | [ActivityFestivalData](#lq-ActivityFestivalData) | repeated |  |
| island_data | [ActivityIslandData](#lq-ActivityIslandData) | repeated |  |
| story_data | [ActivityStoryData](#lq-ActivityStoryData) | repeated |  |
| choose_up_data | [ActivityChooseUpData](#lq-ActivityChooseUpData) | repeated |  |
| simulation_v2_data | [SimulationV2Data](#lq-SimulationV2Data) | repeated |  |
| quest_crew_data | [ActivityQuestCrewChanges](#lq-ActivityQuestCrewChanges) | repeated |  |
| shoot_data | [ActivityShootData](#lq-ActivityShootData) | repeated |  |
| bingo_data | [ActivityBingoData](#lq-ActivityBingoData) | repeated |  |
| snowball_data | [ActivitySnowballValueChanges](#lq-ActivitySnowballValueChanges) | repeated |  |
| choose_group_up_data | [ActivityChooseGroupData](#lq-ActivityChooseGroupData) | repeated |  |
| mmo_data | [ActivityMMODataChanges](#lq-ActivityMMODataChanges) | repeated |  |
| activity_buff | [AccountActivityUpdate.ActivityBuffDataArrayDirty](#lq-AccountActivityUpdate-ActivityBuffDataArrayDirty) |  |  |






<a name="lq-AccountActivityUpdate-ActivityBuffDataArrayDirty"></a>

### AccountActivityUpdate.ActivityBuffDataArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [ActivityBuffData](#lq-ActivityBuffData) | repeated |  |






<a name="lq-AccountCacheView"></a>

### AccountCacheView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cache_version | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| login_time | [uint32](#uint32) |  |  |
| logout_time | [uint32](#uint32) |  |  |
| is_online | [bool](#bool) |  |  |
| room_id | [uint32](#uint32) |  |  |
| title | [uint32](#uint32) |  |  |
| avatar_id | [uint32](#uint32) |  |  |
| vip | [uint32](#uint32) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| playing_game | [AccountPlayingGame](#lq-AccountPlayingGame) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |
| ban_deadline | [uint32](#uint32) |  |  |
| comment_ban | [uint32](#uint32) |  |  |
| ban_state | [uint32](#uint32) |  |  |






<a name="lq-AccountCharacterSnapshot"></a>

### AccountCharacterSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| created_characters | [uint32](#uint32) | repeated |  |
| removed_characters | [Character](#lq-Character) | repeated |  |
| modified_characters | [Character](#lq-Character) | repeated |  |
| main_character | [AccountCharacterSnapshot.MainCharacterSnapshot](#lq-AccountCharacterSnapshot-MainCharacterSnapshot) |  |  |
| skins | [AccountCharacterSnapshot.SkinsSnapshot](#lq-AccountCharacterSnapshot-SkinsSnapshot) |  |  |
| hidden_characters | [AccountCharacterSnapshot.HiddenCharacter](#lq-AccountCharacterSnapshot-HiddenCharacter) |  |  |






<a name="lq-AccountCharacterSnapshot-HiddenCharacter"></a>

### AccountCharacterSnapshot.HiddenCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hidden_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountCharacterSnapshot-MainCharacterSnapshot"></a>

### AccountCharacterSnapshot.MainCharacterSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |






<a name="lq-AccountCharacterSnapshot-SkinsSnapshot"></a>

### AccountCharacterSnapshot.SkinsSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skin_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountDetailStatistic"></a>

### AccountDetailStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_mode | [AccountStatisticByGameMode](#lq-AccountStatisticByGameMode) | repeated |  |
| fan | [AccountStatisticByFan](#lq-AccountStatisticByFan) | repeated |  |
| liujumanguan | [uint32](#uint32) |  |  |
| fan_achieved | [AccountFanAchieved](#lq-AccountFanAchieved) | repeated |  |






<a name="lq-AccountDetailStatisticByCategory"></a>

### AccountDetailStatisticByCategory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [uint32](#uint32) |  |  |
| detail_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |






<a name="lq-AccountDetailStatisticV2"></a>

### AccountDetailStatisticV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| friend_room_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| rank_statistic | [AccountDetailStatisticV2.RankStatistic](#lq-AccountDetailStatisticV2-RankStatistic) |  |  |
| customized_contest_statistic | [AccountDetailStatisticV2.CustomizedContestStatistic](#lq-AccountDetailStatisticV2-CustomizedContestStatistic) |  |  |
| leisure_match_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| challenge_match_statistic | [AccountDetailStatisticV2.ChallengeStatistic](#lq-AccountDetailStatisticV2-ChallengeStatistic) |  |  |
| activity_match_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| ab_match_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |






<a name="lq-AccountDetailStatisticV2-ChallengeStatistic"></a>

### AccountDetailStatisticV2.ChallengeStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| all_season | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| season_data_list | [AccountDetailStatisticV2.ChallengeStatistic.SeasonData](#lq-AccountDetailStatisticV2-ChallengeStatistic-SeasonData) | repeated |  |






<a name="lq-AccountDetailStatisticV2-ChallengeStatistic-SeasonData"></a>

### AccountDetailStatisticV2.ChallengeStatistic.SeasonData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season_id | [uint32](#uint32) |  |  |
| statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |






<a name="lq-AccountDetailStatisticV2-CustomizedContestStatistic"></a>

### AccountDetailStatisticV2.CustomizedContestStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| month_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| month_refresh_time | [uint32](#uint32) |  |  |






<a name="lq-AccountDetailStatisticV2-RankStatistic"></a>

### AccountDetailStatisticV2.RankStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_statistic | [AccountDetailStatisticV2.RankStatistic.RankData](#lq-AccountDetailStatisticV2-RankStatistic-RankData) |  |  |
| month_statistic | [AccountDetailStatisticV2.RankStatistic.RankData](#lq-AccountDetailStatisticV2-RankStatistic-RankData) |  |  |
| month_refresh_time | [uint32](#uint32) |  |  |






<a name="lq-AccountDetailStatisticV2-RankStatistic-RankData"></a>

### AccountDetailStatisticV2.RankStatistic.RankData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| all_level_statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |
| level_data_list | [AccountDetailStatisticV2.RankStatistic.RankData.RankLevelData](#lq-AccountDetailStatisticV2-RankStatistic-RankData-RankLevelData) | repeated |  |






<a name="lq-AccountDetailStatisticV2-RankStatistic-RankData-RankLevelData"></a>

### AccountDetailStatisticV2.RankStatistic.RankData.RankLevelData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank_level | [uint32](#uint32) |  |  |
| statistic | [AccountDetailStatistic](#lq-AccountDetailStatistic) |  |  |






<a name="lq-AccountFanAchieved"></a>

### AccountFanAchieved



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mahjong_category | [uint32](#uint32) |  |  |
| fan | [AccountStatisticByFan](#lq-AccountStatisticByFan) | repeated |  |
| liujumanguan | [uint32](#uint32) |  |  |






<a name="lq-AccountGiftCodeRecord"></a>

### AccountGiftCodeRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| used_gift_code | [string](#string) | repeated |  |






<a name="lq-AccountLevel"></a>

### AccountLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| score | [uint32](#uint32) |  |  |






<a name="lq-AccountMahjongStatistic"></a>

### AccountMahjongStatistic



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| final_position_counts | [uint32](#uint32) | repeated |  |
| recent_round | [AccountMahjongStatistic.RoundSummary](#lq-AccountMahjongStatistic-RoundSummary) |  |  |
| recent_hu | [AccountMahjongStatistic.HuSummary](#lq-AccountMahjongStatistic-HuSummary) |  |  |
| highest_hu | [HighestHuRecord](#lq-HighestHuRecord) |  |  |
| recent_20_hu_summary | [AccountMahjongStatistic.Liqi20Summary](#lq-AccountMahjongStatistic-Liqi20Summary) |  |  |
| recent_10_hu_summary | [AccountMahjongStatistic.LiQi10Summary](#lq-AccountMahjongStatistic-LiQi10Summary) |  |  |
| recent_10_game_result | [AccountMahjongStatistic.GameResult](#lq-AccountMahjongStatistic-GameResult) | repeated |  |






<a name="lq-AccountMahjongStatistic-GameResult"></a>

### AccountMahjongStatistic.GameResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| final_point | [int32](#int32) |  |  |






<a name="lq-AccountMahjongStatistic-HuSummary"></a>

### AccountMahjongStatistic.HuSummary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_count | [uint32](#uint32) |  |  |
| dora_round_count | [uint32](#uint32) |  |  |
| total_fan | [uint32](#uint32) |  |  |






<a name="lq-AccountMahjongStatistic-LiQi10Summary"></a>

### AccountMahjongStatistic.LiQi10Summary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_xuanshang | [uint32](#uint32) |  |  |
| total_fanshu | [uint32](#uint32) |  |  |






<a name="lq-AccountMahjongStatistic-Liqi20Summary"></a>

### AccountMahjongStatistic.Liqi20Summary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_count | [uint32](#uint32) |  |  |
| total_lidora_count | [uint32](#uint32) |  |  |
| average_hu_point | [uint32](#uint32) |  |  |






<a name="lq-AccountMahjongStatistic-RoundSummary"></a>

### AccountMahjongStatistic.RoundSummary



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| total_count | [uint32](#uint32) |  |  |
| rong_count | [uint32](#uint32) |  |  |
| zimo_count | [uint32](#uint32) |  |  |
| fangchong_count | [uint32](#uint32) |  |  |






<a name="lq-AccountMailRecord"></a>

### AccountMailRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| created_mails | [uint32](#uint32) | repeated |  |
| removed_mails | [AccountMailRecord.MailSnapshot](#lq-AccountMailRecord-MailSnapshot) | repeated |  |
| modified_mails | [AccountMailRecord.MailSnapshot](#lq-AccountMailRecord-MailSnapshot) | repeated |  |






<a name="lq-AccountMailRecord-MailSnapshot"></a>

### AccountMailRecord.MailSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id | [uint32](#uint32) |  |  |
| reference_id | [uint32](#uint32) |  |  |
| create_time | [uint32](#uint32) |  |  |
| expire_time | [uint32](#uint32) |  |  |
| take_attachment | [uint32](#uint32) |  |  |
| attachments | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-AccountMiscSnapshot"></a>

### AccountMiscSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| faith_data | [FaithData](#lq-FaithData) |  |  |
| vip_reward_gained | [AccountMiscSnapshot.AccountVIPRewardSnapshot](#lq-AccountMiscSnapshot-AccountVIPRewardSnapshot) |  |  |
| vip | [AccountMiscSnapshot.AccountVIP](#lq-AccountMiscSnapshot-AccountVIP) |  |  |
| shop_info | [ShopInfo](#lq-ShopInfo) |  |  |
| month_ticket | [AccountMiscSnapshot.AccountMonthTicketSnapshot](#lq-AccountMiscSnapshot-AccountMonthTicketSnapshot) |  |  |
| recharged | [AccountMiscSnapshot.AccountRechargeInfo](#lq-AccountMiscSnapshot-AccountRechargeInfo) |  |  |
| month_ticket_v2 | [AccountMiscSnapshot.AccountMonthTicketSnapshotV2](#lq-AccountMiscSnapshot-AccountMonthTicketSnapshotV2) |  |  |






<a name="lq-AccountMiscSnapshot-AccountMonthTicketSnapshot"></a>

### AccountMiscSnapshot.AccountMonthTicketSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tickets | [AccountMiscSnapshot.MonthTicketInfo](#lq-AccountMiscSnapshot-MonthTicketInfo) | repeated |  |






<a name="lq-AccountMiscSnapshot-AccountMonthTicketSnapshotV2"></a>

### AccountMiscSnapshot.AccountMonthTicketSnapshotV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| end_time | [uint32](#uint32) |  |  |
| last_pay_time | [uint32](#uint32) |  |  |
| record_start_time | [uint32](#uint32) |  |  |
| history | [uint32](#uint32) | repeated |  |






<a name="lq-AccountMiscSnapshot-AccountRechargeInfo"></a>

### AccountMiscSnapshot.AccountRechargeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| records | [AccountMiscSnapshot.AccountRechargeInfo.RechargeRecord](#lq-AccountMiscSnapshot-AccountRechargeInfo-RechargeRecord) | repeated |  |
| has_data | [uint32](#uint32) |  |  |






<a name="lq-AccountMiscSnapshot-AccountRechargeInfo-RechargeRecord"></a>

### AccountMiscSnapshot.AccountRechargeInfo.RechargeRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| recharge_time | [uint32](#uint32) |  |  |






<a name="lq-AccountMiscSnapshot-AccountVIP"></a>

### AccountMiscSnapshot.AccountVIP



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vip | [uint32](#uint32) |  |  |






<a name="lq-AccountMiscSnapshot-AccountVIPRewardSnapshot"></a>

### AccountMiscSnapshot.AccountVIPRewardSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rewarded | [uint32](#uint32) | repeated |  |






<a name="lq-AccountMiscSnapshot-MonthTicketInfo"></a>

### AccountMiscSnapshot.MonthTicketInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| last_pay_time | [uint32](#uint32) |  |  |
| record_start_time | [uint32](#uint32) |  |  |
| history | [uint32](#uint32) | repeated |  |






<a name="lq-AccountOwnerData"></a>

### AccountOwnerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unlock_characters | [uint32](#uint32) | repeated |  |






<a name="lq-AccountPlayingGame"></a>

### AccountPlayingGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_uuid | [string](#string) |  |  |
| category | [uint32](#uint32) |  |  |
| meta | [GameMetaData](#lq-GameMetaData) |  |  |






<a name="lq-AccountResourceSnapshot"></a>

### AccountResourceSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bag_item | [AccountResourceSnapshot.BagItemSnapshot](#lq-AccountResourceSnapshot-BagItemSnapshot) | repeated |  |
| currency | [AccountResourceSnapshot.CurrencySnapshot](#lq-AccountResourceSnapshot-CurrencySnapshot) | repeated |  |
| title | [AccountResourceSnapshot.TitleSnapshot](#lq-AccountResourceSnapshot-TitleSnapshot) |  |  |
| used_title | [AccountResourceSnapshot.UsedTitleSnapshot](#lq-AccountResourceSnapshot-UsedTitleSnapshot) |  |  |
| currency_convert | [uint32](#uint32) |  |  |






<a name="lq-AccountResourceSnapshot-BagItemSnapshot"></a>

### AccountResourceSnapshot.BagItemSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_id | [uint32](#uint32) |  |  |
| resource_count | [uint32](#uint32) |  |  |
| resource_version | [uint32](#uint32) |  |  |






<a name="lq-AccountResourceSnapshot-CurrencySnapshot"></a>

### AccountResourceSnapshot.CurrencySnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| currency_id | [uint32](#uint32) |  |  |
| currency_count | [uint32](#uint32) |  |  |






<a name="lq-AccountResourceSnapshot-TitleSnapshot"></a>

### AccountResourceSnapshot.TitleSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountResourceSnapshot-UsedTitleSnapshot"></a>

### AccountResourceSnapshot.UsedTitleSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| title_id | [uint32](#uint32) |  |  |






<a name="lq-AccountSetting"></a>

### AccountSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-AccountShiLian"></a>

### AccountShiLian



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| step | [uint32](#uint32) |  |  |
| state | [uint32](#uint32) |  |  |






<a name="lq-AccountStatisticByFan"></a>

### AccountStatisticByFan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fan_id | [uint32](#uint32) |  |  |
| sum | [uint32](#uint32) |  |  |






<a name="lq-AccountStatisticByGameMode"></a>

### AccountStatisticByGameMode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode | [uint32](#uint32) |  |  |
| game_count_sum | [uint32](#uint32) |  |  |
| game_final_position | [uint32](#uint32) | repeated |  |
| fly_count | [uint32](#uint32) |  |  |
| gold_earn_sum | [float](#float) |  |  |
| round_count_sum | [uint32](#uint32) |  |  |
| dadian_sum | [float](#float) |  |  |
| round_end | [AccountStatisticByGameMode.RoundEndData](#lq-AccountStatisticByGameMode-RoundEndData) | repeated |  |
| ming_count_sum | [uint32](#uint32) |  |  |
| liqi_count_sum | [uint32](#uint32) |  |  |
| xun_count_sum | [uint32](#uint32) |  |  |
| highest_lianzhuang | [uint32](#uint32) |  |  |
| score_earn_sum | [uint32](#uint32) |  |  |
| rank_score | [AccountStatisticByGameMode.RankScore](#lq-AccountStatisticByGameMode-RankScore) | repeated |  |






<a name="lq-AccountStatisticByGameMode-RankScore"></a>

### AccountStatisticByGameMode.RankScore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| score_sum | [int32](#int32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-AccountStatisticByGameMode-RoundEndData"></a>

### AccountStatisticByGameMode.RoundEndData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| sum | [uint32](#uint32) |  |  |






<a name="lq-AccountStatisticData"></a>

### AccountStatisticData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mahjong_category | [uint32](#uint32) |  |  |
| game_category | [uint32](#uint32) |  |  |
| statistic | [AccountMahjongStatistic](#lq-AccountMahjongStatistic) |  |  |
| game_type | [uint32](#uint32) |  |  |






<a name="lq-AccountUpdate"></a>

### AccountUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| numerical | [AccountUpdate.NumericalUpdate](#lq-AccountUpdate-NumericalUpdate) | repeated |  |
| character | [AccountUpdate.CharacterUpdate](#lq-AccountUpdate-CharacterUpdate) |  |  |
| bag | [BagUpdate](#lq-BagUpdate) |  |  |
| achievement | [AccountUpdate.AchievementUpdate](#lq-AccountUpdate-AchievementUpdate) |  |  |
| shilian | [AccountShiLian](#lq-AccountShiLian) |  |  |
| daily_task | [AccountUpdate.DailyTaskUpdate](#lq-AccountUpdate-DailyTaskUpdate) |  |  |
| title | [AccountUpdate.TitleUpdate](#lq-AccountUpdate-TitleUpdate) |  |  |
| new_recharged_list | [uint32](#uint32) | repeated |  |
| activity_task | [AccountUpdate.TaskUpdate](#lq-AccountUpdate-TaskUpdate) |  |  |
| activity_flip_task | [AccountUpdate.TaskUpdate](#lq-AccountUpdate-TaskUpdate) |  |  |
| activity_period_task | [AccountUpdate.TaskUpdate](#lq-AccountUpdate-TaskUpdate) |  |  |
| activity_random_task | [AccountUpdate.TaskUpdate](#lq-AccountUpdate-TaskUpdate) |  |  |
| challenge | [AccountUpdate.AccountChallengeUpdate](#lq-AccountUpdate-AccountChallengeUpdate) |  |  |
| ab_match | [AccountUpdate.AccountABMatchUpdate](#lq-AccountUpdate-AccountABMatchUpdate) |  |  |
| activity | [AccountActivityUpdate](#lq-AccountActivityUpdate) |  |  |
| activity_segment_task | [AccountUpdate.SegmentTaskUpdate](#lq-AccountUpdate-SegmentTaskUpdate) |  |  |
| month_ticket | [AccountUpdate.MonthTicketUpdate](#lq-AccountUpdate-MonthTicketUpdate) |  |  |
| main_character | [AccountUpdate.MainCharacterUpdate](#lq-AccountUpdate-MainCharacterUpdate) |  |  |
| badge | [AccountUpdate.BadgeUpdate](#lq-AccountUpdate-BadgeUpdate) |  |  |






<a name="lq-AccountUpdate-AccountABMatchUpdate"></a>

### AccountUpdate.AccountABMatchUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_id | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| buy_in_count | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |
| rewarded | [bool](#bool) |  |  |
| match_max_point | [AccountUpdate.AccountABMatchUpdate.MatchPoint](#lq-AccountUpdate-AccountABMatchUpdate-MatchPoint) | repeated |  |
| quit | [bool](#bool) |  |  |






<a name="lq-AccountUpdate-AccountABMatchUpdate-MatchPoint"></a>

### AccountUpdate.AccountABMatchUpdate.MatchPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| match_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-AccountUpdate-AccountChallengeUpdate"></a>

### AccountUpdate.AccountChallengeUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| level | [uint32](#uint32) |  |  |
| refresh_count | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |
| task_list | [uint32](#uint32) | repeated |  |
| rewarded_season | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-AchievementUpdate"></a>

### AccountUpdate.AchievementUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [AchievementProgress](#lq-AchievementProgress) | repeated |  |
| rewarded_group | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-BadgeUpdate"></a>

### AccountUpdate.BadgeUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [BadgeAchieveProgress](#lq-BadgeAchieveProgress) | repeated |  |






<a name="lq-AccountUpdate-CharacterUpdate"></a>

### AccountUpdate.CharacterUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| characters | [Character](#lq-Character) | repeated |  |
| skins | [uint32](#uint32) | repeated |  |
| finished_endings | [uint32](#uint32) | repeated |  |
| rewarded_endings | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-DailyTaskUpdate"></a>

### AccountUpdate.DailyTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-MainCharacterUpdate"></a>

### AccountUpdate.MainCharacterUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| skin_id | [uint32](#uint32) |  |  |






<a name="lq-AccountUpdate-MonthTicketUpdate"></a>

### AccountUpdate.MonthTicketUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| end_time | [uint32](#uint32) |  |  |
| last_pay_time | [uint32](#uint32) |  |  |






<a name="lq-AccountUpdate-NumericalUpdate"></a>

### AccountUpdate.NumericalUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |






<a name="lq-AccountUpdate-SegmentTaskUpdate"></a>

### AccountUpdate.SegmentTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [SegmentTaskProgress](#lq-SegmentTaskProgress) | repeated |  |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-TaskUpdate"></a>

### AccountUpdate.TaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| task_list | [uint32](#uint32) | repeated |  |






<a name="lq-AccountUpdate-TitleUpdate"></a>

### AccountUpdate.TitleUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new_titles | [uint32](#uint32) | repeated |  |
| remove_titles | [uint32](#uint32) | repeated |  |






<a name="lq-AchievementProgress"></a>

### AchievementProgress



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| counter | [uint32](#uint32) |  |  |
| achieved | [bool](#bool) |  |  |
| rewarded | [bool](#bool) |  |  |
| achieved_time | [uint32](#uint32) |  |  |






<a name="lq-Activity"></a>

### Activity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |






<a name="lq-ActivityAccumulatedPointData"></a>

### ActivityAccumulatedPointData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| point | [int32](#int32) |  |  |
| gained_reward_list | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityArenaData"></a>

### ActivityArenaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| win_count | [uint32](#uint32) |  |  |
| lose_count | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| enter_time | [uint32](#uint32) |  |  |
| daily_enter_count | [uint32](#uint32) |  |  |
| daily_enter_time | [uint32](#uint32) |  |  |
| max_win_count | [uint32](#uint32) |  |  |
| total_win_count | [uint32](#uint32) |  |  |






<a name="lq-ActivityBingoCardData"></a>

### ActivityBingoCardData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| card_id | [uint32](#uint32) |  |  |
| achieved_pos | [uint32](#uint32) | repeated |  |
| rewarded_ids | [uint32](#uint32) | repeated |  |
| state | [uint32](#uint32) |  |  |
| achieved_records | [ActivityBingoCardData.BingoAchievedRecord](#lq-ActivityBingoCardData-BingoAchievedRecord) | repeated |  |
| reward_records | [ActivityBingoCardData.BingoRewardRecord](#lq-ActivityBingoCardData-BingoRewardRecord) | repeated |  |






<a name="lq-ActivityBingoCardData-BingoAchievedRecord"></a>

### ActivityBingoCardData.BingoAchievedRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pos | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |






<a name="lq-ActivityBingoCardData-BingoRewardRecord"></a>

### ActivityBingoCardData.BingoRewardRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |






<a name="lq-ActivityBingoData"></a>

### ActivityBingoData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| cards | [ActivityBingoCardData](#lq-ActivityBingoCardData) | repeated |  |






<a name="lq-ActivityBuffData"></a>

### ActivityBuffData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityChooseGroupData"></a>

### ActivityChooseGroupData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| selection_id | [uint32](#uint32) |  |  |






<a name="lq-ActivityChooseUpData"></a>

### ActivityChooseUpData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| selection | [uint32](#uint32) |  |  |
| is_end | [uint32](#uint32) |  |  |






<a name="lq-ActivityCombiningData"></a>

### ActivityCombiningData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| workbench | [ActivityCombiningWorkbench](#lq-ActivityCombiningWorkbench) | repeated |  |
| orders | [ActivityCombiningOrderData](#lq-ActivityCombiningOrderData) | repeated |  |
| recycle_bin | [ActivityCombiningWorkbench](#lq-ActivityCombiningWorkbench) |  |  |
| menu | [ActivityCombiningMenuData](#lq-ActivityCombiningMenuData) |  |  |
| current_order_id | [uint32](#uint32) |  |  |
| bonus | [ActivityCombiningData.BonusData](#lq-ActivityCombiningData-BonusData) |  |  |
| unlocked_craft | [uint32](#uint32) | repeated |  |
| craft_pool | [ActivityCombiningPoolData](#lq-ActivityCombiningPoolData) | repeated |  |
| order_pool | [ActivityCombiningPoolData](#lq-ActivityCombiningPoolData) | repeated |  |






<a name="lq-ActivityCombiningData-BonusData"></a>

### ActivityCombiningData.BonusData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityCombiningLQData"></a>

### ActivityCombiningLQData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| workbench | [ActivityCombiningWorkbench](#lq-ActivityCombiningWorkbench) | repeated |  |
| orders | [ActivityCombiningOrderData](#lq-ActivityCombiningOrderData) | repeated |  |
| recycle_bin | [ActivityCombiningWorkbench](#lq-ActivityCombiningWorkbench) |  |  |
| unlocked_craft | [uint32](#uint32) | repeated |  |
| daily_bonus_count | [uint32](#uint32) |  |  |






<a name="lq-ActivityCombiningMenuData"></a>

### ActivityCombiningMenuData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| menu_group | [uint32](#uint32) |  |  |
| generated | [ActivityCombiningMenuData.MenuRequire](#lq-ActivityCombiningMenuData-MenuRequire) | repeated |  |
| multi_generated | [ActivityCombiningMenuData.MenuRequire](#lq-ActivityCombiningMenuData-MenuRequire) | repeated |  |






<a name="lq-ActivityCombiningMenuData-MenuRequire"></a>

### ActivityCombiningMenuData.MenuRequire



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ActivityCombiningOrderData"></a>

### ActivityCombiningOrderData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| char_id | [uint32](#uint32) |  |  |
| finished_craft_id | [uint32](#uint32) | repeated |  |
| craft_id | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityCombiningPoolData"></a>

### ActivityCombiningPoolData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ActivityCombiningWorkbench"></a>

### ActivityCombiningWorkbench



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| craft_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-ActivityFeedData"></a>

### ActivityFeedData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| feed_count | [uint32](#uint32) |  |  |
| friend_receive_data | [ActivityFeedData.CountWithTimeData](#lq-ActivityFeedData-CountWithTimeData) |  |  |
| friend_send_data | [ActivityFeedData.CountWithTimeData](#lq-ActivityFeedData-CountWithTimeData) |  |  |
| gift_inbox | [ActivityFeedData.GiftBoxData](#lq-ActivityFeedData-GiftBoxData) | repeated |  |
| max_inbox_id | [uint32](#uint32) |  |  |






<a name="lq-ActivityFeedData-CountWithTimeData"></a>

### ActivityFeedData.CountWithTimeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| last_update_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityFeedData-GiftBoxData"></a>

### ActivityFeedData.GiftBoxData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| from_account_id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| received | [uint32](#uint32) |  |  |






<a name="lq-ActivityFestivalData"></a>

### ActivityFestivalData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| proposal_list | [FestivalProposalData](#lq-FestivalProposalData) | repeated |  |
| event_list | [uint32](#uint32) | repeated |  |
| buy_record | [SignedTimeCounterData](#lq-SignedTimeCounterData) |  |  |






<a name="lq-ActivityFriendGiftData"></a>

### ActivityFriendGiftData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| max_inbox_id | [uint32](#uint32) |  |  |
| receive_data | [ActivityFriendGiftData.CountWithTimeData](#lq-ActivityFriendGiftData-CountWithTimeData) |  |  |
| send_data | [ActivityFriendGiftData.CountWithTimeData](#lq-ActivityFriendGiftData-CountWithTimeData) |  |  |
| gift_inbox | [ActivityFriendGiftData.GiftBoxData](#lq-ActivityFriendGiftData-GiftBoxData) | repeated |  |






<a name="lq-ActivityFriendGiftData-CountWithTimeData"></a>

### ActivityFriendGiftData.CountWithTimeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| last_update_time | [uint32](#uint32) |  |  |
| send_friend_id | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityFriendGiftData-GiftBoxData"></a>

### ActivityFriendGiftData.GiftBoxData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| from_account_id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| received | [uint32](#uint32) |  |  |






<a name="lq-ActivityGachaData"></a>

### ActivityGachaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| gained | [GachaRecord](#lq-GachaRecord) | repeated |  |






<a name="lq-ActivityGachaUpdateData"></a>

### ActivityGachaUpdateData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| gained | [GachaRecord](#lq-GachaRecord) | repeated |  |
| remain_count | [uint32](#uint32) |  |  |






<a name="lq-ActivityIdTimeRecord"></a>

### ActivityIdTimeRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |






<a name="lq-ActivityIslandData"></a>

### ActivityIslandData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| zone | [uint32](#uint32) |  |  |
| bags | [IslandBagData](#lq-IslandBagData) | repeated |  |
| zones | [IslandZoneData](#lq-IslandZoneData) | repeated |  |






<a name="lq-ActivityMMOData"></a>

### ActivityMMOData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| character | [ActivityMMOData.ActivityMMOCharacterData](#lq-ActivityMMOData-ActivityMMOCharacterData) |  |  |
| team | [ActivityMMOData.ActivityMMOTeamData](#lq-ActivityMMOData-ActivityMMOTeamData) |  |  |
| bag | [ActivityMMOData.ActivityMMOBagData](#lq-ActivityMMOData-ActivityMMOBagData) |  |  |
| map | [ActivityMMOData.ActivityMMOMapData](#lq-ActivityMMOData-ActivityMMOMapData) |  |  |
| support | [ActivityMMOData.ActivityMMOSupportData](#lq-ActivityMMOData-ActivityMMOSupportData) |  |  |






<a name="lq-ActivityMMOData-ActivityMMOBagData"></a>

### ActivityMMOData.ActivityMMOBagData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| equipments | [ActivityMMOEquipmentData](#lq-ActivityMMOEquipmentData) | repeated |  |
| total_gain_count | [uint32](#uint32) |  |  |
| total_fusion_count | [uint32](#uint32) |  |  |
| random_record | [ActivityMMOData.ActivityMMOBagData.ActivityMMORandomRecord](#lq-ActivityMMOData-ActivityMMOBagData-ActivityMMORandomRecord) | repeated |  |






<a name="lq-ActivityMMOData-ActivityMMOBagData-ActivityMMORandomRecord"></a>

### ActivityMMOData.ActivityMMOBagData.ActivityMMORandomRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rarity | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ActivityMMOData-ActivityMMOCharacterData"></a>

### ActivityMMOData.ActivityMMOCharacterData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityMMOData-ActivityMMOMapData"></a>

### ActivityMMOData.ActivityMMOMapData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| random_seed | [uint32](#uint32) |  |  |
| won | [uint32](#uint32) |  |  |
| failed | [uint32](#uint32) |  |  |






<a name="lq-ActivityMMOData-ActivityMMOSupportData"></a>

### ActivityMMOData.ActivityMMOSupportData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| last_receive_time | [uint32](#uint32) |  |  |
| most_supporter | [ActivityMMOSupportRecord](#lq-ActivityMMOSupportRecord) |  |  |
| receive_support_count | [uint32](#uint32) |  |  |
| support_record | [ActivityMMOSupportRecord](#lq-ActivityMMOSupportRecord) | repeated |  |






<a name="lq-ActivityMMOData-ActivityMMOTeamData"></a>

### ActivityMMOData.ActivityMMOTeamData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| members | [ActivityMMOTeamMember](#lq-ActivityMMOTeamMember) | repeated |  |
| friend_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| friend_list_expire | [uint32](#uint32) |  |  |
| random_friends | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |
| daily_update_time | [uint32](#uint32) |  |  |
| npc_list | [MMOActivityTeamCandidateData](#lq-MMOActivityTeamCandidateData) | repeated |  |






<a name="lq-ActivityMMODataChanges"></a>

### ActivityMMODataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| character | [ActivityMMODataChanges.ActivityMMOCharacterDataChanges](#lq-ActivityMMODataChanges-ActivityMMOCharacterDataChanges) |  |  |
| team | [ActivityMMODataChanges.ActivityMMOTeamDataChanges](#lq-ActivityMMODataChanges-ActivityMMOTeamDataChanges) |  |  |
| bag | [ActivityMMODataChanges.ActivityMMOBagDataChanges](#lq-ActivityMMODataChanges-ActivityMMOBagDataChanges) |  |  |
| map | [ActivityMMODataChanges.ActivityMMOMapDataChanges](#lq-ActivityMMODataChanges-ActivityMMOMapDataChanges) |  |  |
| support | [ActivityMMODataChanges.ActivityMMOSupportDataChanges](#lq-ActivityMMODataChanges-ActivityMMOSupportDataChanges) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOBagDataChanges"></a>

### ActivityMMODataChanges.ActivityMMOBagDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| equipments | [ActivityMMODataChanges.ActivityMMOEquipmentsArrayDirty](#lq-ActivityMMODataChanges-ActivityMMOEquipmentsArrayDirty) |  |  |
| total_gain_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| total_fusion_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOCharacterDataChanges"></a>

### ActivityMMODataChanges.ActivityMMOCharacterDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| equipments | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOEquipmentsArrayDirty"></a>

### ActivityMMODataChanges.ActivityMMOEquipmentsArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [ActivityMMOEquipmentData](#lq-ActivityMMOEquipmentData) | repeated |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOMapDataChanges"></a>

### ActivityMMODataChanges.ActivityMMOMapDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| random_seed | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| won | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| failed | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOSupportDataChanges"></a>

### ActivityMMODataChanges.ActivityMMOSupportDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| last_receive_time | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| most_supporter | [ActivityMMOSupportRecordDirty](#lq-ActivityMMOSupportRecordDirty) |  |  |
| receive_support_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOTeamDataChanges"></a>

### ActivityMMODataChanges.ActivityMMOTeamDataChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| members | [ActivityMMODataChanges.ActivityMMOTeamMemberArrayDirty](#lq-ActivityMMODataChanges-ActivityMMOTeamMemberArrayDirty) |  |  |






<a name="lq-ActivityMMODataChanges-ActivityMMOTeamMemberArrayDirty"></a>

### ActivityMMODataChanges.ActivityMMOTeamMemberArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [ActivityMMOTeamMember](#lq-ActivityMMOTeamMember) | repeated |  |






<a name="lq-ActivityMMOEquipmentData"></a>

### ActivityMMOEquipmentData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| stack | [uint32](#uint32) |  |  |






<a name="lq-ActivityMMOSupportRecord"></a>

### ActivityMMOSupportRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| character_id | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityMMOSupportRecordDirty"></a>

### ActivityMMOSupportRecordDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [ActivityMMOSupportRecord](#lq-ActivityMMOSupportRecord) |  |  |






<a name="lq-ActivityMMOTeamMember"></a>

### ActivityMMOTeamMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ActivityMarathonCheckData"></a>

### ActivityMarathonCheckData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round | [uint32](#uint32) |  |  |
| item | [uint32](#uint32) | repeated |  |
| tile | [string](#string) |  |  |
| tick | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |
| time_end | [uint32](#uint32) |  |  |






<a name="lq-ActivityMarathonData"></a>

### ActivityMarathonData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| highest_record | [MarathonGameRecord](#lq-MarathonGameRecord) |  |  |
| race_data | [ActivityMarathonData.MarathonRaceData](#lq-ActivityMarathonData-MarathonRaceData) |  |  |
| history | [ActivityMarathonData.MarathonRaceHistory](#lq-ActivityMarathonData-MarathonRaceHistory) | repeated |  |






<a name="lq-ActivityMarathonData-MarathonRaceData"></a>

### ActivityMarathonData.MarathonRaceData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| random_seed | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityMarathonData-MarathonRaceHistory"></a>

### ActivityMarathonData.MarathonRaceHistory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| race_data | [ActivityMarathonData.MarathonRaceData](#lq-ActivityMarathonData-MarathonRaceData) |  |  |
| record | [MarathonGameRecord](#lq-MarathonGameRecord) |  |  |






<a name="lq-ActivityProgressRewardData"></a>

### ActivityProgressRewardData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rewarded_progresses | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityQuestCrewChanges"></a>

### ActivityQuestCrewChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| members | [ActivityQuestCrewChanges.QCMemberArrayDirty](#lq-ActivityQuestCrewChanges-QCMemberArrayDirty) |  |  |
| quest_board | [ActivityQuestCrewChanges.QCQuestArrayDirty](#lq-ActivityQuestCrewChanges-QCQuestArrayDirty) |  |  |
| market_board | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |






<a name="lq-ActivityQuestCrewChanges-QCMemberArrayDirty"></a>

### ActivityQuestCrewChanges.QCMemberArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [QCMember](#lq-QCMember) | repeated |  |






<a name="lq-ActivityQuestCrewChanges-QCQuestArrayDirty"></a>

### ActivityQuestCrewChanges.QCQuestArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [QCQuest](#lq-QCQuest) | repeated |  |






<a name="lq-ActivityQuestCrewData"></a>

### ActivityQuestCrewData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| members | [QCMember](#lq-QCMember) | repeated |  |
| quest_board | [QCQuest](#lq-QCQuest) | repeated |  |
| market_board | [uint32](#uint32) | repeated |  |






<a name="lq-ActivityQuestCrewEffectResult"></a>

### ActivityQuestCrewEffectResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| result_change | [ActivityQuestCrewEffectResult.QCQuestResultChange](#lq-ActivityQuestCrewEffectResult-QCQuestResultChange) |  |  |
| consumed_change | [ActivityQuestCrewEffectResult.QCQuestConsumeChange](#lq-ActivityQuestCrewEffectResult-QCQuestConsumeChange) | repeated |  |
| reward | [ActivityQuestCrewEffectResult.QCItemReward](#lq-ActivityQuestCrewEffectResult-QCItemReward) |  |  |






<a name="lq-ActivityQuestCrewEffectResult-QCItemReward"></a>

### ActivityQuestCrewEffectResult.QCItemReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| execute_reward | [ExecuteReward](#lq-ExecuteReward) | repeated |  |






<a name="lq-ActivityQuestCrewEffectResult-QCQuestConsumeChange"></a>

### ActivityQuestCrewEffectResult.QCQuestConsumeChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| member_id | [uint32](#uint32) |  |  |
| from | [uint32](#uint32) |  |  |
| to | [uint32](#uint32) |  |  |






<a name="lq-ActivityQuestCrewEffectResult-QCQuestResultChange"></a>

### ActivityQuestCrewEffectResult.QCQuestResultChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [uint32](#uint32) |  |  |
| to | [uint32](#uint32) |  |  |






<a name="lq-ActivityRankPointData"></a>

### ActivityRankPointData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_id | [uint32](#uint32) |  |  |
| point | [int32](#int32) |  |  |
| gained_reward | [bool](#bool) |  |  |
| gainable_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityShootData"></a>

### ActivityShootData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| enemies | [ActivityShootEnemyInfo](#lq-ActivityShootEnemyInfo) | repeated |  |
| rewarded_ids | [uint32](#uint32) | repeated |  |
| ended | [bool](#bool) |  |  |
| rewarded_records | [ActivityShootRewardRecord](#lq-ActivityShootRewardRecord) | repeated |  |






<a name="lq-ActivityShootEnemyInfo"></a>

### ActivityShootEnemyInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| enemy_id | [uint32](#uint32) |  |  |
| hp | [uint32](#uint32) |  |  |






<a name="lq-ActivityShootEnemyInfoDirty"></a>

### ActivityShootEnemyInfoDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [uint32](#uint32) |  |  |
| enemies | [ActivityShootEnemyInfo](#lq-ActivityShootEnemyInfo) | repeated |  |






<a name="lq-ActivityShootRewardRecord"></a>

### ActivityShootRewardRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enemy_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| rewarded_time | [uint32](#uint32) |  |  |






<a name="lq-ActivityShootValueChange"></a>

### ActivityShootValueChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [ActivityShootValueChange.Uint32ValueDirty](#lq-ActivityShootValueChange-Uint32ValueDirty) |  |  |
| enemies | [ActivityShootEnemyInfoDirty](#lq-ActivityShootEnemyInfoDirty) |  |  |
| rewarded_ids | [ActivityShootValueChange.RewardArrayDirty](#lq-ActivityShootValueChange-RewardArrayDirty) |  |  |






<a name="lq-ActivityShootValueChange-RewardArrayDirty"></a>

### ActivityShootValueChange.RewardArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reward_ids | [uint32](#uint32) | repeated |  |
| dirty | [uint32](#uint32) |  |  |






<a name="lq-ActivityShootValueChange-Uint32ValueDirty"></a>

### ActivityShootValueChange.Uint32ValueDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [uint32](#uint32) |  |  |
| dirty | [uint32](#uint32) |  |  |






<a name="lq-ActivitySimulationDailyContest"></a>

### ActivitySimulationDailyContest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| day | [uint32](#uint32) |  |  |
| characters | [uint32](#uint32) | repeated |  |
| records | [ActivitySimulationGameRecord](#lq-ActivitySimulationGameRecord) | repeated |  |
| round | [uint32](#uint32) |  |  |






<a name="lq-ActivitySimulationData"></a>

### ActivitySimulationData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| stats | [uint32](#uint32) | repeated |  |
| stamina_update_time | [uint32](#uint32) |  |  |
| daily_contest | [ActivitySimulationDailyContest](#lq-ActivitySimulationDailyContest) | repeated |  |
| train_records | [ActivitySimulationTrainRecord](#lq-ActivitySimulationTrainRecord) | repeated |  |






<a name="lq-ActivitySimulationGameRecord"></a>

### ActivitySimulationGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round | [uint32](#uint32) |  |  |
| seats | [uint32](#uint32) | repeated |  |
| uuid | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| scores | [int32](#int32) | repeated |  |
| messages | [ActivitySimulationGameRecordMessage](#lq-ActivitySimulationGameRecordMessage) | repeated |  |






<a name="lq-ActivitySimulationGameRecordMessage"></a>

### ActivitySimulationGameRecordMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| args | [uint32](#uint32) | repeated |  |
| xun | [uint32](#uint32) |  |  |






<a name="lq-ActivitySimulationTrainRecord"></a>

### ActivitySimulationTrainRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time | [uint32](#uint32) |  |  |
| modify_stats | [int32](#int32) | repeated |  |
| final_stats | [uint32](#uint32) | repeated |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-ActivitySnowballData"></a>

### ActivitySnowballData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| upgrade | [ActivitySnowballUpgrade](#lq-ActivitySnowballUpgrade) | repeated |  |
| rewarded_level | [uint32](#uint32) | repeated |  |
| finished_level | [uint32](#uint32) | repeated |  |
| random_seed | [uint32](#uint32) |  |  |
| battle_id | [string](#string) |  |  |
| level_finished_count | [uint32](#uint32) |  |  |
| player_combo | [uint32](#uint32) |  |  |
| reward_records | [ActivityIdTimeRecord](#lq-ActivityIdTimeRecord) | repeated |  |
| finish_records | [ActivityIdTimeRecord](#lq-ActivityIdTimeRecord) | repeated |  |






<a name="lq-ActivitySnowballPlayerAction"></a>

### ActivitySnowballPlayerAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tick | [uint32](#uint32) |  |  |
| track | [uint32](#uint32) |  |  |






<a name="lq-ActivitySnowballPlayerAttackedInfo"></a>

### ActivitySnowballPlayerAttackedInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target | [uint32](#uint32) |  |  |
| track | [uint32](#uint32) |  |  |
| damage | [uint32](#uint32) |  |  |
| critia | [uint32](#uint32) |  |  |






<a name="lq-ActivitySnowballPlayerState"></a>

### ActivitySnowballPlayerState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| player | [uint32](#uint32) |  |  |
| hp | [uint32](#uint32) |  |  |
| mp | [uint32](#uint32) |  |  |






<a name="lq-ActivitySnowballUpgrade"></a>

### ActivitySnowballUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-ActivitySnowballUpgradeDirty"></a>

### ActivitySnowballUpgradeDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [ActivitySnowballUpgrade](#lq-ActivitySnowballUpgrade) | repeated |  |
| dirty | [bool](#bool) |  |  |






<a name="lq-ActivitySnowballValueChanges"></a>

### ActivitySnowballValueChanges



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| upgrade | [ActivitySnowballUpgradeDirty](#lq-ActivitySnowballUpgradeDirty) |  |  |
| rewarded_level | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| finished_level | [UInt32ArrayDirty](#lq-UInt32ArrayDirty) |  |  |
| level_finished_count | [UInt32Dirty](#lq-UInt32Dirty) |  |  |
| player_combo | [UInt32Dirty](#lq-UInt32Dirty) |  |  |






<a name="lq-ActivitySpotData"></a>

### ActivitySpotData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| spots | [ActivitySpotData.SpotData](#lq-ActivitySpotData-SpotData) | repeated |  |






<a name="lq-ActivitySpotData-SpotData"></a>

### ActivitySpotData.SpotData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| rewarded | [uint32](#uint32) |  |  |
| unlocked_ending | [uint32](#uint32) | repeated |  |
| unlocked | [uint32](#uint32) |  |  |






<a name="lq-ActivityStoryData"></a>

### ActivityStoryData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| unlocked_story | [UnlockedStoryData](#lq-UnlockedStoryData) | repeated |  |






<a name="lq-ActivityUpgradeData"></a>

### ActivityUpgradeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| groups | [ActivityUpgradeData.LevelGroup](#lq-ActivityUpgradeData-LevelGroup) | repeated |  |
| received_level | [uint32](#uint32) |  |  |






<a name="lq-ActivityUpgradeData-LevelGroup"></a>

### ActivityUpgradeData.LevelGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |






<a name="lq-ActivityVillageData"></a>

### ActivityVillageData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| buildings | [VillageBuildingData](#lq-VillageBuildingData) | repeated |  |
| trip | [VillageTripData](#lq-VillageTripData) | repeated |  |
| tasks | [VillageTaskData](#lq-VillageTaskData) | repeated |  |
| round | [uint32](#uint32) |  |  |






<a name="lq-Announcement"></a>

### Announcement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| title | [string](#string) |  |  |
| content | [string](#string) |  |  |
| header_image | [string](#string) |  |  |






<a name="lq-AntiAddiction"></a>

### AntiAddiction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| online_duration | [uint32](#uint32) |  |  |






<a name="lq-BadgeAchieveProgress"></a>

### BadgeAchieveProgress



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| counter | [uint32](#uint32) |  |  |
| achieved_counter | [uint32](#uint32) |  |  |
| achieved_time | [uint32](#uint32) |  |  |






<a name="lq-Bag"></a>

### Bag



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [Item](#lq-Item) | repeated |  |
| daily_gain_record | [ItemGainRecords](#lq-ItemGainRecords) | repeated |  |






<a name="lq-BagUpdate"></a>

### BagUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| update_items | [Item](#lq-Item) | repeated |  |
| update_daily_gain_record | [ItemGainRecords](#lq-ItemGainRecords) | repeated |  |






<a name="lq-BannerActivityData"></a>

### BannerActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| tag_img_url | [string](#string) |  |  |
| banner_background_url | [string](#string) |  |  |
| banner_button_url | [string](#string) |  |  |
| tag_name | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| url | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| need_popout | [uint32](#uint32) |  |  |






<a name="lq-BillShortcut"></a>

### BillShortcut



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| dealPrice | [uint32](#uint32) |  |  |






<a name="lq-BillingGoods"></a>

### BillingGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| name | [string](#string) |  |  |
| desc | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| resource_id | [uint32](#uint32) |  |  |
| resource_count | [uint32](#uint32) |  |  |






<a name="lq-BillingProduct"></a>

### BillingProduct



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods | [BillingGoods](#lq-BillingGoods) |  |  |
| currency_code | [string](#string) |  |  |
| currency_price | [uint32](#uint32) |  |  |
| sort_weight | [uint32](#uint32) |  |  |






<a name="lq-BuyRecord"></a>

### BuyRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ChangeNicknameRecord"></a>

### ChangeNicknameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [string](#string) |  |  |
| to | [string](#string) |  |  |
| time | [uint32](#uint32) |  |  |






<a name="lq-Character"></a>

### Character



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| charid | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| views | [ViewSlot](#lq-ViewSlot) | repeated |  |
| skin | [uint32](#uint32) |  |  |
| is_upgraded | [bool](#bool) |  |  |
| extra_emoji | [uint32](#uint32) | repeated |  |
| rewarded_level | [uint32](#uint32) | repeated |  |






<a name="lq-ChestData"></a>

### ChestData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| total_open_count | [uint32](#uint32) |  |  |
| consume_count | [uint32](#uint32) |  |  |
| face_black_count | [uint32](#uint32) |  |  |






<a name="lq-ChestDataV2"></a>

### ChestDataV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| total_open_count | [uint32](#uint32) |  |  |
| face_black_count | [uint32](#uint32) |  |  |
| ticket_face_black_count | [uint32](#uint32) |  |  |






<a name="lq-ClientDeviceInfo"></a>

### ClientDeviceInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| platform | [string](#string) |  |  |
| hardware | [string](#string) |  |  |
| os | [string](#string) |  |  |
| os_version | [string](#string) |  |  |
| is_browser | [bool](#bool) |  |  |
| software | [string](#string) |  |  |
| sale_platform | [string](#string) |  |  |
| hardware_vendor | [string](#string) |  |  |
| model_number | [string](#string) |  |  |
| screen_width | [uint32](#uint32) |  |  |
| screen_height | [uint32](#uint32) |  |  |
| user_agent | [string](#string) |  |  |
| screen_type | [uint32](#uint32) |  |  |






<a name="lq-ClientDeviceInfoLog"></a>

### ClientDeviceInfoLog



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| device_info | [ClientDeviceInfo](#lq-ClientDeviceInfo) |  |  |
| login_time | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |






<a name="lq-ClientVersionInfo"></a>

### ClientVersionInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource | [string](#string) |  |  |
| package | [string](#string) |  |  |






<a name="lq-CommentItem"></a>

### CommentItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| comment_id | [uint32](#uint32) |  |  |
| timestamp | [uint32](#uint32) |  |  |
| commenter | [PlayerBaseView](#lq-PlayerBaseView) |  |  |
| content | [string](#string) |  |  |
| is_banned | [uint32](#uint32) |  |  |






<a name="lq-ContestDetailRule"></a>

### ContestDetailRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| init_point | [uint32](#uint32) |  |  |
| fandian | [uint32](#uint32) |  |  |
| can_jifei | [bool](#bool) |  |  |
| tianbian_value | [uint32](#uint32) |  |  |
| liqibang_value | [uint32](#uint32) |  |  |
| changbang_value | [uint32](#uint32) |  |  |
| noting_fafu_1 | [uint32](#uint32) |  |  |
| noting_fafu_2 | [uint32](#uint32) |  |  |
| noting_fafu_3 | [uint32](#uint32) |  |  |
| have_liujumanguan | [bool](#bool) |  |  |
| have_qieshangmanguan | [bool](#bool) |  |  |
| have_biao_dora | [bool](#bool) |  |  |
| have_gang_biao_dora | [bool](#bool) |  |  |
| ming_dora_immediately_open | [bool](#bool) |  |  |
| have_li_dora | [bool](#bool) |  |  |
| have_gang_li_dora | [bool](#bool) |  |  |
| have_sifenglianda | [bool](#bool) |  |  |
| have_sigangsanle | [bool](#bool) |  |  |
| have_sijializhi | [bool](#bool) |  |  |
| have_jiuzhongjiupai | [bool](#bool) |  |  |
| have_sanjiahele | [bool](#bool) |  |  |
| have_toutiao | [bool](#bool) |  |  |
| have_helelianzhuang | [bool](#bool) |  |  |
| have_helezhongju | [bool](#bool) |  |  |
| have_tingpailianzhuang | [bool](#bool) |  |  |
| have_tingpaizhongju | [bool](#bool) |  |  |
| have_yifa | [bool](#bool) |  |  |
| have_nanruxiru | [bool](#bool) |  |  |
| jingsuanyuandian | [uint32](#uint32) |  |  |
| shunweima_2 | [int32](#int32) |  |  |
| shunweima_3 | [int32](#int32) |  |  |
| shunweima_4 | [int32](#int32) |  |  |
| bianjietishi | [bool](#bool) |  |  |
| ai_level | [uint32](#uint32) |  |  |
| have_zimosun | [bool](#bool) |  |  |
| disable_multi_yukaman | [bool](#bool) |  |  |
| guyi_mode | [uint32](#uint32) |  |  |
| disable_leijiyiman | [bool](#bool) |  |  |
| dora3_mode | [uint32](#uint32) |  |  |
| xuezhandaodi | [uint32](#uint32) |  |  |
| huansanzhang | [uint32](#uint32) |  |  |
| chuanma | [uint32](#uint32) |  |  |
| disable_double_yakuman | [uint32](#uint32) |  |  |
| disable_composite_yakuman | [uint32](#uint32) |  |  |
| enable_shiti | [uint32](#uint32) |  |  |
| enable_nontsumo_liqi | [uint32](#uint32) |  |  |
| disable_double_wind_four_fu | [uint32](#uint32) |  |  |
| disable_angang_guoshi | [uint32](#uint32) |  |  |
| enable_renhe | [uint32](#uint32) |  |  |
| enable_baopai_extend_settings | [uint32](#uint32) |  |  |
| fanfu | [uint32](#uint32) |  |  |






<a name="lq-ContestDetailRuleV2"></a>

### ContestDetailRuleV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_rule | [ContestDetailRule](#lq-ContestDetailRule) |  |  |
| extra_rule | [ContestDetailRuleV2.ExtraRule](#lq-ContestDetailRuleV2-ExtraRule) |  |  |






<a name="lq-ContestDetailRuleV2-ExtraRule"></a>

### ContestDetailRuleV2.ExtraRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| required_level | [uint32](#uint32) |  |  |
| max_game_count | [uint32](#uint32) |  |  |






<a name="lq-ContestGameMetaData"></a>

### ContestGameMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type_list | [ContestGameMetaData.ContestTypeZoneData](#lq-ContestGameMetaData-ContestTypeZoneData) | repeated |  |
| rank_type | [uint32](#uint32) |  |  |






<a name="lq-ContestGameMetaData-ContestTypeZoneData"></a>

### ContestGameMetaData.ContestTypeZoneData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| zone | [uint32](#uint32) |  |  |
| contest_type | [uint32](#uint32) |  |  |






<a name="lq-CustomizedContestAbstract"></a>

### CustomizedContestAbstract



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| contest_id | [uint32](#uint32) |  |  |
| contest_name | [string](#string) |  |  |
| state | [uint32](#uint32) |  |  |
| creator_id | [uint32](#uint32) |  |  |
| create_time | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| finish_time | [uint32](#uint32) |  |  |
| open | [bool](#bool) |  |  |
| public_notice | [string](#string) |  |  |
| contest_type | [uint32](#uint32) |  |  |






<a name="lq-CustomizedContestBase"></a>

### CustomizedContestBase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| contest_id | [uint32](#uint32) |  |  |
| contest_name | [string](#string) |  |  |
| state | [uint32](#uint32) |  |  |
| creator_id | [uint32](#uint32) |  |  |
| create_time | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| finish_time | [uint32](#uint32) |  |  |
| open | [bool](#bool) |  |  |
| contest_type | [uint32](#uint32) |  |  |
| public_notice | [string](#string) |  |  |
| check_state | [uint32](#uint32) |  |  |
| checking_name | [string](#string) |  |  |
| rank_type | [uint32](#uint32) |  |  |
| show_team_rank | [bool](#bool) |  |  |






<a name="lq-CustomizedContestDetail"></a>

### CustomizedContestDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| contest_id | [uint32](#uint32) |  |  |
| contest_name | [string](#string) |  |  |
| state | [uint32](#uint32) |  |  |
| create_time | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| finish_time | [uint32](#uint32) |  |  |
| open | [bool](#bool) |  |  |
| rank_rule | [uint32](#uint32) |  |  |
| game_mode | [GameMode](#lq-GameMode) |  |  |
| private_notice | [string](#string) |  |  |
| observer_switch | [uint32](#uint32) |  |  |
| emoji_switch | [uint32](#uint32) |  |  |
| contest_type | [uint32](#uint32) |  |  |
| disable_broadcast | [uint32](#uint32) |  |  |
| signup_start_time | [uint32](#uint32) |  |  |
| signup_end_time | [uint32](#uint32) |  |  |
| signup_type | [uint32](#uint32) |  |  |
| auto_match | [uint32](#uint32) |  |  |
| rank_type | [uint32](#uint32) |  |  |
| show_team_rank | [bool](#bool) |  |  |
| tied_rank | [uint32](#uint32) |  |  |
| match_start_time | [uint32](#uint32) |  |  |
| match_end_time | [uint32](#uint32) |  |  |
| open_rank_percent | [uint32](#uint32) |  |  |






<a name="lq-CustomizedContestExtend"></a>

### CustomizedContestExtend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| public_notice | [string](#string) |  |  |






<a name="lq-CustomizedContestGameEnd"></a>

### CustomizedContestGameEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| players | [CustomizedContestGameEnd.Item](#lq-CustomizedContestGameEnd-Item) | repeated |  |






<a name="lq-CustomizedContestGameEnd-Item"></a>

### CustomizedContestGameEnd.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| total_point | [int32](#int32) |  |  |






<a name="lq-CustomizedContestGamePlan"></a>

### CustomizedContestGamePlan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |
| ready_players | [uint32](#uint32) | repeated |  |
| account_ids | [uint32](#uint32) | repeated |  |
| game_start_time | [uint32](#uint32) |  |  |
| expired_time | [uint32](#uint32) |  |  |






<a name="lq-CustomizedContestGameStart"></a>

### CustomizedContestGameStart



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| players | [CustomizedContestGameStart.Item](#lq-CustomizedContestGameStart-Item) | repeated |  |






<a name="lq-CustomizedContestGameStart-Item"></a>

### CustomizedContestGameStart.Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |






<a name="lq-CustomizedContestPlayerReport"></a>

### CustomizedContestPlayerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank_rule | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| point | [int32](#int32) |  |  |
| game_ranks | [uint32](#uint32) | repeated |  |
| total_game_count | [uint32](#uint32) |  |  |
| rank_percent | [uint32](#uint32) |  |  |






<a name="lq-Error"></a>

### Error



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [uint32](#uint32) |  |  |
| u32_params | [uint32](#uint32) | repeated |  |
| str_params | [string](#string) | repeated |  |
| json_param | [string](#string) |  |  |
| level | [uint32](#uint32) |  |  |
| message | [string](#string) |  |  |






<a name="lq-ExchangeRecord"></a>

### ExchangeRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| exchange_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ExecuteResult"></a>

### ExecuteResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [int32](#int32) |  |  |






<a name="lq-ExecuteReward"></a>

### ExecuteReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reward | [RewardSlot](#lq-RewardSlot) |  |  |
| replace | [RewardSlot](#lq-RewardSlot) |  |  |
| replace_count | [uint32](#uint32) |  |  |






<a name="lq-FaithData"></a>

### FaithData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| faith_id | [uint32](#uint32) |  |  |
| total_open_count | [uint32](#uint32) |  |  |
| consume_count | [uint32](#uint32) |  |  |
| modify_count | [int32](#int32) |  |  |






<a name="lq-FakeRandomRecords"></a>

### FakeRandomRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| special_item_id | [uint32](#uint32) |  |  |
| gain_count | [uint32](#uint32) |  |  |
| gain_history | [uint32](#uint32) | repeated |  |






<a name="lq-FavoriteHu"></a>

### FavoriteHu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| hu | [HighestHuRecord](#lq-HighestHuRecord) |  |  |
| mode | [uint32](#uint32) |  |  |






<a name="lq-FeedActivityData"></a>

### FeedActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| feed_count | [uint32](#uint32) |  |  |
| friend_receive_data | [FeedActivityData.CountWithTimeData](#lq-FeedActivityData-CountWithTimeData) |  |  |
| friend_send_data | [FeedActivityData.CountWithTimeData](#lq-FeedActivityData-CountWithTimeData) |  |  |
| gift_inbox | [FeedActivityData.GiftBoxData](#lq-FeedActivityData-GiftBoxData) | repeated |  |






<a name="lq-FeedActivityData-CountWithTimeData"></a>

### FeedActivityData.CountWithTimeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| last_update_time | [uint32](#uint32) |  |  |






<a name="lq-FeedActivityData-GiftBoxData"></a>

### FeedActivityData.GiftBoxData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| from_account_id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| received | [uint32](#uint32) |  |  |






<a name="lq-FestivalProposalData"></a>

### FestivalProposalData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| proposal_id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) |  |  |






<a name="lq-Friend"></a>

### Friend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| base | [PlayerBaseView](#lq-PlayerBaseView) |  |  |
| state | [AccountActiveState](#lq-AccountActiveState) |  |  |
| remark | [string](#string) |  |  |






<a name="lq-GachaRecord"></a>

### GachaRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-GameConfig"></a>

### GameConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [uint32](#uint32) |  |  |
| mode | [GameMode](#lq-GameMode) |  |  |
| meta | [GameMetaData](#lq-GameMetaData) |  |  |






<a name="lq-GameConnectInfo"></a>

### GameConnectInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| connect_token | [string](#string) |  |  |
| game_uuid | [string](#string) |  |  |
| location | [string](#string) |  |  |






<a name="lq-GameDetailRule"></a>

### GameDetailRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_fixed | [uint32](#uint32) |  |  |
| time_add | [uint32](#uint32) |  |  |
| dora_count | [uint32](#uint32) |  |  |
| shiduan | [uint32](#uint32) |  |  |
| init_point | [uint32](#uint32) |  |  |
| fandian | [uint32](#uint32) |  |  |
| can_jifei | [bool](#bool) |  |  |
| tianbian_value | [uint32](#uint32) |  |  |
| liqibang_value | [uint32](#uint32) |  |  |
| changbang_value | [uint32](#uint32) |  |  |
| noting_fafu_1 | [uint32](#uint32) |  |  |
| noting_fafu_2 | [uint32](#uint32) |  |  |
| noting_fafu_3 | [uint32](#uint32) |  |  |
| have_liujumanguan | [bool](#bool) |  |  |
| have_qieshangmanguan | [bool](#bool) |  |  |
| have_biao_dora | [bool](#bool) |  |  |
| have_gang_biao_dora | [bool](#bool) |  |  |
| ming_dora_immediately_open | [bool](#bool) |  |  |
| have_li_dora | [bool](#bool) |  |  |
| have_gang_li_dora | [bool](#bool) |  |  |
| have_sifenglianda | [bool](#bool) |  |  |
| have_sigangsanle | [bool](#bool) |  |  |
| have_sijializhi | [bool](#bool) |  |  |
| have_jiuzhongjiupai | [bool](#bool) |  |  |
| have_sanjiahele | [bool](#bool) |  |  |
| have_toutiao | [bool](#bool) |  |  |
| have_helelianzhuang | [bool](#bool) |  |  |
| have_helezhongju | [bool](#bool) |  |  |
| have_tingpailianzhuang | [bool](#bool) |  |  |
| have_tingpaizhongju | [bool](#bool) |  |  |
| have_yifa | [bool](#bool) |  |  |
| have_nanruxiru | [bool](#bool) |  |  |
| jingsuanyuandian | [uint32](#uint32) |  |  |
| shunweima_2 | [int32](#int32) |  |  |
| shunweima_3 | [int32](#int32) |  |  |
| shunweima_4 | [int32](#int32) |  |  |
| bianjietishi | [bool](#bool) |  |  |
| ai_level | [uint32](#uint32) |  |  |
| have_zimosun | [bool](#bool) |  |  |
| disable_multi_yukaman | [bool](#bool) |  |  |
| fanfu | [uint32](#uint32) |  |  |
| guyi_mode | [uint32](#uint32) |  |  |
| dora3_mode | [uint32](#uint32) |  |  |
| begin_open_mode | [uint32](#uint32) |  |  |
| jiuchao_mode | [uint32](#uint32) |  |  |
| muyu_mode | [uint32](#uint32) |  |  |
| open_hand | [uint32](#uint32) |  |  |
| xuezhandaodi | [uint32](#uint32) |  |  |
| huansanzhang | [uint32](#uint32) |  |  |
| chuanma | [uint32](#uint32) |  |  |
| reveal_discard | [uint32](#uint32) |  |  |
| field_spell_mode | [uint32](#uint32) |  |  |
| zhanxing | [uint32](#uint32) |  |  |
| tianming_mode | [uint32](#uint32) |  |  |
| disable_leijiyiman | [bool](#bool) |  |  |
| disable_double_yakuman | [uint32](#uint32) |  |  |
| disable_composite_yakuman | [uint32](#uint32) |  |  |
| enable_shiti | [uint32](#uint32) |  |  |
| enable_nontsumo_liqi | [uint32](#uint32) |  |  |
| disable_double_wind_four_fu | [uint32](#uint32) |  |  |
| disable_angang_guoshi | [uint32](#uint32) |  |  |
| enable_renhe | [uint32](#uint32) |  |  |
| enable_baopai_extend_settings | [uint32](#uint32) |  |  |
| yongchang_mode | [uint32](#uint32) |  |  |
| hunzhiyiji_mode | [uint32](#uint32) |  |  |
| wanxiangxiuluo_mode | [uint32](#uint32) |  |  |
| beishuizhizhan_mode | [uint32](#uint32) |  |  |
| amusement_switches | [uint32](#uint32) | repeated |  |






<a name="lq-GameEndAction"></a>

### GameEndAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [uint32](#uint32) |  |  |






<a name="lq-GameEndResult"></a>

### GameEndResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| players | [GameEndResult.PlayerItem](#lq-GameEndResult-PlayerItem) | repeated |  |






<a name="lq-GameEndResult-PlayerItem"></a>

### GameEndResult.PlayerItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| total_point | [int32](#int32) |  |  |
| part_point_1 | [int32](#int32) |  |  |
| part_point_2 | [int32](#int32) |  |  |
| grading_score | [int32](#int32) |  |  |
| gold | [int32](#int32) |  |  |






<a name="lq-GameFinalSnapshot"></a>

### GameFinalSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| state | [uint32](#uint32) |  |  |
| category | [uint32](#uint32) |  |  |
| mode | [GameMode](#lq-GameMode) |  |  |
| meta | [GameMetaData](#lq-GameMetaData) |  |  |
| calculate_param | [GameFinalSnapshot.CalculateParam](#lq-GameFinalSnapshot-CalculateParam) |  |  |
| create_time | [uint32](#uint32) |  |  |
| start_time | [uint32](#uint32) |  |  |
| finish_time | [uint32](#uint32) |  |  |
| seats | [GameFinalSnapshot.GameSeat](#lq-GameFinalSnapshot-GameSeat) | repeated |  |
| rounds | [GameRoundSnapshot](#lq-GameRoundSnapshot) | repeated |  |
| account_views | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| final_players | [GameFinalSnapshot.FinalPlayer](#lq-GameFinalSnapshot-FinalPlayer) | repeated |  |
| afk_info | [GameFinalSnapshot.AFKInfo](#lq-GameFinalSnapshot-AFKInfo) | repeated |  |
| robot_views | [PlayerGameView](#lq-PlayerGameView) | repeated |  |






<a name="lq-GameFinalSnapshot-AFKInfo"></a>

### GameFinalSnapshot.AFKInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| deal_tile_count | [uint32](#uint32) |  |  |
| moqie_count | [uint32](#uint32) |  |  |
| seat | [uint32](#uint32) |  |  |






<a name="lq-GameFinalSnapshot-CalculateParam"></a>

### GameFinalSnapshot.CalculateParam



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| init_point | [uint32](#uint32) |  |  |
| jingsuanyuandian | [uint32](#uint32) |  |  |
| rank_points | [int32](#int32) | repeated |  |






<a name="lq-GameFinalSnapshot-FinalPlayer"></a>

### GameFinalSnapshot.FinalPlayer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| total_point | [int32](#int32) |  |  |
| part_point_1 | [int32](#int32) |  |  |
| part_point_2 | [int32](#int32) |  |  |
| grading_score | [int32](#int32) |  |  |
| gold | [int32](#int32) |  |  |






<a name="lq-GameFinalSnapshot-GameSeat"></a>

### GameFinalSnapshot.GameSeat



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| notify_endpoint | [NetworkEndpoint](#lq-NetworkEndpoint) |  |  |
| client_address | [string](#string) |  |  |
| is_connected | [bool](#bool) |  |  |






<a name="lq-GameLiveHead"></a>

### GameLiveHead



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| game_config | [GameConfig](#lq-GameConfig) |  |  |
| players | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| seat_list | [uint32](#uint32) | repeated |  |






<a name="lq-GameLiveSegment"></a>

### GameLiveSegment



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| actions | [GameLiveUnit](#lq-GameLiveUnit) | repeated |  |






<a name="lq-GameLiveSegmentUri"></a>

### GameLiveSegmentUri



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| segment_id | [uint32](#uint32) |  |  |
| segment_uri | [string](#string) |  |  |






<a name="lq-GameLiveUnit"></a>

### GameLiveUnit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [uint32](#uint32) |  |  |
| action_category | [uint32](#uint32) |  |  |
| action_data | [bytes](#bytes) |  |  |






<a name="lq-GameMetaData"></a>

### GameMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| room_id | [uint32](#uint32) |  |  |
| mode_id | [uint32](#uint32) |  |  |
| contest_uid | [uint32](#uint32) |  |  |
| contest_info | [ContestGameMetaData](#lq-ContestGameMetaData) |  |  |






<a name="lq-GameMode"></a>

### GameMode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode | [uint32](#uint32) |  |  |
| ai | [bool](#bool) |  |  |
| extendinfo | [string](#string) |  |  |
| detail_rule | [GameDetailRule](#lq-GameDetailRule) |  |  |
| testing_environment | [GameTestingEnvironmentSet](#lq-GameTestingEnvironmentSet) |  |  |
| game_setting | [GameSetting](#lq-GameSetting) |  |  |






<a name="lq-GameNewRoundState"></a>

### GameNewRoundState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat_states | [uint32](#uint32) | repeated |  |






<a name="lq-GameNoopAction"></a>

### GameNoopAction







<a name="lq-GameRoundHuData"></a>

### GameRoundHuData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hupai | [GameRoundHuData.HuPai](#lq-GameRoundHuData-HuPai) |  |  |
| fans | [GameRoundHuData.Fan](#lq-GameRoundHuData-Fan) | repeated |  |
| score | [uint32](#uint32) |  |  |
| xun | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |
| fan_sum | [uint32](#uint32) |  |  |
| fu_sum | [uint32](#uint32) |  |  |
| yakuman_count | [uint32](#uint32) |  |  |
| biao_dora_count | [uint32](#uint32) |  |  |
| red_dora_count | [uint32](#uint32) |  |  |
| li_dora_count | [uint32](#uint32) |  |  |
| babei_count | [uint32](#uint32) |  |  |
| xuan_shang_count | [uint32](#uint32) |  |  |
| pai_left_count | [uint32](#uint32) |  |  |






<a name="lq-GameRoundHuData-Fan"></a>

### GameRoundHuData.Fan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| fan | [uint32](#uint32) |  |  |






<a name="lq-GameRoundHuData-HuPai"></a>

### GameRoundHuData.HuPai



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| seat | [uint32](#uint32) |  |  |
| liqi | [uint32](#uint32) |  |  |






<a name="lq-GameRoundPlayer"></a>

### GameRoundPlayer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| score | [int32](#int32) |  |  |
| rank | [uint32](#uint32) |  |  |
| result | [GameRoundPlayerResult](#lq-GameRoundPlayerResult) |  |  |






<a name="lq-GameRoundPlayerFangChongInfo"></a>

### GameRoundPlayerFangChongInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| pai_left_count | [uint32](#uint32) |  |  |






<a name="lq-GameRoundPlayerResult"></a>

### GameRoundPlayerResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| hands | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| liqi_type | [uint32](#uint32) |  |  |
| is_fulu | [bool](#bool) |  |  |
| is_liujumanguan | [bool](#bool) |  |  |
| lian_zhuang | [uint32](#uint32) |  |  |
| hu | [GameRoundHuData](#lq-GameRoundHuData) |  |  |
| fangchongs | [GameRoundPlayerFangChongInfo](#lq-GameRoundPlayerFangChongInfo) | repeated |  |
| liqi_fangchong | [bool](#bool) |  |  |
| liqi_failed | [bool](#bool) |  |  |






<a name="lq-GameRoundSnapshot"></a>

### GameRoundSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| players | [GameRoundPlayer](#lq-GameRoundPlayer) | repeated |  |






<a name="lq-GameRuleSetting"></a>

### GameRuleSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round_type | [uint32](#uint32) |  |  |
| shiduan | [bool](#bool) |  |  |
| dora_count | [uint32](#uint32) |  |  |
| thinking_type | [uint32](#uint32) |  |  |
| use_detail_rule | [bool](#bool) |  |  |
| detail_rule_v2 | [ContestDetailRuleV2](#lq-ContestDetailRuleV2) |  |  |






<a name="lq-GameSetting"></a>

### GameSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| emoji_switch | [uint32](#uint32) |  |  |






<a name="lq-GameTestingEnvironmentSet"></a>

### GameTestingEnvironmentSet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| paixing | [uint32](#uint32) |  |  |
| left_count | [uint32](#uint32) |  |  |
| field_spell_var | [uint32](#uint32) |  |  |






<a name="lq-HighestHuRecord"></a>

### HighestHuRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fanshu | [uint32](#uint32) |  |  |
| doranum | [uint32](#uint32) |  |  |
| title | [string](#string) |  |  |
| hands | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| hupai | [string](#string) |  |  |
| title_id | [uint32](#uint32) |  |  |






<a name="lq-I18nContext"></a>

### I18nContext



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |
| context | [string](#string) |  |  |






<a name="lq-IslandBagData"></a>

### IslandBagData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| matrix | [string](#string) |  |  |
| items | [IslandBagItemData](#lq-IslandBagItemData) | repeated |  |






<a name="lq-IslandBagItemData"></a>

### IslandBagItemData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| pos | [uint32](#uint32) | repeated |  |
| rotate | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |






<a name="lq-IslandGoodsData"></a>

### IslandGoodsData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods_id | [uint32](#uint32) |  |  |
| count | [int32](#int32) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-IslandZoneData"></a>

### IslandZoneData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| currency_used | [SignedTimeCounterData](#lq-SignedTimeCounterData) |  |  |
| goods_records | [IslandGoodsData](#lq-IslandGoodsData) | repeated |  |






<a name="lq-Item"></a>

### Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| stack | [uint32](#uint32) |  |  |






<a name="lq-ItemGainRecord"></a>

### ItemGainRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-ItemGainRecords"></a>

### ItemGainRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| record_time | [uint32](#uint32) |  |  |
| limit_source_id | [uint32](#uint32) |  |  |
| records | [ItemGainRecord](#lq-ItemGainRecord) | repeated |  |






<a name="lq-MMOActivityTeamCandidateData"></a>

### MMOActivityTeamCandidateData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| equipments | [uint32](#uint32) | repeated |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-Mail"></a>

### Mail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id | [uint32](#uint32) |  |  |
| state | [uint32](#uint32) |  |  |
| take_attachment | [bool](#bool) |  |  |
| title | [string](#string) |  |  |
| content | [string](#string) |  |  |
| attachments | [RewardSlot](#lq-RewardSlot) | repeated |  |
| create_time | [uint32](#uint32) |  |  |
| expire_time | [uint32](#uint32) |  |  |
| reference_id | [uint32](#uint32) |  |  |
| title_i18n | [I18nContext](#lq-I18nContext) | repeated |  |
| content_i18n | [I18nContext](#lq-I18nContext) | repeated |  |
| template_id | [uint32](#uint32) |  |  |






<a name="lq-MaintainNotice"></a>

### MaintainNotice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| maintain_time | [uint32](#uint32) |  |  |






<a name="lq-MarathonGameRecord"></a>

### MarathonGameRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| point | [uint32](#uint32) |  |  |
| distance | [uint32](#uint32) |  |  |
| used_tick | [uint32](#uint32) |  |  |






<a name="lq-MineActivityData"></a>

### MineActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dig_point | [Point](#lq-Point) | repeated |  |
| map | [MineReward](#lq-MineReward) | repeated |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-MineReward"></a>

### MineReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| point | [Point](#lq-Point) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| received | [bool](#bool) |  |  |






<a name="lq-MonthTicketInfo"></a>

### MonthTicketInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| last_pay_time | [uint32](#uint32) |  |  |






<a name="lq-NetworkEndpoint"></a>

### NetworkEndpoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| family | [string](#string) |  |  |
| address | [string](#string) |  |  |
| port | [uint32](#uint32) |  |  |






<a name="lq-NicknameSetting"></a>

### NicknameSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| enable | [uint32](#uint32) |  |  |
| nicknames | [string](#string) | repeated |  |






<a name="lq-OpenResult"></a>

### OpenResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reward | [RewardSlot](#lq-RewardSlot) |  |  |
| replace | [RewardSlot](#lq-RewardSlot) |  |  |






<a name="lq-PaymentSetting"></a>

### PaymentSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| open_payment | [uint32](#uint32) |  |  |
| payment_info_show_type | [uint32](#uint32) |  |  |
| payment_info | [string](#string) |  |  |
| wechat | [PaymentSetting.WechatData](#lq-PaymentSetting-WechatData) |  |  |
| alipay | [PaymentSetting.AlipayData](#lq-PaymentSetting-AlipayData) |  |  |






<a name="lq-PaymentSetting-AlipayData"></a>

### PaymentSetting.AlipayData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| disable_create | [bool](#bool) |  |  |
| payment_source_platform | [uint32](#uint32) |  |  |






<a name="lq-PaymentSetting-WechatData"></a>

### PaymentSetting.WechatData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| disable_create | [bool](#bool) |  |  |
| payment_source_platform | [uint32](#uint32) |  |  |
| enable_credit | [bool](#bool) |  |  |






<a name="lq-PaymentSettingV2"></a>

### PaymentSettingV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| open_payment | [uint32](#uint32) |  |  |
| payment_platforms | [PaymentSettingV2.PaymentSettingUnit](#lq-PaymentSettingV2-PaymentSettingUnit) | repeated |  |






<a name="lq-PaymentSettingV2-PaymentMaintain"></a>

### PaymentSettingV2.PaymentMaintain



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| goods_click_action | [uint32](#uint32) |  |  |
| goods_click_text | [string](#string) |  |  |
| enabled_channel | [string](#string) | repeated |  |






<a name="lq-PaymentSettingV2-PaymentSettingUnit"></a>

### PaymentSettingV2.PaymentSettingUnit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| platform | [string](#string) |  |  |
| is_show | [bool](#bool) |  |  |
| goods_click_action | [uint32](#uint32) |  |  |
| goods_click_text | [string](#string) |  |  |
| maintain | [PaymentSettingV2.PaymentMaintain](#lq-PaymentSettingV2-PaymentMaintain) |  |  |
| enable_for_frozen_account | [bool](#bool) |  |  |
| extra_data | [string](#string) |  |  |
| enabled_channel | [string](#string) | repeated |  |






<a name="lq-PlayerBaseView"></a>

### PlayerBaseView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| avatar_id | [uint32](#uint32) |  |  |
| title | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |
| is_banned | [uint32](#uint32) |  |  |






<a name="lq-PlayerGameView"></a>

### PlayerGameView



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| avatar_id | [uint32](#uint32) |  |  |
| title | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| character | [Character](#lq-Character) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |
| views | [ViewSlot](#lq-ViewSlot) | repeated |  |
| team_id | [uint32](#uint32) |  |  |
| team_name | [string](#string) |  |  |






<a name="lq-Point"></a>

### Point



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [uint32](#uint32) |  |  |
| y | [uint32](#uint32) |  |  |






<a name="lq-QCMember"></a>

### QCMember



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| member_id | [uint32](#uint32) |  |  |
| consumed_sta | [TimeCounterData](#lq-TimeCounterData) |  |  |






<a name="lq-QCQuest"></a>

### QCQuest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| quest_id | [uint32](#uint32) |  |  |
| finished | [uint32](#uint32) |  |  |
| finished_time | [uint32](#uint32) |  |  |






<a name="lq-QuestionnaireBrief"></a>

### QuestionnaireBrief



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| version_id | [uint32](#uint32) |  |  |
| effective_time_start | [uint32](#uint32) |  |  |
| effective_time_end | [uint32](#uint32) |  |  |
| rewards | [QuestionnaireReward](#lq-QuestionnaireReward) | repeated |  |
| banner_title | [string](#string) |  |  |
| title | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-QuestionnaireDetail"></a>

### QuestionnaireDetail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| version_id | [uint32](#uint32) |  |  |
| effective_time_start | [uint32](#uint32) |  |  |
| effective_time_end | [uint32](#uint32) |  |  |
| rewards | [QuestionnaireReward](#lq-QuestionnaireReward) | repeated |  |
| banner_title | [string](#string) |  |  |
| title | [string](#string) |  |  |
| announcement_title | [string](#string) |  |  |
| announcement_content | [string](#string) |  |  |
| final_text | [string](#string) |  |  |
| questions | [QuestionnaireQuestion](#lq-QuestionnaireQuestion) | repeated |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-QuestionnaireQuestion"></a>

### QuestionnaireQuestion



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| title | [string](#string) |  |  |
| describe | [string](#string) |  |  |
| type | [string](#string) |  |  |
| sub_type | [string](#string) |  |  |
| options | [QuestionnaireQuestion.QuestionOption](#lq-QuestionnaireQuestion-QuestionOption) | repeated |  |
| option_random_sort | [bool](#bool) |  |  |
| require | [bool](#bool) |  |  |
| max_choice | [uint32](#uint32) |  |  |
| next_question | [QuestionnaireQuestion.NextQuestionData](#lq-QuestionnaireQuestion-NextQuestionData) | repeated |  |
| matrix_row | [string](#string) | repeated |  |
| option_random_sort_index | [int32](#int32) |  |  |






<a name="lq-QuestionnaireQuestion-NextQuestionData"></a>

### QuestionnaireQuestion.NextQuestionData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_question_id | [uint32](#uint32) |  |  |
| conditions | [QuestionnaireQuestion.NextQuestionData.QuestionconditionWrapper](#lq-QuestionnaireQuestion-NextQuestionData-QuestionconditionWrapper) | repeated |  |






<a name="lq-QuestionnaireQuestion-NextQuestionData-QuestionCondition"></a>

### QuestionnaireQuestion.NextQuestionData.QuestionCondition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| question_id | [uint32](#uint32) |  |  |
| op | [string](#string) |  |  |
| values | [string](#string) | repeated |  |






<a name="lq-QuestionnaireQuestion-NextQuestionData-QuestionconditionWrapper"></a>

### QuestionnaireQuestion.NextQuestionData.QuestionconditionWrapper



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| conditions | [QuestionnaireQuestion.NextQuestionData.QuestionCondition](#lq-QuestionnaireQuestion-NextQuestionData-QuestionCondition) | repeated |  |






<a name="lq-QuestionnaireQuestion-QuestionOption"></a>

### QuestionnaireQuestion.QuestionOption



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| label | [string](#string) |  |  |
| value | [string](#string) |  |  |
| allow_input | [bool](#bool) |  |  |






<a name="lq-QuestionnaireReward"></a>

### QuestionnaireReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| resource_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-RPGActivity"></a>

### RPGActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| last_show_uuid | [string](#string) |  |  |
| last_played_uuid | [string](#string) |  |  |
| current_state | [RPGState](#lq-RPGState) |  |  |
| last_show_state | [RPGState](#lq-RPGState) |  |  |
| received_rewards | [uint32](#uint32) | repeated |  |
| last_show_id | [uint32](#uint32) |  |  |






<a name="lq-RPGState"></a>

### RPGState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| player_damaged | [uint32](#uint32) |  |  |
| monster_damaged | [uint32](#uint32) |  |  |
| monster_seq | [uint32](#uint32) |  |  |






<a name="lq-RandomCharacter"></a>

### RandomCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| character_id | [uint32](#uint32) |  |  |
| skin_id | [uint32](#uint32) |  |  |






<a name="lq-RecordAnalysisedData"></a>

### RecordAnalysisedData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round_infos | [RecordRoundInfo](#lq-RecordRoundInfo) | repeated |  |






<a name="lq-RecordBaBeiInfo"></a>

### RecordBaBeiInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| is_zi_mo | [bool](#bool) |  |  |
| is_chong | [bool](#bool) |  |  |
| is_bei | [bool](#bool) |  |  |






<a name="lq-RecordCollectedData"></a>

### RecordCollectedData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| remarks | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |






<a name="lq-RecordGame"></a>

### RecordGame



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| config | [GameConfig](#lq-GameConfig) |  |  |
| accounts | [RecordGame.AccountInfo](#lq-RecordGame-AccountInfo) | repeated |  |
| result | [GameEndResult](#lq-GameEndResult) |  |  |
| robots | [RecordGame.AccountInfo](#lq-RecordGame-AccountInfo) | repeated |  |
| standard_rule | [uint32](#uint32) |  |  |






<a name="lq-RecordGame-AccountInfo"></a>

### RecordGame.AccountInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| seat | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| avatar_id | [uint32](#uint32) |  |  |
| character | [Character](#lq-Character) |  |  |
| title | [uint32](#uint32) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |
| views | [ViewSlot](#lq-ViewSlot) | repeated |  |






<a name="lq-RecordGangInfo"></a>

### RecordGangInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| pai | [string](#string) |  |  |
| is_dora | [bool](#bool) |  |  |
| xun | [uint32](#uint32) |  |  |






<a name="lq-RecordHuleInfo"></a>

### RecordHuleInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hand | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| hu_tile | [string](#string) |  |  |
| seat | [uint32](#uint32) |  |  |
| zimo | [bool](#bool) |  |  |
| qinjia | [bool](#bool) |  |  |
| liqi | [bool](#bool) |  |  |
| doras | [string](#string) | repeated |  |
| li_doras | [string](#string) | repeated |  |
| yiman | [bool](#bool) |  |  |
| count | [uint32](#uint32) |  |  |
| fans | [RecordHuleInfo.RecordFanInfo](#lq-RecordHuleInfo-RecordFanInfo) | repeated |  |
| fu | [uint32](#uint32) |  |  |
| point_zimo_qin | [uint32](#uint32) |  |  |
| point_zimo_xian | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |
| point_sum | [uint32](#uint32) |  |  |
| dadian | [uint32](#uint32) |  |  |
| is_jue_zhang | [bool](#bool) |  |  |
| xun | [uint32](#uint32) |  |  |
| ting_type | [uint32](#uint32) |  |  |
| ting_mian | [uint32](#uint32) |  |  |






<a name="lq-RecordHuleInfo-RecordFanInfo"></a>

### RecordHuleInfo.RecordFanInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| val | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-RecordHulesInfo"></a>

### RecordHulesInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [int32](#int32) |  |  |
| hules | [RecordHuleInfo](#lq-RecordHuleInfo) | repeated |  |






<a name="lq-RecordLiqiInfo"></a>

### RecordLiqiInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| score | [uint32](#uint32) |  |  |
| is_w | [bool](#bool) |  |  |
| is_zhen_ting | [bool](#bool) |  |  |
| xun | [uint32](#uint32) |  |  |
| is_success | [bool](#bool) |  |  |






<a name="lq-RecordListEntry"></a>

### RecordListEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| tag | [uint32](#uint32) |  |  |
| subtag | [uint32](#uint32) |  |  |
| players | [RecordPlayerResult](#lq-RecordPlayerResult) | repeated |  |
| standard_rule | [uint32](#uint32) |  |  |






<a name="lq-RecordLiujuInfo"></a>

### RecordLiujuInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-RecordNoTileInfo"></a>

### RecordNoTileInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| liujumanguan | [bool](#bool) |  |  |
| players | [RecordNoTilePlayerInfo](#lq-RecordNoTilePlayerInfo) | repeated |  |






<a name="lq-RecordNoTilePlayerInfo"></a>

### RecordNoTilePlayerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tingpai | [bool](#bool) |  |  |
| hand | [string](#string) | repeated |  |
| tings | [RecordTingPaiInfo](#lq-RecordTingPaiInfo) | repeated |  |
| liuman | [bool](#bool) |  |  |






<a name="lq-RecordPeiPaiInfo"></a>

### RecordPeiPaiInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dora_count | [uint32](#uint32) |  |  |
| r_dora_count | [uint32](#uint32) |  |  |
| bei_count | [uint32](#uint32) |  |  |






<a name="lq-RecordPlayerResult"></a>

### RecordPlayerResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| rank | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| nickname | [string](#string) |  |  |
| level | [AccountLevel](#lq-AccountLevel) |  |  |
| level3 | [AccountLevel](#lq-AccountLevel) |  |  |
| seat | [uint32](#uint32) |  |  |
| pt | [int32](#int32) |  |  |
| point | [int32](#int32) |  |  |
| max_hu_type | [uint32](#uint32) |  |  |
| action_liqi | [uint32](#uint32) |  |  |
| action_rong | [uint32](#uint32) |  |  |
| action_zimo | [uint32](#uint32) |  |  |
| action_chong | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |






<a name="lq-RecordRoundInfo"></a>

### RecordRoundInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| scores | [uint32](#uint32) | repeated |  |
| liqi_infos | [RecordLiqiInfo](#lq-RecordLiqiInfo) | repeated |  |
| gang_infos | [RecordGangInfo](#lq-RecordGangInfo) | repeated |  |
| peipai_infos | [RecordPeiPaiInfo](#lq-RecordPeiPaiInfo) | repeated |  |
| babai_infos | [RecordBaBeiInfo](#lq-RecordBaBeiInfo) | repeated |  |
| hules_info | [RecordHulesInfo](#lq-RecordHulesInfo) |  |  |
| liuju_info | [RecordLiujuInfo](#lq-RecordLiujuInfo) |  |  |
| no_tile_info | [RecordNoTileInfo](#lq-RecordNoTileInfo) |  |  |
| xiuluo_hules_info | [RecordHulesInfo](#lq-RecordHulesInfo) | repeated |  |






<a name="lq-RecordTingPaiInfo"></a>

### RecordTingPaiInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| haveyi | [bool](#bool) |  |  |
| yiman | [bool](#bool) |  |  |
| count | [uint32](#uint32) |  |  |
| fu | [uint32](#uint32) |  |  |
| biao_dora_count | [uint32](#uint32) |  |  |
| yiman_zimo | [bool](#bool) |  |  |
| count_zimo | [uint32](#uint32) |  |  |
| fu_zimo | [uint32](#uint32) |  |  |






<a name="lq-ReqCommon"></a>

### ReqCommon







<a name="lq-ResAccountUpdate"></a>

### ResAccountUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |
| update | [AccountUpdate](#lq-AccountUpdate) |  |  |






<a name="lq-ResCommon"></a>

### ResCommon



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| error | [Error](#lq-Error) |  |  |






<a name="lq-RewardPlusResult"></a>

### RewardPlusResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| exchange | [RewardPlusResult.Exchange](#lq-RewardPlusResult-Exchange) |  |  |






<a name="lq-RewardPlusResult-Exchange"></a>

### RewardPlusResult.Exchange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| exchange | [uint32](#uint32) |  |  |






<a name="lq-RewardSlot"></a>

### RewardSlot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-RollingNotice"></a>

### RollingNotice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| content | [string](#string) |  |  |
| start_time | [uint32](#uint32) |  |  |
| end_time | [uint32](#uint32) |  |  |
| repeat_interval | [uint32](#uint32) |  |  |
| repeat_time | [uint32](#uint32) | repeated |  |
| repeat_type | [uint32](#uint32) |  |  |






<a name="lq-Room"></a>

### Room



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| room_id | [uint32](#uint32) |  |  |
| owner_id | [uint32](#uint32) |  |  |
| mode | [GameMode](#lq-GameMode) |  |  |
| max_player_count | [uint32](#uint32) |  |  |
| persons | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| ready_list | [uint32](#uint32) | repeated |  |
| is_playing | [bool](#bool) |  |  |
| public_live | [bool](#bool) |  |  |
| robot_count | [uint32](#uint32) |  |  |
| tournament_id | [uint32](#uint32) |  |  |
| seq | [uint32](#uint32) |  |  |
| pre_rule | [string](#string) |  |  |
| robots | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| positions | [uint32](#uint32) | repeated |  |






<a name="lq-SeerBrief"></a>

### SeerBrief



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| state | [uint32](#uint32) |  |  |
| expire_time | [uint32](#uint32) |  |  |
| player_scores | [SeerScore](#lq-SeerScore) | repeated |  |
| create_time | [uint32](#uint32) |  |  |






<a name="lq-SeerEvent"></a>

### SeerEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| record_index | [int32](#int32) |  |  |
| seer_index | [int32](#int32) |  |  |
| recommends | [SeerRecommend](#lq-SeerRecommend) | repeated |  |






<a name="lq-SeerPrediction"></a>

### SeerPrediction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| action | [int32](#int32) |  |  |
| score | [int32](#int32) |  |  |






<a name="lq-SeerRecommend"></a>

### SeerRecommend



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [int32](#int32) |  |  |
| predictions | [SeerPrediction](#lq-SeerPrediction) | repeated |  |






<a name="lq-SeerReport"></a>

### SeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| uuid | [string](#string) |  |  |
| events | [SeerEvent](#lq-SeerEvent) | repeated |  |
| rounds | [SeerRound](#lq-SeerRound) | repeated |  |






<a name="lq-SeerRound"></a>

### SeerRound



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| player_scores | [SeerScore](#lq-SeerScore) | repeated |  |






<a name="lq-SeerScore"></a>

### SeerScore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| rating | [uint32](#uint32) |  |  |






<a name="lq-SegmentTaskProgress"></a>

### SegmentTaskProgress



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| counter | [uint32](#uint32) |  |  |
| achieved | [bool](#bool) |  |  |
| rewarded | [bool](#bool) |  |  |
| failed | [bool](#bool) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| achieved_count | [uint32](#uint32) |  |  |






<a name="lq-ServerSettings"></a>

### ServerSettings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| payment_setting | [PaymentSetting](#lq-PaymentSetting) |  |  |
| payment_setting_v2 | [PaymentSettingV2](#lq-PaymentSettingV2) |  |  |
| nickname_setting | [NicknameSetting](#lq-NicknameSetting) |  |  |






<a name="lq-ShopInfo"></a>

### ShopInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| zhp | [ZHPShop](#lq-ZHPShop) |  |  |
| buy_records | [BuyRecord](#lq-BuyRecord) | repeated |  |
| last_refresh_time | [uint32](#uint32) |  |  |
| selected_package_records | [ShopInfo.SelectedPackageBuyRecord](#lq-ShopInfo-SelectedPackageBuyRecord) | repeated |  |






<a name="lq-ShopInfo-SelectedPackageBuyRecord"></a>

### ShopInfo.SelectedPackageBuyRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| package_id | [uint32](#uint32) |  |  |
| buy_records | [BuyRecord](#lq-BuyRecord) | repeated |  |






<a name="lq-SignedTimeCounterData"></a>

### SignedTimeCounterData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [int32](#int32) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-SimulationActionData"></a>

### SimulationActionData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| riichi | [SimulationActionData.ActionRiichiData](#lq-SimulationActionData-ActionRiichiData) |  |  |
| hule | [SimulationActionData.ActionHuleData](#lq-SimulationActionData-ActionHuleData) |  |  |
| fulu | [SimulationActionData.ActionFuluData](#lq-SimulationActionData-ActionFuluData) |  |  |
| discard_tile | [SimulationActionData.ActionDiscardData](#lq-SimulationActionData-ActionDiscardData) |  |  |
| deal_tile | [SimulationActionData.ActionDealTileData](#lq-SimulationActionData-ActionDealTileData) |  |  |






<a name="lq-SimulationActionData-ActionDealTileData"></a>

### SimulationActionData.ActionDealTileData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |






<a name="lq-SimulationActionData-ActionDiscardData"></a>

### SimulationActionData.ActionDiscardData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| riichi | [bool](#bool) |  |  |






<a name="lq-SimulationActionData-ActionFuluData"></a>

### SimulationActionData.ActionFuluData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |






<a name="lq-SimulationActionData-ActionHuleData"></a>

### SimulationActionData.ActionHuleData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hule | [SimulationActionData.ActionHuleData.HuleInfo](#lq-SimulationActionData-ActionHuleData-HuleInfo) | repeated |  |






<a name="lq-SimulationActionData-ActionHuleData-HuleInfo"></a>

### SimulationActionData.ActionHuleData.HuleInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fan | [uint32](#uint32) |  |  |
| zimo | [bool](#bool) |  |  |
| point | [uint32](#uint32) |  |  |
| oya | [bool](#bool) |  |  |
| player | [uint32](#uint32) |  |  |
| chong | [uint32](#uint32) |  |  |
| toutiao | [bool](#bool) |  |  |






<a name="lq-SimulationActionData-ActionRiichiData"></a>

### SimulationActionData.ActionRiichiData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Ability"></a>

### SimulationV2Ability



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| luk | [uint32](#uint32) |  |  |
| tec | [uint32](#uint32) |  |  |
| ins | [uint32](#uint32) |  |  |
| int | [uint32](#uint32) |  |  |
| res | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Buff"></a>

### SimulationV2Buff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| round | [uint32](#uint32) |  |  |
| store | [uint32](#uint32) | repeated |  |






<a name="lq-SimulationV2Data"></a>

### SimulationV2Data



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| season | [SimulationV2SeasonData](#lq-SimulationV2SeasonData) |  |  |
| highest_score | [int32](#int32) |  |  |
| upgrade | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |
| event_pool | [uint32](#uint32) | repeated |  |
| season_count | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Effect"></a>

### SimulationV2Effect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Event"></a>

### SimulationV2Event



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| selections | [SimulationV2Event.SimulationV2EventSelection](#lq-SimulationV2Event-SimulationV2EventSelection) | repeated |  |
| next_round | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Event-SimulationV2EventSelection"></a>

### SimulationV2Event.SimulationV2EventSelection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| results | [SimulationV2Event.SimulationV2EventSelection.SimulationV2EventResult](#lq-SimulationV2Event-SimulationV2EventSelection-SimulationV2EventResult) | repeated |  |






<a name="lq-SimulationV2Event-SimulationV2EventSelection-SimulationV2EventResult"></a>

### SimulationV2Event.SimulationV2EventSelection.SimulationV2EventResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2EventHistory"></a>

### SimulationV2EventHistory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| round | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Match"></a>

### SimulationV2Match



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [SimulationV2MatchInfo](#lq-SimulationV2MatchInfo) |  |  |
| players | [SimulationV2Match.SimulationV2Player](#lq-SimulationV2Match-SimulationV2Player) | repeated |  |
| history | [SimulationV2MatchHistory](#lq-SimulationV2MatchHistory) | repeated |  |
| rank | [uint32](#uint32) | repeated |  |
| is_match_end | [bool](#bool) |  |  |
| actions | [SimulationActionData](#lq-SimulationActionData) | repeated |  |
| buff_list | [SimulationV2Buff](#lq-SimulationV2Buff) | repeated |  |
| is_first_round | [bool](#bool) |  |  |
| last_event_remain | [uint32](#uint32) |  |  |
| effected_buff_list | [uint32](#uint32) | repeated |  |
| triggered_story | [uint32](#uint32) | repeated |  |






<a name="lq-SimulationV2Match-SimulationV2Player"></a>

### SimulationV2Match.SimulationV2Player



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| main | [bool](#bool) |  |  |
| ting | [uint32](#uint32) |  |  |
| score | [int32](#int32) |  |  |
| fulu | [uint32](#uint32) |  |  |
| riichi | [bool](#bool) |  |  |
| find_ting | [uint32](#uint32) | repeated |  |
| seat | [uint32](#uint32) |  |  |
| con_push_ting | [uint32](#uint32) |  |  |
| con_keep_ting | [uint32](#uint32) |  |  |
| ippatsu | [bool](#bool) |  |  |






<a name="lq-SimulationV2MatchHistory"></a>

### SimulationV2MatchHistory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| remain | [uint32](#uint32) |  |  |
| score_modify | [int32](#int32) | repeated |  |
| round_start | [SimulationV2MatchHistory.RoundStartArgs](#lq-SimulationV2MatchHistory-RoundStartArgs) |  |  |
| riichi | [SimulationV2MatchHistory.RiichiArgs](#lq-SimulationV2MatchHistory-RiichiArgs) |  |  |
| fulu | [SimulationV2MatchHistory.FuluArgs](#lq-SimulationV2MatchHistory-FuluArgs) |  |  |
| hule | [SimulationV2MatchHistory.HuleArgs](#lq-SimulationV2MatchHistory-HuleArgs) | repeated |  |
| push_ting | [SimulationV2MatchHistory.PushTingArgs](#lq-SimulationV2MatchHistory-PushTingArgs) |  |  |
| find_ting | [SimulationV2MatchHistory.FindTingArgs](#lq-SimulationV2MatchHistory-FindTingArgs) |  |  |
| liuju | [SimulationV2MatchHistory.LiujuArgs](#lq-SimulationV2MatchHistory-LiujuArgs) |  |  |
| story | [SimulationV2MatchHistory.StoryArgs](#lq-SimulationV2MatchHistory-StoryArgs) |  |  |






<a name="lq-SimulationV2MatchHistory-FindTingArgs"></a>

### SimulationV2MatchHistory.FindTingArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| target | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchHistory-FuluArgs"></a>

### SimulationV2MatchHistory.FuluArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| ting | [uint32](#uint32) |  |  |
| fulu | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchHistory-HuleArgs"></a>

### SimulationV2MatchHistory.HuleArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| zimo | [bool](#bool) |  |  |
| chong_seat | [uint32](#uint32) |  |  |
| point | [int32](#int32) |  |  |
| fan | [int32](#int32) |  |  |
| score_modify | [int32](#int32) | repeated |  |






<a name="lq-SimulationV2MatchHistory-LiujuArgs"></a>

### SimulationV2MatchHistory.LiujuArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ting | [uint32](#uint32) | repeated |  |






<a name="lq-SimulationV2MatchHistory-PushTingArgs"></a>

### SimulationV2MatchHistory.PushTingArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| ting | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchHistory-RiichiArgs"></a>

### SimulationV2MatchHistory.RiichiArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchHistory-RoundStartArgs"></a>

### SimulationV2MatchHistory.RoundStartArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [SimulationV2MatchInfo](#lq-SimulationV2MatchInfo) |  |  |
| scores | [int32](#int32) | repeated |  |
| ting | [uint32](#uint32) |  |  |
| effected_buff_list | [uint32](#uint32) | repeated |  |






<a name="lq-SimulationV2MatchHistory-StoryArgs"></a>

### SimulationV2MatchHistory.StoryArgs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| story_id | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchInfo"></a>

### SimulationV2MatchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| gong | [uint32](#uint32) |  |  |
| remain | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2MatchRecord"></a>

### SimulationV2MatchRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| players | [SimulationV2PlayerRecord](#lq-SimulationV2PlayerRecord) | repeated |  |
| round | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2PlayerRecord"></a>

### SimulationV2PlayerRecord



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| main | [bool](#bool) |  |  |
| score | [int32](#int32) |  |  |
| rank | [uint32](#uint32) |  |  |
| seat | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2Record"></a>

### SimulationV2Record



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hu_count | [uint32](#uint32) |  |  |
| chong_count | [uint32](#uint32) |  |  |
| highest_hu | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) | repeated |  |
| round_count | [uint32](#uint32) |  |  |






<a name="lq-SimulationV2SeasonData"></a>

### SimulationV2SeasonData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| round | [uint32](#uint32) |  |  |
| ability | [SimulationV2Ability](#lq-SimulationV2Ability) |  |  |
| effect_list | [SimulationV2Effect](#lq-SimulationV2Effect) | repeated |  |
| match | [SimulationV2Match](#lq-SimulationV2Match) |  |  |
| event | [SimulationV2Event](#lq-SimulationV2Event) |  |  |
| event_history | [SimulationV2EventHistory](#lq-SimulationV2EventHistory) | repeated |  |
| record | [SimulationV2Record](#lq-SimulationV2Record) |  |  |
| total_score | [int32](#int32) |  |  |
| match_history | [SimulationV2MatchRecord](#lq-SimulationV2MatchRecord) | repeated |  |






<a name="lq-SnowballActivityBossAction"></a>

### SnowballActivityBossAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tick | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| track | [uint32](#uint32) |  |  |
| attack_info | [SnowballActivityBossAction.SnowballActivityBossAttackInfo](#lq-SnowballActivityBossAction-SnowballActivityBossAttackInfo) |  |  |
| mp_consume_info | [SnowballActivityBossAction.SnowballActivityBossMPConsumeInfo](#lq-SnowballActivityBossAction-SnowballActivityBossMPConsumeInfo) |  |  |






<a name="lq-SnowballActivityBossAction-SnowballActivityBossAttackInfo"></a>

### SnowballActivityBossAction.SnowballActivityBossAttackInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| damage | [uint32](#uint32) |  |  |
| is_con_attack | [uint32](#uint32) |  |  |






<a name="lq-SnowballActivityBossAction-SnowballActivityBossMPConsumeInfo"></a>

### SnowballActivityBossAction.SnowballActivityBossMPConsumeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mp_consume | [uint32](#uint32) |  |  |
| before_delay | [uint32](#uint32) |  |  |
| after_delay | [uint32](#uint32) |  |  |






<a name="lq-StringArrayDirty"></a>

### StringArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [string](#string) | repeated |  |






<a name="lq-StringDirty"></a>

### StringDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [string](#string) |  |  |






<a name="lq-TaskProgress"></a>

### TaskProgress



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| counter | [uint32](#uint32) |  |  |
| achieved | [bool](#bool) |  |  |
| rewarded | [bool](#bool) |  |  |
| failed | [bool](#bool) |  |  |
| rewarded_time | [uint32](#uint32) |  |  |






<a name="lq-TimeCounterData"></a>

### TimeCounterData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| update_time | [uint32](#uint32) |  |  |






<a name="lq-TransparentData"></a>

### TransparentData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| method | [string](#string) |  |  |
| data | [bytes](#bytes) |  |  |
| session | [string](#string) |  |  |
| remote | [NetworkEndpoint](#lq-NetworkEndpoint) |  |  |
| platform | [string](#string) |  |  |






<a name="lq-UInt32ArrayDirty"></a>

### UInt32ArrayDirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [uint32](#uint32) | repeated |  |






<a name="lq-UInt32Dirty"></a>

### UInt32Dirty



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| dirty | [bool](#bool) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="lq-UnlockedStoryData"></a>

### UnlockedStoryData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| story_id | [uint32](#uint32) |  |  |
| finished_ending | [uint32](#uint32) | repeated |  |
| rewarded_ending | [uint32](#uint32) | repeated |  |
| finish_rewarded | [uint32](#uint32) |  |  |
| all_finish_rewarded | [uint32](#uint32) |  |  |






<a name="lq-ViewSlot"></a>

### ViewSlot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| slot | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| item_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-VillageBuildingData"></a>

### VillageBuildingData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| reward | [VillageReward](#lq-VillageReward) | repeated |  |
| workers | [uint32](#uint32) | repeated |  |






<a name="lq-VillageReward"></a>

### VillageReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-VillageTargetInfo"></a>

### VillageTargetInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| nickname | [string](#string) |  |  |
| avatar | [uint32](#uint32) |  |  |
| avatar_frame | [uint32](#uint32) |  |  |
| title | [uint32](#uint32) |  |  |
| verified | [uint32](#uint32) |  |  |






<a name="lq-VillageTaskData"></a>

### VillageTaskData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| completed_count | [uint32](#uint32) |  |  |






<a name="lq-VillageTripData"></a>

### VillageTripData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| start_round | [uint32](#uint32) |  |  |
| dest_id | [uint32](#uint32) |  |  |
| reward | [VillageReward](#lq-VillageReward) | repeated |  |
| level | [uint32](#uint32) |  |  |
| info | [VillageTargetInfo](#lq-VillageTargetInfo) |  |  |






<a name="lq-VoteData"></a>

### VoteData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| vote | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |






<a name="lq-Wrapper"></a>

### Wrapper



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| data | [bytes](#bytes) |  |  |






<a name="lq-ZHPShop"></a>

### ZHPShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| goods | [uint32](#uint32) | repeated |  |
| buy_records | [BuyRecord](#lq-BuyRecord) | repeated |  |
| free_refresh | [ZHPShop.RefreshCount](#lq-ZHPShop-RefreshCount) |  |  |
| cost_refresh | [ZHPShop.RefreshCount](#lq-ZHPShop-RefreshCount) |  |  |






<a name="lq-ZHPShop-RefreshCount"></a>

### ZHPShop.RefreshCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |








<a name="lq-GamePlayerState"></a>

### GamePlayerState


| Name | Number | Description |
| ---- | ------ | ----------- |
| NULL | 0 |  |
| AUTH | 1 |  |
| SYNCING | 2 |  |
| READY | 3 |  |










<a name="config-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## config.proto



<a name="lq-config-ConfigTables"></a>

### ConfigTables



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| header_hash | [string](#string) |  |  |
| schemas | [TableSchema](#lq-config-TableSchema) | repeated |  |
| datas | [SheetData](#lq-config-SheetData) | repeated |  |






<a name="lq-config-Field"></a>

### Field



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field_name | [string](#string) |  |  |
| array_length | [uint32](#uint32) |  |  |
| pb_type | [string](#string) |  |  |
| pb_index | [uint32](#uint32) |  |  |






<a name="lq-config-SheetData"></a>

### SheetData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| table | [string](#string) |  |  |
| sheet | [string](#string) |  |  |
| data | [bytes](#bytes) | repeated |  |






<a name="lq-config-SheetMeta"></a>

### SheetMeta



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| category | [string](#string) |  |  |
| key | [string](#string) |  |  |






<a name="lq-config-SheetSchema"></a>

### SheetSchema



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| meta | [SheetMeta](#lq-config-SheetMeta) |  |  |
| fields | [Field](#lq-config-Field) | repeated |  |






<a name="lq-config-TableSchema"></a>

### TableSchema



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| sheets | [SheetSchema](#lq-config-SheetSchema) | repeated |  |















<a name="excel-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## excel.proto



<a name="lqc-Sheet_AbMatch_ConsumeSeq"></a>

### Sheet_AbMatch_ConsumeSeq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| item_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_AbMatch_MatchInfo"></a>

### Sheet_AbMatch_MatchInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| ab_match_activity_id | [uint32](#uint32) |  |  |
| match_activity_id | [uint32](#uint32) |  |  |
| desktop_id_list | [string](#string) |  |  |
| consume_id | [uint32](#uint32) |  |  |
| buy_in_condition | [string](#string) |  |  |
| mail_template_id | [uint32](#uint32) |  |  |
| max_match_count | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| point_id | [uint32](#uint32) |  |  |
| match_level | [uint32](#uint32) |  |  |
| priority | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_AbMatch_Point"></a>

### Sheet_AbMatch_Point



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| desktop_id_list | [string](#string) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_AbMatch_RewardSeq"></a>

### Sheet_AbMatch_RewardSeq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| point_lower | [uint32](#uint32) |  |  |
| point_upper | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| chest_mark | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Achievement_Achievement"></a>

### Sheet_Achievement_Achievement



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| rare | [uint32](#uint32) |  |  |
| locked | [uint32](#uint32) |  |  |
| group_id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| segment_id | [uint32](#uint32) |  |  |
| base_task | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| hidden | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Achievement_AchievementGroup"></a>

### Sheet_Achievement_AchievementGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| img | [string](#string) |  |  |
| reward | [string](#string) |  |  |
| percentage | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Achievement_Badge"></a>

### Sheet_Achievement_Badge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| base_task | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Achievement_BadgeGroup"></a>

### Sheet_Achievement_BadgeGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| badge_id | [uint32](#uint32) | repeated |  |
| name | [uint32](#uint32) |  |  |
| desc | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| img | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_Activity"></a>

### Sheet_Activity_Activity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| type | [string](#string) |  |  |
| need_popout | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ActivityBanner"></a>

### Sheet_Activity_ActivityBanner



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| banner_type | [uint32](#uint32) |  |  |
| enter_icon | [string](#string) |  |  |
| banner_big | [string](#string) |  |  |
| banner_left | [string](#string) |  |  |
| banner_left_selected | [string](#string) |  |  |
| banner_left_icon | [string](#string) |  |  |
| time_remind | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ActivityBuff"></a>

### Sheet_Activity_ActivityBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| buff_level | [uint32](#uint32) |  |  |
| buff_type | [uint32](#uint32) |  |  |
| upgrade_resource_id | [uint32](#uint32) |  |  |
| upgrade_resource_count | [uint32](#uint32) |  |  |
| effect | [uint32](#uint32) |  |  |
| unlock_params | [uint32](#uint32) | repeated |  |
| effect_desc | [uint32](#uint32) |  |  |
| effect_desc_2 | [uint32](#uint32) |  |  |
| limit_count | [uint32](#uint32) |  |  |
| limit_interval | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ActivityDesktop"></a>

### Sheet_Activity_ActivityDesktop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| desktop_id | [uint32](#uint32) |  |  |
| interval | [uint32](#uint32) |  |  |
| interval_type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ActivityGuide"></a>

### Sheet_Activity_ActivityGuide



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| guide_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| guide_location | [uint32](#uint32) |  |  |
| char_id | [uint32](#uint32) |  |  |
| char_str_id | [uint32](#uint32) |  |  |
| content_str_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ActivityItem"></a>

### Sheet_Activity_ActivityItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| item_list | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_ActivityRoom"></a>

### Sheet_Activity_ActivityRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| str_name | [string](#string) |  |  |
| str_rule | [string](#string) |  |  |
| friend_room_id | [uint32](#uint32) |  |  |
| dora3_mode | [uint32](#uint32) |  |  |
| begin_open_mode | [uint32](#uint32) |  |  |
| muyu_mode | [uint32](#uint32) |  |  |
| xuezhan_mode | [uint32](#uint32) |  |  |
| huanzhang_mode | [uint32](#uint32) |  |  |
| chuanma_mode | [uint32](#uint32) |  |  |
| jiuchao_mode | [uint32](#uint32) |  |  |
| reveal_discard | [uint32](#uint32) |  |  |
| field_spell_mode | [uint32](#uint32) |  |  |
| zhanxing_mode | [uint32](#uint32) |  |  |
| tianming_mode | [uint32](#uint32) |  |  |
| yongchang_mode | [uint32](#uint32) |  |  |
| hunzhiyiji_mode | [uint32](#uint32) |  |  |
| wanxiangxiuluo_mode | [uint32](#uint32) |  |  |
| beishuizhizhan_mode | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_AmuletUpgrade"></a>

### Sheet_Activity_AmuletUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| skill_point | [uint32](#uint32) |  |  |
| buff_id | [uint32](#uint32) |  |  |
| display_value | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ArenaActivity"></a>

### Sheet_Activity_ArenaActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| match_time | [string](#string) |  |  |
| ticket_time_limit | [string](#string) |  |  |
| ticket_item_id | [uint32](#uint32) |  |  |
| ticket_price | [string](#string) |  |  |
| desktop_id | [uint32](#uint32) |  |  |
| max_win_count | [uint32](#uint32) |  |  |
| max_lose_count | [uint32](#uint32) |  |  |
| reward_group | [uint32](#uint32) |  |  |
| daily_ticket_limit | [uint32](#uint32) |  |  |
| mail_template | [uint32](#uint32) |  |  |
| arena_reward_display_group | [uint32](#uint32) |  |  |
| level_limit | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ArenaReward"></a>

### Sheet_Activity_ArenaReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| win_count | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_ArenaRewardDisplay"></a>

### Sheet_Activity_ArenaRewardDisplay



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| win_count_min | [uint32](#uint32) |  |  |
| win_count_max | [uint32](#uint32) |  |  |
| reward_1 | [uint32](#uint32) |  |  |
| reward_1_remark | [string](#string) |  |  |
| reward_2 | [uint32](#uint32) |  |  |
| reward_2_remark | [string](#string) |  |  |
| reward_3 | [uint32](#uint32) |  |  |
| reward_3_remark | [string](#string) |  |  |
| reward_4 | [uint32](#uint32) |  |  |
| reward_4_remark | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_BuffCondition"></a>

### Sheet_Activity_BuffCondition







<a name="lqc-Sheet_Activity_ChestReplaceUp"></a>

### Sheet_Activity_ChestReplaceUp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ChestUp"></a>

### Sheet_Activity_ChestUp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| title_str_id | [uint32](#uint32) |  |  |
| str_id | [string](#string) |  |  |
| chara_str_id | [uint32](#uint32) |  |  |
| item_str_id | [uint32](#uint32) |  |  |
| img | [string](#string) |  |  |
| title_img | [string](#string) |  |  |
| title_img_2 | [string](#string) |  |  |
| typeset | [uint32](#uint32) |  |  |
| enter_animation | [string](#string) |  |  |
| special_effect_front | [string](#string) |  |  |
| special_effect_back | [string](#string) |  |  |
| special_audio | [uint32](#uint32) |  |  |
| up_items_type | [uint32](#uint32) |  |  |
| up_items | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_ChooseUpActivity"></a>

### Sheet_Activity_ChooseUpActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| replace_id | [uint32](#uint32) |  |  |
| base_chest_id | [uint32](#uint32) | repeated |  |
| choose_type | [string](#string) | repeated |  |
| sort | [uint32](#uint32) |  |  |
| title_str_id | [uint32](#uint32) |  |  |
| str_id | [string](#string) |  |  |
| chara_str_id | [uint32](#uint32) |  |  |
| item_str_id | [uint32](#uint32) |  |  |
| img | [string](#string) |  |  |
| title_img | [string](#string) |  |  |
| title_img_2 | [string](#string) |  |  |
| typeset | [uint32](#uint32) |  |  |
| enter_animation | [string](#string) |  |  |
| special_effect_front | [string](#string) |  |  |
| special_effect_back | [string](#string) |  |  |
| special_audio | [uint32](#uint32) |  |  |
| up_items_type | [uint32](#uint32) |  |  |
| up_items | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_ChooseUpReplace"></a>

### Sheet_Activity_ChooseUpReplace



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_CombiningActivityInfo"></a>

### Sheet_Activity_CombiningActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| craft_bin | [uint32](#uint32) | repeated |  |
| craft_bin_price | [string](#string) | repeated |  |
| craft_bin_unlock | [uint32](#uint32) | repeated |  |
| point_item | [uint32](#uint32) |  |  |
| bonus_daily_limit | [uint32](#uint32) |  |  |
| multi_order_rate | [uint32](#uint32) |  |  |
| one_coin_num | [uint32](#uint32) |  |  |
| coin_num_max | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_CombiningCraft"></a>

### Sheet_Activity_CombiningCraft



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| group | [uint32](#uint32) |  |  |
| recycling_price | [string](#string) |  |  |
| level | [uint32](#uint32) |  |  |
| upgrade_craft_id | [uint32](#uint32) |  |  |
| order_price | [string](#string) |  |  |
| if_bonus | [uint32](#uint32) |  |  |
| img_name | [string](#string) |  |  |
| craft_name | [uint32](#uint32) |  |  |
| craft_desc | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_CombiningCraftPool"></a>

### Sheet_Activity_CombiningCraftPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bin_id | [uint32](#uint32) |  |  |
| craft_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_CombiningCustomer"></a>

### Sheet_Activity_CombiningCustomer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| customer_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| order_type | [uint32](#uint32) |  |  |
| customer_location | [uint32](#uint32) |  |  |
| customer_skin | [string](#string) |  |  |
| customer_loading | [uint32](#uint32) |  |  |
| complete_sound | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_CombiningMap"></a>

### Sheet_Activity_CombiningMap



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| point_item_id | [uint32](#uint32) |  |  |
| point_item_count | [uint32](#uint32) |  |  |
| workbench_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_CombiningOrder"></a>

### Sheet_Activity_CombiningOrder







<a name="lqc-Sheet_Activity_DailySign"></a>

### Sheet_Activity_DailySign



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_Exchange"></a>

### Sheet_Activity_Exchange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| consume_id | [uint32](#uint32) |  |  |
| consume_count | [uint32](#uint32) |  |  |
| exchange_limit | [int32](#int32) |  |  |
| item_limit_id | [uint32](#uint32) |  |  |
| item_limit_count | [uint32](#uint32) |  |  |
| unlock_day | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_FeedActivityInfo"></a>

### Sheet_Activity_FeedActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| max_feed_count | [uint32](#uint32) |  |  |
| feed_reward_id | [uint32](#uint32) |  |  |
| friend_send_limit | [uint32](#uint32) |  |  |
| friend_recv_limit | [uint32](#uint32) |  |  |
| food_item_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_FeedActivityReward"></a>

### Sheet_Activity_FeedActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| img_stage | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FestivalActivity"></a>

### Sheet_Activity_FestivalActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| funds_id | [uint32](#uint32) |  |  |
| proposal_id | [uint32](#uint32) |  |  |
| proposal_consume | [uint32](#uint32) |  |  |
| daily_buy_limit | [uint32](#uint32) |  |  |
| arrow_amount | [uint32](#uint32) |  |  |
| max_amount | [uint32](#uint32) |  |  |
| max_proposal_pos | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FestivalEnding"></a>

### Sheet_Activity_FestivalEnding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |
| ending_type | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| item_plus | [string](#string) |  |  |
| item_minus | [string](#string) |  |  |
| funds | [int32](#int32) |  |  |
| ending_text | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FestivalEvent"></a>

### Sheet_Activity_FestivalEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| event_id | [uint32](#uint32) |  |  |
| position | [uint32](#uint32) |  |  |
| unlock_level | [uint32](#uint32) |  |  |
| ending_group | [uint32](#uint32) | repeated |  |
| event_title | [uint32](#uint32) |  |  |
| client_name | [uint32](#uint32) |  |  |
| client_icon | [string](#string) |  |  |
| event_text | [uint32](#uint32) |  |  |
| option_text_a | [uint32](#uint32) |  |  |
| option_text_b | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FestivalLevel"></a>

### Sheet_Activity_FestivalLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| level_name | [uint32](#uint32) |  |  |
| level_require | [string](#string) |  |  |
| level_res | [string](#string) |  |  |
| unlock_event_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FestivalProposal"></a>

### Sheet_Activity_FestivalProposal



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| proposal_id | [uint32](#uint32) |  |  |
| unlock_level | [uint32](#uint32) |  |  |
| ending_group | [uint32](#uint32) | repeated |  |
| client_name | [uint32](#uint32) |  |  |
| client_icon | [string](#string) |  |  |
| proposal_text | [uint32](#uint32) |  |  |
| option_text_a | [uint32](#uint32) |  |  |
| option_text_b | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FlipInfo"></a>

### Sheet_Activity_FlipInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| flip_count | [uint32](#uint32) |  |  |
| init_task_list | [string](#string) |  |  |
| start_time | [string](#string) |  |  |
| end_time | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_FlipTask"></a>

### Sheet_Activity_FlipTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| matrix_x | [uint32](#uint32) |  |  |
| matrix_y | [uint32](#uint32) |  |  |
| is_reward | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_FriendGiftActivity"></a>

### Sheet_Activity_FriendGiftActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| friend_send_limit | [uint32](#uint32) |  |  |
| friend_send_consume | [uint32](#uint32) |  |  |
| friend_recv_limit | [uint32](#uint32) |  |  |
| extra_gift | [uint32](#uint32) |  |  |
| gift_item_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_GachaActivityInfo"></a>

### Sheet_Activity_GachaActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| gacha_pool | [uint32](#uint32) |  |  |
| gacha_control | [uint32](#uint32) |  |  |
| sp_trigger_times | [uint32](#uint32) |  |  |
| sp_rewards | [string](#string) |  |  |
| consume | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_GachaControl"></a>

### Sheet_Activity_GachaControl







<a name="lqc-Sheet_Activity_GachaPool"></a>

### Sheet_Activity_GachaPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pool_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| rare | [uint32](#uint32) |  |  |
| item | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_GamePoint"></a>

### Sheet_Activity_GamePoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| point_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |
| res_id | [uint32](#uint32) |  |  |
| res_count | [uint32](#uint32) |  |  |
| unlock_day | [int32](#int32) |  |  |
| node_mark | [uint32](#uint32) |  |  |
| image_mark | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_GamePointFilter"></a>

### Sheet_Activity_GamePointFilter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| has_robot | [string](#string) |  |  |
| category | [string](#string) |  |  |
| room | [string](#string) |  |  |
| mode | [string](#string) |  |  |
| point_coe | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_GamePointInfo"></a>

### Sheet_Activity_GamePointInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| filter_id | [uint32](#uint32) |  |  |
| reward_mail_template | [uint32](#uint32) |  |  |
| max_point_limit_day | [int32](#int32) |  |  |
| should_rank | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_GamePointRank"></a>

### Sheet_Activity_GamePointRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rank_rate_lower | [uint32](#uint32) |  |  |
| rank_rate_upper | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_GameTask"></a>

### Sheet_Activity_GameTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| hidden_reward | [string](#string) |  |  |
| limit_id | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_IslandActivity"></a>

### Sheet_Activity_IslandActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| food_id | [uint32](#uint32) |  |  |
| currency_id | [uint32](#uint32) |  |  |
| food_consume | [uint32](#uint32) |  |  |
| sell_discount | [uint32](#uint32) |  |  |
| guide_bottle_price | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_IslandBag"></a>

### Sheet_Activity_IslandBag



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| bag_id | [uint32](#uint32) |  |  |
| bag_name | [uint32](#uint32) |  |  |
| bag_desc | [uint32](#uint32) |  |  |
| bag_icon_locked | [string](#string) |  |  |
| bag_icon_unlocked | [string](#string) |  |  |
| matrix | [string](#string) |  |  |
| max_matrix | [string](#string) |  |  |
| unlock_consume | [string](#string) |  |  |
| initial | [uint32](#uint32) |  |  |
| unlock_task_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_IslandGoods"></a>

### Sheet_Activity_IslandGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| goods_name | [uint32](#uint32) |  |  |
| matrix | [string](#string) |  |  |
| price | [uint32](#uint32) |  |  |
| goods_res | [string](#string) |  |  |
| icon | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_IslandMap"></a>

### Sheet_Activity_IslandMap



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| zone_id | [uint32](#uint32) |  |  |
| zone_name | [uint32](#uint32) |  |  |
| zone_icon_unlocked | [string](#string) |  |  |
| currency_amount | [uint32](#uint32) |  |  |
| initial | [uint32](#uint32) |  |  |
| distance | [uint32](#uint32) | repeated |  |
| route | [string](#string) | repeated |  |
| unlock_task_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_IslandNews"></a>

### Sheet_Activity_IslandNews



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |
| show_day | [uint32](#uint32) |  |  |
| news_date | [uint32](#uint32) |  |  |
| news_week | [uint32](#uint32) |  |  |
| zone | [int32](#int32) |  |  |
| news_desc | [uint32](#uint32) |  |  |
| goods_id | [int32](#int32) |  |  |
| effect | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_IslandShop"></a>

### Sheet_Activity_IslandShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |
| zone_id | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| discount | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_LiverEventInfo"></a>

### Sheet_Activity_LiverEventInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| follower_amount | [uint32](#uint32) |  |  |
| daily_follower_plus | [uint32](#uint32) |  |  |
| intro_text | [uint32](#uint32) |  |  |
| text_max_amount | [uint32](#uint32) |  |  |
| text_create_timer | [string](#string) |  |  |
| text_create_weight | [string](#string) |  |  |
| rolltext_speed | [uint32](#uint32) |  |  |
| gift_weight | [string](#string) |  |  |
| rolltext_gift_time | [string](#string) |  |  |
| key_item_id | [uint32](#uint32) |  |  |
| face_time_block | [string](#string) |  |  |
| face_weight | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_LiverTextInfo"></a>

### Sheet_Activity_LiverTextInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| chara_id | [uint32](#uint32) |  |  |
| mob_str_id | [uint32](#uint32) |  |  |
| normal_text | [string](#string) |  |  |
| gift_text | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_MineActivity"></a>

### Sheet_Activity_MineActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| reward_group | [uint32](#uint32) |  |  |
| cost_item | [string](#string) |  |  |
| map_size_x | [uint32](#uint32) |  |  |
| map_size_y | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_MineReward"></a>

### Sheet_Activity_MineReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |
| x | [uint32](#uint32) |  |  |
| y | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_PeriodTask"></a>

### Sheet_Activity_PeriodTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| interval | [uint32](#uint32) |  |  |
| progress_limit | [uint32](#uint32) |  |  |
| progress_limit_interval | [uint32](#uint32) |  |  |
| reward_limit_day | [uint32](#uint32) |  |  |
| accessible_days | [string](#string) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |
| node_mark | [uint32](#uint32) |  |  |
| omit_mail_reward | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_ProgressReward"></a>

### Sheet_Activity_ProgressReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| progress | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_RandomTaskInfo"></a>

### Sheet_Activity_RandomTaskInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| pool_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_RandomTaskPool"></a>

### Sheet_Activity_RandomTaskPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pool_id | [uint32](#uint32) |  |  |
| task_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| hidden_reward | [string](#string) |  |  |
| limit_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_Rank"></a>

### Sheet_Activity_Rank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| leaderboard_id | [uint32](#uint32) |  |  |
| rank_reward_id | [uint32](#uint32) |  |  |
| require_point | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RankReward"></a>

### Sheet_Activity_RankReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| lower_rank_bound | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_RewardMail"></a>

### Sheet_Activity_RewardMail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| mail_template_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RichmanEvent"></a>

### Sheet_Activity_RichmanEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| event_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| event_type | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| param | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_RichmanInfo"></a>

### Sheet_Activity_RichmanInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| map_id | [uint32](#uint32) |  |  |
| map_distance | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| consume_item_id | [uint32](#uint32) |  |  |
| special_item_id | [uint32](#uint32) |  |  |
| step_bank_save | [uint32](#uint32) |  |  |
| finish_bank_save | [uint32](#uint32) |  |  |
| finish_reward_seq | [uint32](#uint32) |  |  |
| step_exp | [uint32](#uint32) |  |  |
| finish_exp | [uint32](#uint32) |  |  |
| item_worth_pool | [uint32](#uint32) |  |  |
| min_avg_worth | [uint32](#uint32) |  |  |
| max_avg_worth | [uint32](#uint32) |  |  |
| chest_pool_seq | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RichmanLevel"></a>

### Sheet_Activity_RichmanLevel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| id | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| buff | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RichmanMap"></a>

### Sheet_Activity_RichmanMap



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| map_id | [uint32](#uint32) |  |  |
| location | [uint32](#uint32) |  |  |
| pos_x | [uint32](#uint32) |  |  |
| pos_y | [uint32](#uint32) |  |  |
| piece_face | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| param | [uint32](#uint32) |  |  |
| bonus_type | [uint32](#uint32) |  |  |
| worth | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RichmanRewardSeq"></a>

### Sheet_Activity_RichmanRewardSeq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_RpgActivity"></a>

### Sheet_Activity_RpgActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| base_hp | [uint32](#uint32) |  |  |
| base_atk | [uint32](#uint32) |  |  |
| base_dex | [uint32](#uint32) |  |  |
| base_luk | [uint32](#uint32) |  |  |
| ds_atk | [uint32](#uint32) |  |  |
| special_heal | [uint32](#uint32) |  |  |
| chain_atk | [uint32](#uint32) | repeated |  |
| monster_group | [uint32](#uint32) |  |  |
| sanma_debuff | [uint32](#uint32) |  |  |
| has_robot | [uint32](#uint32) |  |  |
| category | [string](#string) |  |  |
| mode | [string](#string) |  |  |
| room | [string](#string) |  |  |
| daily_limit | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RpgMonsterGroup"></a>

### Sheet_Activity_RpgMonsterGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| seq | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| hp | [uint32](#uint32) |  |  |
| atk | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| season | [uint32](#uint32) |  |  |
| chapters | [string](#string) |  |  |
| imaget_path | [string](#string) |  |  |
| background | [string](#string) |  |  |
| name_str_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_RpgV2Activity"></a>

### Sheet_Activity_RpgV2Activity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| base_atk | [uint32](#uint32) |  |  |
| monster_group | [uint32](#uint32) |  |  |
| sanma_debuff | [uint32](#uint32) |  |  |
| special_debuff | [uint32](#uint32) |  |  |
| has_robot | [uint32](#uint32) |  |  |
| category | [string](#string) |  |  |
| mode | [string](#string) |  |  |
| room | [string](#string) |  |  |
| daily_limit | [uint32](#uint32) |  |  |
| mail_template_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_SegmentTask"></a>

### Sheet_Activity_SegmentTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| max_finish_count | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| interval | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_SimulationActivityInfo"></a>

### Sheet_Activity_SimulationActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| stamina_item_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_SnsActivity"></a>

### Sheet_Activity_SnsActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| disable | [uint32](#uint32) |  |  |
| pm | [uint32](#uint32) |  |  |
| period | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| content_str_id | [uint32](#uint32) |  |  |
| parent_id | [uint32](#uint32) |  |  |
| char_id | [uint32](#uint32) |  |  |
| char_str_id | [uint32](#uint32) |  |  |
| reply_char_id | [uint32](#uint32) |  |  |
| reply_char_str_id | [uint32](#uint32) |  |  |
| choice_id | [uint32](#uint32) |  |  |
| like | [uint32](#uint32) |  |  |
| unlock_time | [string](#string) |  |  |
| unlock_item_id | [uint32](#uint32) |  |  |
| unlock_item_count | [uint32](#uint32) |  |  |
| content_image | [string](#string) | repeated |  |






<a name="lqc-Sheet_Activity_SpotActivity"></a>

### Sheet_Activity_SpotActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| dep | [uint32](#uint32) |  |  |
| limit_day | [uint32](#uint32) |  |  |
| unlock_task_id | [uint32](#uint32) |  |  |
| unlock_task_activity_id | [uint32](#uint32) |  |  |
| spot_group | [uint32](#uint32) |  |  |
| unlock_spot_item | [string](#string) |  |  |
| content_path | [string](#string) |  |  |
| title | [uint32](#uint32) |  |  |
| subtitle_title | [uint32](#uint32) |  |  |
| unlock_item | [string](#string) |  |  |
| unlock_by_ending_id | [uint32](#uint32) |  |  |
| unlock_ending_id | [string](#string) | repeated |  |
| ending_id | [uint32](#uint32) | repeated |  |
| ending_res | [string](#string) |  |  |
| ending_id_dep | [uint32](#uint32) | repeated |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_StoryActivity"></a>

### Sheet_Activity_StoryActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| unlock_item | [string](#string) |  |  |
| unlock_story | [string](#string) |  |  |
| unlock_ending | [string](#string) |  |  |
| unlock_consume | [string](#string) |  |  |
| finish_reward | [string](#string) |  |  |
| all_finish_reward | [string](#string) |  |  |
| content_path | [string](#string) |  |  |
| title | [uint32](#uint32) |  |  |
| subtitle_title | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_StoryEnding"></a>

### Sheet_Activity_StoryEnding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| story_id | [uint32](#uint32) |  |  |
| ending_id | [uint32](#uint32) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| unlock_item | [string](#string) |  |  |
| unlock_story | [string](#string) |  |  |
| unlock_ending | [string](#string) |  |  |
| unlock_consume | [string](#string) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_SummerStory"></a>

### Sheet_Activity_SummerStory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| story_name | [uint32](#uint32) |  |  |
| building | [uint32](#uint32) |  |  |
| building_name | [uint32](#uint32) |  |  |
| exchange_activity | [uint32](#uint32) |  |  |
| building_unlock | [uint32](#uint32) |  |  |
| story_unlock | [string](#string) |  |  |
| story_id | [string](#string) |  |  |
| story_desc | [uint32](#uint32) |  |  |
| show_character | [string](#string) |  |  |






<a name="lqc-Sheet_Activity_SummerStoryReward"></a>

### Sheet_Activity_SummerStoryReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| period_task_id | [uint32](#uint32) |  |  |
| building_icon | [string](#string) |  |  |
| click_notice | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_Task"></a>

### Sheet_Activity_Task



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |
| hidden_reward | [string](#string) |  |  |
| limit_id | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_TaskDisplay"></a>

### Sheet_Activity_TaskDisplay



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| day | [uint32](#uint32) |  |  |
| task_serial_number | [uint32](#uint32) |  |  |
| task_type | [uint32](#uint32) |  |  |
| period_task_id | [uint32](#uint32) |  |  |
| answer | [uint32](#uint32) |  |  |
| right_str | [uint32](#uint32) |  |  |
| wrong_str | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_UpgradeActivity"></a>

### Sheet_Activity_UpgradeActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| mail_id | [uint32](#uint32) |  |  |
| consume_item | [string](#string) |  |  |
| total_reward_id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Activity_UpgradeActivityDisplay"></a>

### Sheet_Activity_UpgradeActivityDisplay



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| display | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_UpgradeActivityReward"></a>

### Sheet_Activity_UpgradeActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| highlight | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_VillageActivityInfo"></a>

### Sheet_Activity_VillageActivityInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| worker_item_id | [uint32](#uint32) |  |  |
| round_consume | [string](#string) |  |  |
| random_building | [string](#string) |  |  |
| food_item_id | [uint32](#uint32) |  |  |
| trip_consume | [uint32](#uint32) |  |  |
| trip_cold_down | [uint32](#uint32) |  |  |
| trip_round | [uint32](#uint32) |  |  |
| trip_reward | [string](#string) | repeated |  |
| stage_require | [string](#string) | repeated |  |






<a name="lqc-Sheet_Activity_VillageBuilding"></a>

### Sheet_Activity_VillageBuilding



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| building_id | [uint32](#uint32) |  |  |
| initial | [uint32](#uint32) |  |  |
| building_name | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| next_level_id | [uint32](#uint32) |  |  |
| produce_item | [string](#string) |  |  |
| base_produce | [string](#string) |  |  |
| upgrade_item | [string](#string) |  |  |
| max_worker_count | [uint32](#uint32) |  |  |
| upgrade_reward | [string](#string) |  |  |
| building_stage | [uint32](#uint32) |  |  |
| worker_consume | [uint32](#uint32) |  |  |
| func | [string](#string) |  |  |
| args | [uint32](#uint32) | repeated |  |
| type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_VillageTask"></a>

### Sheet_Activity_VillageTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| mission_id | [uint32](#uint32) |  |  |
| mission_str | [uint32](#uint32) |  |  |
| fruit_type | [string](#string) |  |  |
| consume | [string](#string) |  |  |
| reward | [string](#string) |  |  |
| unlock_day | [uint32](#uint32) |  |  |
| unlock_point | [string](#string) |  |  |
| if_loop | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Activity_VoteActivity"></a>

### Sheet_Activity_VoteActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| vote_item | [uint32](#uint32) |  |  |
| choice_id_list | [string](#string) |  |  |
| vote_end_time | [string](#string) |  |  |






<a name="lqc-Sheet_Amulet_AmuletActivity"></a>

### Sheet_Amulet_AmuletActivity



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| skill_item | [uint32](#uint32) |  |  |
| init_coin | [uint32](#uint32) |  |  |
| shop_count | [uint32](#uint32) |  |  |
| record_level | [uint32](#uint32) |  |  |
| book_unlock_level | [uint32](#uint32) |  |  |
| free_effect_goods_id | [uint32](#uint32) |  |  |
| shop_refresh_coin | [uint32](#uint32) |  |  |
| effect_max_count | [uint32](#uint32) |  |  |
| init_dora_indicator | [uint32](#uint32) |  |  |
| init_change_hand | [uint32](#uint32) |  |  |
| init_desktop_count | [uint32](#uint32) |  |  |
| init_open_desktop_count | [uint32](#uint32) |  |  |
| init_shupai_point | [uint32](#uint32) |  |  |
| init_zipai_point | [uint32](#uint32) |  |  |
| init_mount_count | [uint32](#uint32) |  |  |
| init_level | [uint32](#uint32) |  |  |
| init_tian_count | [uint32](#uint32) |  |  |
| init_badge_weight | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Amulet_AmuletBadge"></a>

### Sheet_Amulet_AmuletBadge



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |
| coverable | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| rarity | [uint32](#uint32) |  |  |
| volume | [uint32](#uint32) |  |  |
| badge_name | [uint32](#uint32) |  |  |
| badge_desc | [uint32](#uint32) |  |  |
| badge_image | [string](#string) |  |  |
| args | [int32](#int32) | repeated |  |






<a name="lqc-Sheet_Amulet_AmuletBuff"></a>

### Sheet_Amulet_AmuletBuff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |
| common_weight | [uint32](#uint32) |  |  |
| ex_weight | [uint32](#uint32) |  |  |
| desc | [uint32](#uint32) |  |  |
| invalid_type | [uint32](#uint32) |  |  |
| args | [int32](#int32) | repeated |  |






<a name="lqc-Sheet_Amulet_AmuletEffect"></a>

### Sheet_Amulet_AmuletEffect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| book_enabled | [uint32](#uint32) |  |  |
| deprecated | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| effect_group | [uint32](#uint32) |  |  |
| shop_badge | [uint32](#uint32) |  |  |
| duplicate_enabled | [uint32](#uint32) |  |  |
| upgrade | [uint32](#uint32) |  |  |
| rarity | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| sell_price | [uint32](#uint32) |  |  |
| name | [uint32](#uint32) |  |  |
| desc | [uint32](#uint32) |  |  |
| card_image | [string](#string) |  |  |
| card_remark | [uint32](#uint32) |  |  |
| init_param_view | [uint32](#uint32) | repeated |  |
| args | [int32](#int32) | repeated |  |
| tag_id | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Amulet_AmuletEffectGroup"></a>

### Sheet_Amulet_AmuletEffectGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| merge_card | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletFan"></a>

### Sheet_Amulet_AmuletFan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| val | [uint32](#uint32) |  |  |
| desc | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletGames"></a>

### Sheet_Amulet_AmuletGames



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| target_point | [string](#string) |  |  |
| reward_pack | [string](#string) |  |  |
| reward | [uint32](#uint32) |  |  |
| boss | [uint32](#uint32) |  |  |
| next_level | [uint32](#uint32) |  |  |
| round | [uint32](#uint32) |  |  |
| clear_mark | [uint32](#uint32) |  |  |
| level_group | [uint32](#uint32) |  |  |
| level_name | [string](#string) |  |  |
| guaranteed_goods | [uint32](#uint32) |  |  |
| level_amulet_pool | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletGoods"></a>

### Sheet_Amulet_AmuletGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| guaranteed | [uint32](#uint32) |  |  |
| pack_name | [uint32](#uint32) |  |  |
| pack_desc | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| rarity_weight | [uint32](#uint32) | repeated |  |
| badge_weight | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Amulet_AmuletPool"></a>

### Sheet_Amulet_AmuletPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level_amulet_pool_id | [uint32](#uint32) |  |  |
| amulet_id | [uint32](#uint32) |  |  |
| amulet_weight | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletRewards"></a>

### Sheet_Amulet_AmuletRewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| target_point | [uint32](#uint32) |  |  |
| reward_coin | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletShopUpgrade"></a>

### Sheet_Amulet_AmuletShopUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| display_value | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletTag"></a>

### Sheet_Amulet_AmuletTag



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tag_id | [uint32](#uint32) |  |  |
| tag_name | [uint32](#uint32) |  |  |
| tag_desc | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Amulet_AmuletTask"></a>

### Sheet_Amulet_AmuletTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| amulet_id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| base_task_id | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Amulet_AmuletUpgrade"></a>

### Sheet_Amulet_AmuletUpgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| skill_point | [uint32](#uint32) |  |  |
| buff_id | [uint32](#uint32) |  |  |
| display_value | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Animation_Animation"></a>

### Sheet_Animation_Animation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| type | [string](#string) |  |  |
| lifetime | [uint32](#uint32) |  |  |
| speed | [float](#float) |  |  |
| keypoint | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Audio_Audio"></a>

### Sheet_Audio_Audio



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| path | [string](#string) |  |  |
| time_length | [float](#float) |  |  |
| type | [string](#string) |  |  |






<a name="lqc-Sheet_Audio_Bgm"></a>

### Sheet_Audio_Bgm



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| auto_hide | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| path | [string](#string) |  |  |
| time_length | [float](#float) |  |  |
| type | [string](#string) |  |  |
| unlock_desc_chs | [string](#string) |  |  |
| unlock_desc_chs_t | [string](#string) |  |  |
| unlock_desc_jp | [string](#string) |  |  |
| unlock_desc_en | [string](#string) |  |  |
| unlock_desc_kr | [string](#string) |  |  |
| unlock_item | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Character_Cutin"></a>

### Sheet_Character_Cutin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skinid | [uint32](#uint32) |  |  |
| cutin_name | [string](#string) |  |  |
| effect | [string](#string) |  |  |
| atlas | [string](#string) |  |  |
| char_x | [int32](#int32) |  |  |
| char_y | [int32](#int32) |  |  |
| char_width | [uint32](#uint32) |  |  |
| char_height | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Character_Emoji"></a>

### Sheet_Character_Emoji



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| charid | [uint32](#uint32) |  |  |
| sub_id | [uint32](#uint32) |  |  |
| unlock_desc_chs | [string](#string) |  |  |
| unlock_desc_chs_t | [string](#string) |  |  |
| unlock_desc_jp | [string](#string) |  |  |
| unlock_desc_en | [string](#string) |  |  |
| unlock_desc_kr | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |
| view | [string](#string) |  |  |
| audio | [uint32](#uint32) |  |  |
| after_unlock_desc_chs | [string](#string) |  |  |
| after_unlock_desc_chs_t | [string](#string) |  |  |
| after_unlock_desc_jp | [string](#string) |  |  |
| after_unlock_desc_en | [string](#string) |  |  |
| after_unlock_desc_kr | [string](#string) |  |  |
| unlock_type | [uint32](#uint32) |  |  |
| unlock_param | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Character_Skin"></a>

### Sheet_Character_Skin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skinid | [uint32](#uint32) |  |  |
| spine_layers | [uint32](#uint32) |  |  |
| effects | [string](#string) | repeated |  |
| audio_celebrate | [string](#string) |  |  |
| audio_celebrate_idle | [string](#string) |  |  |
| audio_idle | [string](#string) |  |  |
| audio_greeting | [string](#string) |  |  |
| audio_click | [string](#string) |  |  |
| audio_click2 | [string](#string) |  |  |
| celebrate_delay | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_Chest"></a>

### Sheet_Chest_Chest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| img | [string](#string) |  |  |
| gift | [uint32](#uint32) |  |  |
| currency | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| price10 | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |
| ticket_10_id | [uint32](#uint32) |  |  |
| faith_id | [uint32](#uint32) |  |  |
| zone | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_ChestShop"></a>

### Sheet_Chest_ChestShop



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| item_id | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| need_amount | [uint32](#uint32) |  |  |
| check_activity | [uint32](#uint32) |  |  |
| launch_time | [string](#string) |  |  |
| remove_limit_mark | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_ItemPool"></a>

### Sheet_Chest_ItemPool







<a name="lqc-Sheet_Chest_ItemPrice"></a>

### Sheet_Chest_ItemPrice







<a name="lqc-Sheet_Chest_Pool"></a>

### Sheet_Chest_Pool







<a name="lqc-Sheet_Chest_PoolSeq"></a>

### Sheet_Chest_PoolSeq







<a name="lqc-Sheet_Chest_Preview"></a>

### Sheet_Chest_Preview



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |
| check_activity | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_ReplacePool"></a>

### Sheet_Chest_ReplacePool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| resource_id | [uint32](#uint32) |  |  |
| is_replace | [uint32](#uint32) |  |  |
| add_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_ReplaceUp"></a>

### Sheet_Chest_ReplaceUp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| replace_pool_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| count_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Chest_Up"></a>

### Sheet_Chest_Up







<a name="lqc-Sheet_Compose_Characompose"></a>

### Sheet_Compose_Characompose



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| item_num | [uint32](#uint32) |  |  |
| chara_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Contest_Contest"></a>

### Sheet_Contest_Contest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| int_value | [int32](#int32) |  |  |






<a name="lqc-Sheet_Desktop_Chest"></a>

### Sheet_Desktop_Chest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| exp_step | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| reward_pool | [uint32](#uint32) |  |  |
| select_count | [uint32](#uint32) |  |  |
| repeated | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Desktop_FieldSpell"></a>

### Sheet_Desktop_FieldSpell



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| cardname | [string](#string) |  |  |
| sord_card_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Desktop_FriendRoom"></a>

### Sheet_Desktop_FriendRoom



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| pre_rule | [string](#string) |  |  |
| sort | [uint32](#uint32) |  |  |
| str_name | [string](#string) |  |  |
| str_rule | [string](#string) |  |  |
| set_jushu | [uint32](#uint32) |  |  |
| rule_images | [string](#string) | repeated |  |






<a name="lqc-Sheet_Desktop_Matchmode"></a>

### Sheet_Desktop_Matchmode



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| is_open | [uint32](#uint32) |  |  |
| match_group | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| open_guyi | [uint32](#uint32) |  |  |
| dora3_mode | [uint32](#uint32) |  |  |
| begin_open_mode | [uint32](#uint32) |  |  |
| muyu_mode | [uint32](#uint32) |  |  |
| xuezhan_mode | [uint32](#uint32) |  |  |
| chuanma_mode | [uint32](#uint32) |  |  |
| huanzhang_mode | [uint32](#uint32) |  |  |
| jiuchao_mode | [uint32](#uint32) |  |  |
| reveal_discard | [uint32](#uint32) |  |  |
| field_spell_mode | [uint32](#uint32) |  |  |
| zhanxing_mode | [uint32](#uint32) |  |  |
| tianming_mode | [uint32](#uint32) |  |  |
| yongchang_mode | [uint32](#uint32) |  |  |
| hunzhiyiji_mode | [uint32](#uint32) |  |  |
| wanxiangxiuluo_mode | [uint32](#uint32) |  |  |
| beishuizhizhan_mode | [uint32](#uint32) |  |  |
| room | [uint32](#uint32) |  |  |
| mode | [uint32](#uint32) |  |  |
| can_sumup | [uint32](#uint32) |  |  |
| room_name_chs | [string](#string) |  |  |
| room_name_chs_t | [string](#string) |  |  |
| room_name_jp | [string](#string) |  |  |
| room_name_en | [string](#string) |  |  |
| room_name_kr | [string](#string) |  |  |
| str_rule | [string](#string) |  |  |
| interval_image | [string](#string) |  |  |
| rule_images | [string](#string) | repeated |  |
| glimit_floor | [int32](#int32) |  |  |
| glimit_ceil | [int32](#int32) |  |  |
| gcarry | [int32](#int32) |  |  |
| exchange_rate | [int32](#int32) |  |  |
| levelpoint1 | [int32](#int32) |  |  |
| levelpoint2 | [int32](#int32) |  |  |
| levelpoint3 | [int32](#int32) |  |  |
| levelpoint4 | [int32](#int32) |  |  |
| fish_point | [int32](#int32) |  |  |
| init_point | [int32](#int32) |  |  |
| back_point | [int32](#int32) |  |  |
| count_point | [int32](#int32) |  |  |
| buchang | [int32](#int32) | repeated |  |
| level_limit | [uint32](#uint32) |  |  |
| level_limit_ceil | [uint32](#uint32) |  |  |
| tip | [int32](#int32) |  |  |
| friendship | [int32](#int32) |  |  |
| chest_id | [uint32](#uint32) |  |  |
| chest_exp_add | [uint32](#uint32) | repeated |  |
| level_match | [uint32](#uint32) |  |  |
| level_match_range | [uint32](#uint32) |  |  |
| level_match_max | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Desktop_Settings"></a>

### Sheet_Desktop_Settings



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| int_value | [int32](#int32) |  |  |






<a name="lqc-Sheet_Desktop_TourPresetRule"></a>

### Sheet_Desktop_TourPresetRule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| preset_rule | [uint32](#uint32) |  |  |
| params | [int32](#int32) | repeated |  |






<a name="lqc-Sheet_Events_BaseTask"></a>

### Sheet_Events_BaseTask



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |
| target | [uint32](#uint32) |  |  |
| param | [string](#string) | repeated |  |






<a name="lqc-Sheet_Events_Dailyevent"></a>

### Sheet_Events_Dailyevent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| reward_type | [uint32](#uint32) |  |  |
| reward_num | [uint32](#uint32) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| active_type | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| target | [uint32](#uint32) |  |  |
| param | [string](#string) | repeated |  |
| level_limit | [string](#string) |  |  |






<a name="lqc-Sheet_Events_Soscoin"></a>

### Sheet_Events_Soscoin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level_limit | [uint32](#uint32) |  |  |
| level3_limit | [uint32](#uint32) |  |  |
| gold_limit | [uint32](#uint32) |  |  |
| gold_num | [uint32](#uint32) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |






<a name="lqc-Sheet_Exchange_Exchange"></a>

### Sheet_Exchange_Exchange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| source_currency | [uint32](#uint32) |  |  |
| source_value | [int32](#int32) |  |  |
| target_currency | [uint32](#uint32) |  |  |
| target_value | [int32](#int32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |






<a name="lqc-Sheet_Exchange_Fushiquanexchange"></a>

### Sheet_Exchange_Fushiquanexchange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| source_currency | [uint32](#uint32) |  |  |
| source_value | [int32](#int32) |  |  |
| target_currency | [uint32](#uint32) |  |  |
| target_value | [int32](#int32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |






<a name="lqc-Sheet_Exchange_Searchexchange"></a>

### Sheet_Exchange_Searchexchange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| source_currency | [uint32](#uint32) |  |  |
| source_value | [int32](#int32) |  |  |
| target_currency | [uint32](#uint32) |  |  |
| target_value | [int32](#int32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kor | [string](#string) |  |  |






<a name="lqc-Sheet_Fan_Fan"></a>

### Sheet_Fan_Fan



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| xuanshang | [uint32](#uint32) |  |  |
| yiman | [uint32](#uint32) |  |  |
| fan_menqing | [uint32](#uint32) |  |  |
| fan_fulu | [uint32](#uint32) |  |  |
| show_index | [uint32](#uint32) |  |  |
| sound | [string](#string) |  |  |
| is_guyi | [uint32](#uint32) |  |  |
| rarity | [uint32](#uint32) |  |  |
| show_range_1 | [uint32](#uint32) |  |  |
| show_range_2 | [string](#string) |  |  |
| merge_id | [uint32](#uint32) |  |  |
| mark | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Fandesc_Fandesc"></a>

### Sheet_Fandesc_Fandesc



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| tag | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| desc2_chs | [string](#string) |  |  |
| desc2_jp | [string](#string) |  |  |
| desc2_en | [string](#string) |  |  |
| desc2_chs_t | [string](#string) |  |  |
| desc2_kr | [string](#string) |  |  |
| case | [string](#string) |  |  |
| show | [uint32](#uint32) |  |  |
| mode | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_GameLive_SelectFilters"></a>

### Sheet_GameLive_SelectFilters



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| category | [uint32](#uint32) |  |  |
| mode_id | [uint32](#uint32) |  |  |
| mode | [uint32](#uint32) |  |  |
| tournament_id | [uint32](#uint32) |  |  |
| open | [uint32](#uint32) |  |  |
| initial | [uint32](#uint32) |  |  |
| name1_chs | [string](#string) |  |  |
| name1_chs_t | [string](#string) |  |  |
| name1_jp | [string](#string) |  |  |
| name1_en | [string](#string) |  |  |
| name1_kr | [string](#string) |  |  |
| name2_chs | [string](#string) |  |  |
| name2_chs_t | [string](#string) |  |  |
| name2_jp | [string](#string) |  |  |
| name2_en | [string](#string) |  |  |
| name2_kr | [string](#string) |  |  |






<a name="lqc-Sheet_Global_Global"></a>

### Sheet_Global_Global



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| args | [string](#string) |  |  |






<a name="lqc-Sheet_Info_Error"></a>

### Sheet_Info_Error



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| chs | [string](#string) |  |  |
| chs_t | [string](#string) |  |  |
| jp | [string](#string) |  |  |
| en | [string](#string) |  |  |
| kr | [string](#string) |  |  |






<a name="lqc-Sheet_Info_Forbidden"></a>

### Sheet_Info_Forbidden



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| word | [string](#string) |  |  |
| type_chs | [uint32](#uint32) |  |  |
| near_chs | [uint32](#uint32) |  |  |
| chs | [uint32](#uint32) |  |  |
| type_us | [uint32](#uint32) |  |  |
| near_us | [uint32](#uint32) |  |  |
| us | [uint32](#uint32) |  |  |
| type_jp | [uint32](#uint32) |  |  |
| near_jp | [uint32](#uint32) |  |  |
| jp | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Info_Near"></a>

### Sheet_Info_Near



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| word1 | [string](#string) |  |  |
| word2 | [string](#string) |  |  |
| word3 | [string](#string) |  |  |
| word4 | [string](#string) |  |  |
| word5 | [string](#string) |  |  |






<a name="lqc-Sheet_Info_Translate"></a>

### Sheet_Info_Translate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| original | [string](#string) |  |  |
| chs | [string](#string) |  |  |
| chs_t | [string](#string) |  |  |
| jp | [string](#string) |  |  |
| en | [string](#string) |  |  |
| kr | [string](#string) |  |  |






<a name="lqc-Sheet_ItemDefinition_Character"></a>

### Sheet_ItemDefinition_Character



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| launch_time | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs2 | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_chs_t2 | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_jp2 | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| open | [uint32](#uint32) |  |  |
| init_skin | [uint32](#uint32) |  |  |
| full_fetter_skin | [uint32](#uint32) |  |  |
| hand | [uint32](#uint32) |  |  |
| favorite | [uint32](#uint32) |  |  |
| star_5_material | [string](#string) |  |  |
| star_5_cost | [uint32](#uint32) |  |  |
| can_marry | [uint32](#uint32) |  |  |
| exchange_item_id | [uint32](#uint32) |  |  |
| exchange_item_num | [int32](#int32) |  |  |
| emo | [string](#string) |  |  |
| sound | [uint32](#uint32) |  |  |
| sound_volume | [float](#float) |  |  |
| sex | [uint32](#uint32) |  |  |
| desc_stature_chs | [string](#string) |  |  |
| desc_stature_chs_t | [string](#string) |  |  |
| desc_stature_jp | [string](#string) |  |  |
| desc_stature_en | [string](#string) |  |  |
| desc_stature_kr | [string](#string) |  |  |
| desc_birth_chs | [string](#string) |  |  |
| desc_birth_chs_t | [string](#string) |  |  |
| desc_birth_jp | [string](#string) |  |  |
| desc_birth_en | [string](#string) |  |  |
| desc_birth_kr | [string](#string) |  |  |
| desc_age_chs | [string](#string) |  |  |
| desc_age_chs_t | [string](#string) |  |  |
| desc_age_jp | [string](#string) |  |  |
| desc_age_en | [string](#string) |  |  |
| desc_age_kr | [string](#string) |  |  |
| desc_bloodtype_chs | [string](#string) |  |  |
| desc_bloodtype_chs_t | [string](#string) |  |  |
| desc_bloodtype_jp | [string](#string) |  |  |
| desc_bloodtype_en | [string](#string) |  |  |
| desc_bloodtype_kr | [string](#string) |  |  |
| desc_cv_chs | [string](#string) |  |  |
| desc_cv_chs_t | [string](#string) |  |  |
| desc_cv_jp | [string](#string) |  |  |
| desc_cv_en | [string](#string) |  |  |
| desc_cv_kr | [string](#string) |  |  |
| desc_hobby_chs | [string](#string) |  |  |
| desc_hobby_chs_t | [string](#string) |  |  |
| desc_hobby_jp | [string](#string) |  |  |
| desc_hobby_en | [string](#string) |  |  |
| desc_hobby_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_item_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_item_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_item_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_item_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| desc_item_kr | [string](#string) |  |  |
| collaboration | [uint32](#uint32) |  |  |
| region_limit | [uint32](#uint32) |  |  |
| skin_lib | [uint32](#uint32) | repeated |  |
| ur | [uint32](#uint32) |  |  |
| ur_ron | [uint32](#uint32) |  |  |
| ur_liqi | [uint32](#uint32) |  |  |
| ur_cutin | [string](#string) |  |  |
| limited | [uint32](#uint32) |  |  |
| treasure_sp | [uint32](#uint32) |  |  |
| blink | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_Currency"></a>

### Sheet_ItemDefinition_Currency



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| icon_jpg | [string](#string) |  |  |






<a name="lqc-Sheet_ItemDefinition_FakeRandomPool"></a>

### Sheet_ItemDefinition_FakeRandomPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| stage_count | [uint32](#uint32) | repeated |  |
| stage_weight | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_ItemDefinition_FunctionItem"></a>

### Sheet_ItemDefinition_FunctionItem



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| args | [uint32](#uint32) | repeated |  |
| name | [uint32](#uint32) |  |  |
| desc_func | [uint32](#uint32) |  |  |
| desc | [uint32](#uint32) |  |  |
| icon | [string](#string) |  |  |
| icon_transparent | [string](#string) |  |  |






<a name="lqc-Sheet_ItemDefinition_Item"></a>

### Sheet_ItemDefinition_Item



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_chs_t2 | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_func_chs | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_func_chs_t | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_chs_t2 | [string](#string) |  |  |
| desc_func_jp | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_func_en | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_func_kr | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| icon_transparent | [string](#string) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| is_unique | [uint32](#uint32) |  |  |
| max_stack | [uint32](#uint32) |  |  |
| access | [string](#string) |  |  |
| accessinfo | [uint32](#uint32) |  |  |
| func | [string](#string) |  |  |
| iargs | [uint32](#uint32) | repeated |  |
| sargs | [string](#string) | repeated |  |
| can_sell | [uint32](#uint32) |  |  |
| sell_reward_id | [uint32](#uint32) |  |  |
| sell_reward_count | [uint32](#uint32) |  |  |
| item_expire | [string](#string) |  |  |
| expire_desc_chs | [string](#string) |  |  |
| expire_desc_chs_t | [string](#string) |  |  |
| expire_desc_jp | [string](#string) |  |  |
| expire_desc_en | [string](#string) |  |  |
| expire_desc_kr | [string](#string) |  |  |
| region_limit | [uint32](#uint32) |  |  |
| cross_view | [uint32](#uint32) |  |  |
| database_cache | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_ItemManualPool"></a>

### Sheet_ItemDefinition_ItemManualPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| res_id | [uint32](#uint32) |  |  |
| res_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_ItemPackage"></a>

### Sheet_ItemDefinition_ItemPackage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| res_id | [uint32](#uint32) |  |  |
| res_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_ItemRecovery"></a>

### Sheet_ItemDefinition_ItemRecovery







<a name="lqc-Sheet_ItemDefinition_LoadingImage"></a>

### Sheet_ItemDefinition_LoadingImage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| img_path | [string](#string) |  |  |
| thumb_path | [string](#string) |  |  |
| sort | [uint32](#uint32) |  |  |
| unlock_items | [uint32](#uint32) | repeated |  |
| args | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_ItemDefinition_Skin"></a>

### Sheet_ItemDefinition_Skin



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_jp2 | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| character_id | [uint32](#uint32) |  |  |
| lock_tips_chs | [string](#string) |  |  |
| lock_tips_chs_t | [string](#string) |  |  |
| lock_tips_jp | [string](#string) |  |  |
| lock_tips_en | [string](#string) |  |  |
| lock_tips_kr | [string](#string) |  |  |
| path | [string](#string) |  |  |
| exchange_item_id | [uint32](#uint32) |  |  |
| exchange_item_num | [int32](#int32) |  |  |
| direction | [uint32](#uint32) |  |  |
| no_reverse | [uint32](#uint32) |  |  |
| lock_reverse | [uint32](#uint32) |  |  |
| offset_x | [int32](#int32) |  |  |
| offset_y | [int32](#int32) |  |  |
| spot_scale | [string](#string) |  |  |
| effective_time | [string](#string) |  |  |
| lobby_offset | [string](#string) |  |  |
| liaoshe_offset | [string](#string) |  |  |
| shop_offset | [string](#string) |  |  |
| win_offset | [string](#string) |  |  |
| gameend_offset | [string](#string) |  |  |
| starup_offset | [string](#string) |  |  |
| treasure_offset | [string](#string) |  |  |
| ck_full_0_offset | [string](#string) |  |  |
| ck_full_1_offset | [string](#string) |  |  |
| ck_full_2_offset | [string](#string) |  |  |
| ck_full_3_offset | [string](#string) |  |  |
| ck_full_single_offset | [string](#string) |  |  |
| ck_half_0_offset | [string](#string) |  |  |
| ck_half_1_offset | [string](#string) |  |  |
| ck_half_2_offset | [string](#string) |  |  |
| ck_half_3_offset | [string](#string) |  |  |
| ck_half_single_offset | [string](#string) |  |  |
| smallhead_x | [int32](#int32) |  |  |
| smallhead_y | [int32](#int32) |  |  |
| smallhead_width | [int32](#int32) |  |  |
| full_x | [int32](#int32) |  |  |
| full_y | [int32](#int32) |  |  |
| full_width | [int32](#int32) |  |  |
| full_height | [int32](#int32) |  |  |
| half_x | [int32](#int32) |  |  |
| half_y | [int32](#int32) |  |  |
| half_width | [int32](#int32) |  |  |
| half_height | [int32](#int32) |  |  |
| spine_type | [int32](#int32) |  |  |
| spine_width | [int32](#int32) |  |  |
| spine_height | [int32](#int32) |  |  |
| pivot_x | [int32](#int32) |  |  |
| pivot_y | [int32](#int32) |  |  |
| idle | [int32](#int32) |  |  |
| greeting | [int32](#int32) |  |  |
| celebrate | [int32](#int32) |  |  |
| click | [int32](#int32) |  |  |
| greeting_init | [int32](#int32) |  |  |
| click2 | [int32](#int32) |  |  |
| celebrate_idle | [int32](#int32) |  |  |
| illust_data | [string](#string) |  |  |






<a name="lqc-Sheet_ItemDefinition_SourceLimit"></a>

### Sheet_ItemDefinition_SourceLimit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| item_limit | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_Title"></a>

### Sheet_ItemDefinition_Title



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| icon_item | [string](#string) |  |  |
| priority | [uint32](#uint32) |  |  |
| unlock_type | [uint32](#uint32) |  |  |
| unlock_param | [uint32](#uint32) | repeated |  |
| cross_view | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_ItemDefinition_View"></a>

### Sheet_ItemDefinition_View



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| res_name | [string](#string) |  |  |
| audio_id | [uint32](#uint32) |  |  |
| character_id | [uint32](#uint32) |  |  |
| sargs | [string](#string) | repeated |  |
| old_effect_mark | [uint32](#uint32) |  |  |
| new_hand | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Leaderboard_Leaderboard"></a>

### Sheet_Leaderboard_Leaderboard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| start_time | [string](#string) |  |  |
| end_time | [string](#string) |  |  |
| refresh_cd | [uint32](#uint32) |  |  |
| max_count | [uint32](#uint32) |  |  |
| show_list | [string](#string) |  |  |






<a name="lqc-Sheet_LevelDefinition_Character"></a>

### Sheet_LevelDefinition_Character



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| character_id | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| reward | [string](#string) |  |  |
| unlock_says | [uint32](#uint32) |  |  |
| unlock_desc_chs | [string](#string) |  |  |
| unlock_desc_chs_t | [string](#string) |  |  |
| unlock_desc_jp | [string](#string) |  |  |
| unlock_desc_en | [string](#string) |  |  |
| unlock_desc_kr | [string](#string) |  |  |






<a name="lqc-Sheet_LevelDefinition_LevelDefinition"></a>

### Sheet_LevelDefinition_LevelDefinition



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [int32](#int32) |  |  |
| primary_level | [uint32](#uint32) |  |  |
| secondary_level | [uint32](#uint32) |  |  |
| init_point | [uint32](#uint32) |  |  |
| end_point | [uint32](#uint32) |  |  |
| primary_icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| full_name_chs | [string](#string) |  |  |
| full_name_chs_t | [string](#string) |  |  |
| full_name_jp | [string](#string) |  |  |
| full_name_en | [string](#string) |  |  |
| full_name_kr | [string](#string) |  |  |
| can_degrade | [uint32](#uint32) |  |  |
| can_upgrade | [uint32](#uint32) |  |  |
| can_getpoint | [uint32](#uint32) |  |  |
| rankpt1 | [int32](#int32) |  |  |
| rankpt2 | [int32](#int32) |  |  |
| top_rank_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_LevelDefinition_TopRank"></a>

### Sheet_LevelDefinition_TopRank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| rank_pt | [int32](#int32) | repeated |  |
| top_rank_pt | [int32](#int32) | repeated |  |
| mode | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_LevelDefinition_Trail"></a>

### Sheet_LevelDefinition_Trail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| init_level | [uint32](#uint32) |  |  |
| end_level | [uint32](#uint32) |  |  |
| trail_icon | [uint32](#uint32) |  |  |
| trail_fire | [int32](#int32) |  |  |






<a name="lqc-Sheet_Mall_ChannelConfig"></a>

### Sheet_Mall_ChannelConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| currency_platforms | [string](#string) |  |  |
| free_jade_ids | [string](#string) |  |  |
| paid_jade_ids | [string](#string) |  |  |
| free_voucher_ids | [string](#string) |  |  |
| paid_voucher_ids | [string](#string) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| shelves_id | [string](#string) |  |  |
| name | [string](#string) |  |  |






<a name="lqc-Sheet_Mall_Goods"></a>

### Sheet_Mall_Goods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| icon | [string](#string) |  |  |
| resource_id | [uint32](#uint32) |  |  |
| resource_count | [uint32](#uint32) |  |  |
| vip_exp | [uint32](#uint32) |  |  |
| cny | [uint32](#uint32) |  |  |
| price | [string](#string) |  |  |
| first_desc_chs | [string](#string) |  |  |
| first_desc_chs_t | [string](#string) |  |  |
| first_desc_jp | [string](#string) |  |  |
| first_desc_en | [string](#string) |  |  |
| first_desc_kr | [string](#string) |  |  |
| first_extend_add | [uint32](#uint32) |  |  |
| normal_desc_chs | [string](#string) |  |  |
| normal_desc_chs_t | [string](#string) |  |  |
| normal_desc_jp | [string](#string) |  |  |
| normal_desc_en | [string](#string) |  |  |
| normal_desc_kr | [string](#string) |  |  |
| normal_extend_add | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Mall_GoodsShelves"></a>

### Sheet_Mall_GoodsShelves



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| currency_code | [string](#string) |  |  |
| currency_price | [uint32](#uint32) |  |  |
| price | [string](#string) |  |  |
| is_monthcard | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Mall_MonthTicket"></a>

### Sheet_Mall_MonthTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| resource_id | [uint32](#uint32) |  |  |
| resource_count | [uint32](#uint32) |  |  |
| vip_exp | [uint32](#uint32) |  |  |
| effective_time | [uint32](#uint32) |  |  |
| icon | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| desc_detail_chs | [string](#string) |  |  |
| desc_detail_chs_t | [string](#string) |  |  |
| desc_detail_jp | [string](#string) |  |  |
| desc_detail_en | [string](#string) |  |  |
| desc_detail_kr | [string](#string) |  |  |
| desc_detail2_chs | [string](#string) |  |  |
| desc_detail2_chs_t | [string](#string) |  |  |
| desc_detail2_jp | [string](#string) |  |  |
| desc_detail2_en | [string](#string) |  |  |
| desc_detail2_kr | [string](#string) |  |  |






<a name="lqc-Sheet_Mall_MonthTicketInfo"></a>

### Sheet_Mall_MonthTicketInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Mall_Product"></a>

### Sheet_Mall_Product



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| payment_platform | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| product_type | [uint32](#uint32) |  |  |
| product_id | [string](#string) |  |  |
| currency_code | [string](#string) |  |  |
| currency_price | [uint32](#uint32) |  |  |
| actual_code | [string](#string) |  |  |
| actual_price | [uint32](#uint32) |  |  |
| brief_desc | [string](#string) |  |  |
| detail_desc | [string](#string) |  |  |






<a name="lqc-Sheet_Mall_ZoneParams"></a>

### Sheet_Mall_ZoneParams



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| zone_id | [string](#string) |  |  |
| key | [string](#string) |  |  |
| string_value | [string](#string) |  |  |






<a name="lqc-Sheet_MatchShilian_Shilian"></a>

### Sheet_MatchShilian_Shilian



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| ticket_id | [uint32](#uint32) |  |  |
| currency_id | [uint32](#uint32) |  |  |
| currency_count | [uint32](#uint32) |  |  |
| mode | [uint32](#uint32) |  |  |
| mode1 | [uint32](#uint32) |  |  |
| mode2 | [uint32](#uint32) |  |  |
| init_point | [int32](#int32) |  |  |
| back_point | [int32](#int32) |  |  |






<a name="lqc-Sheet_MatchShilian_ShilianReward"></a>

### Sheet_MatchShilian_ShilianReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_MatchShilian_ShilianTime"></a>

### Sheet_MatchShilian_ShilianTime



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| start | [string](#string) |  |  |
| end | [string](#string) |  |  |






<a name="lqc-Sheet_MiscFunction_DailySignIn"></a>

### Sheet_MiscFunction_DailySignIn



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| reward_id | [uint32](#uint32) |  |  |
| reward_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_EffectLiqi"></a>

### Sheet_OutfitConfig_EffectLiqi



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Hand"></a>

### Sheet_OutfitConfig_Hand



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Headframe"></a>

### Sheet_OutfitConfig_Headframe



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Liqi"></a>

### Sheet_OutfitConfig_Liqi



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Mjp"></a>

### Sheet_OutfitConfig_Mjp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Mjpface"></a>

### Sheet_OutfitConfig_Mjpface



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Mpzs"></a>

### Sheet_OutfitConfig_Mpzs



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Ron"></a>

### Sheet_OutfitConfig_Ron



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| is_fullscreen | [uint32](#uint32) |  |  |
| queue_change_delay | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_OutfitConfig_Tablecloth"></a>

### Sheet_OutfitConfig_Tablecloth



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_RankIntroduce_Rank"></a>

### Sheet_RankIntroduce_Rank



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| info | [string](#string) | repeated |  |






<a name="lqc-Sheet_RankIntroduce_Rank3"></a>

### Sheet_RankIntroduce_Rank3



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| info | [string](#string) | repeated |  |






<a name="lqc-Sheet_Season_LevelTicket"></a>

### Sheet_Season_LevelTicket



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| level | [uint32](#uint32) |  |  |
| game_count | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| task | [uint32](#uint32) | repeated |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Season_LevelTicketPool"></a>

### Sheet_Season_LevelTicketPool



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pool_id | [uint32](#uint32) |  |  |
| level_lower | [uint32](#uint32) |  |  |
| level_upper | [uint32](#uint32) |  |  |
| ticket_level | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Season_Season"></a>

### Sheet_Season_Season



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| start_time | [string](#string) |  |  |
| end_time | [string](#string) |  |  |
| disappear_time | [string](#string) |  |  |
| match_mode | [uint32](#uint32) |  |  |
| level_ticket_pool | [uint32](#uint32) |  |  |
| ticket_retry | [uint32](#uint32) |  |  |
| point_item_id | [uint32](#uint32) |  |  |
| point_consume | [uint32](#uint32) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| desktop_type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Season_SeasonReward"></a>

### Sheet_Season_SeasonReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| season_id | [uint32](#uint32) |  |  |
| rank_lower | [uint32](#uint32) |  |  |
| rank_upper | [uint32](#uint32) |  |  |
| rewards | [string](#string) |  |  |






<a name="lqc-Sheet_Season_TicketRetry"></a>

### Sheet_Season_TicketRetry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| cost | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Shops_Goods"></a>

### Sheet_Shops_Goods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| category | [uint32](#uint32) |  |  |
| category_goods | [uint32](#uint32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| item_id | [uint32](#uint32) |  |  |
| price | [string](#string) |  |  |
| show_original_price | [string](#string) |  |  |
| need_amount | [uint32](#uint32) |  |  |
| buy_limit | [int32](#int32) |  |  |
| show_has | [int32](#int32) |  |  |
| sort | [uint32](#uint32) |  |  |
| discount | [uint32](#uint32) |  |  |
| sell_activity | [uint32](#uint32) |  |  |
| launch_time | [string](#string) |  |  |
| func | [string](#string) |  |  |
| discount_activity | [uint32](#uint32) |  |  |
| zone | [string](#string) |  |  |






<a name="lqc-Sheet_Shops_GoodsPackage"></a>

### Sheet_Shops_GoodsPackage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| good_id | [uint32](#uint32) |  |  |
| good_count | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Shops_IntervalRefreshGoods"></a>

### Sheet_Shops_IntervalRefreshGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| group_id | [uint32](#uint32) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| interval | [uint32](#uint32) |  |  |
| interval_type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Shops_ItemPackage"></a>

### Sheet_Shops_ItemPackage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_info | [string](#string) |  |  |






<a name="lqc-Sheet_Shops_ZhpGoods"></a>

### Sheet_Shops_ZhpGoods



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| icon | [string](#string) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| item_id | [uint32](#uint32) |  |  |
| name_kr | [string](#string) |  |  |
| buy_limit | [int32](#int32) |  |  |
| currency | [uint32](#uint32) |  |  |
| price | [uint32](#uint32) |  |  |
| need_amount | [uint32](#uint32) |  |  |
| show_has | [int32](#int32) |  |  |






<a name="lqc-Sheet_Shops_ZhpRefreshGroup"></a>

### Sheet_Shops_ZhpRefreshGroup







<a name="lqc-Sheet_Shops_ZhpRefreshPrice"></a>

### Sheet_Shops_ZhpRefreshPrice



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| refresh_price | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Buff"></a>

### Sheet_Simulation_SimV2Buff



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buff_id | [uint32](#uint32) |  |  |
| buff_result_desc | [uint32](#uint32) |  |  |
| buff_desc | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| match_effect | [uint32](#uint32) |  |  |
| param | [string](#string) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2Character"></a>

### Sheet_Simulation_SimV2Character



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| luk | [uint32](#uint32) |  |  |
| tec | [uint32](#uint32) |  |  |
| ins | [uint32](#uint32) |  |  |
| int | [uint32](#uint32) |  |  |
| res | [uint32](#uint32) |  |  |
| leaderboard_score | [uint32](#uint32) |  |  |
| show_round | [string](#string) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Effect"></a>

### Sheet_Simulation_SimV2Effect



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| effect_id | [uint32](#uint32) |  |  |
| luk | [int32](#int32) |  |  |
| tec | [int32](#int32) |  |  |
| ins | [int32](#int32) |  |  |
| int | [int32](#int32) |  |  |
| res | [int32](#int32) |  |  |
| effect_title | [int32](#int32) |  |  |
| effect_desc | [int32](#int32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Event"></a>

### Sheet_Simulation_SimV2Event



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| event_group_id | [uint32](#uint32) |  |  |
| event_id | [uint32](#uint32) |  |  |
| event_title | [uint32](#uint32) |  |  |
| event_desc | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| cd_round | [uint32](#uint32) |  |  |
| trigger_rate | [uint32](#uint32) |  |  |
| trigger_sort | [uint32](#uint32) |  |  |
| trigger | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2Info"></a>

### Sheet_Simulation_SimV2Info



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| player_chara_id | [uint32](#uint32) |  |  |
| event_group_id | [uint32](#uint32) |  |  |
| train_result_fail | [uint32](#uint32) |  |  |
| train_result_normal | [uint32](#uint32) |  |  |
| train_result_great | [uint32](#uint32) |  |  |
| train_cap | [uint32](#uint32) |  |  |
| find_ting_adj | [uint32](#uint32) |  |  |
| shunweima_2 | [int32](#int32) |  |  |
| shunweima_3 | [int32](#int32) |  |  |
| shunweima_4 | [int32](#int32) |  |  |
| match_event_cd | [uint32](#uint32) |  |  |
| show_arrow_buff | [string](#string) |  |  |
| add_sub_buff | [string](#string) |  |  |
| attribute_add_buff | [string](#string) |  |  |
| arrow_amount_12001 | [uint32](#uint32) |  |  |
| arrow_amount_12002 | [uint32](#uint32) |  |  |
| arrow_amount_12004 | [uint32](#uint32) |  |  |
| arrow_amount_12005 | [uint32](#uint32) |  |  |
| arrow_amount_12014 | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Reward"></a>

### Sheet_Simulation_SimV2Reward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rank | [uint32](#uint32) |  |  |
| ability | [uint32](#uint32) |  |  |
| random_effect | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Roll"></a>

### Sheet_Simulation_SimV2Roll



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| event_group_id | [uint32](#uint32) |  |  |
| name | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Round"></a>

### Sheet_Simulation_SimV2Round



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| round_id | [uint32](#uint32) |  |  |
| round_type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Simulation_SimV2Selection"></a>

### Sheet_Simulation_SimV2Selection



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| event_id | [uint32](#uint32) |  |  |
| selection_id | [uint32](#uint32) |  |  |
| selection_desc | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| check | [string](#string) | repeated |  |
| args | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2SelectionResult"></a>

### Sheet_Simulation_SimV2SelectionResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| selection_id | [uint32](#uint32) |  |  |
| selection_result_id | [uint32](#uint32) |  |  |
| selection_result_type | [uint32](#uint32) |  |  |
| initial_weight | [uint32](#uint32) |  |  |
| luk | [int32](#int32) |  |  |
| tec | [int32](#int32) |  |  |
| ins | [int32](#int32) |  |  |
| int | [int32](#int32) |  |  |
| res | [int32](#int32) |  |  |
| effect | [uint32](#uint32) | repeated |  |
| buff | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2Story"></a>

### Sheet_Simulation_SimV2Story



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| story_id | [uint32](#uint32) |  |  |
| trigger_type | [uint32](#uint32) |  |  |
| weight | [uint32](#uint32) |  |  |
| str_id | [uint32](#uint32) |  |  |
| args | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2Trigger"></a>

### Sheet_Simulation_SimV2Trigger



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| trigger_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| param | [string](#string) | repeated |  |






<a name="lqc-Sheet_Simulation_SimV2Upgrade"></a>

### Sheet_Simulation_SimV2Upgrade



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| skill_point | [uint32](#uint32) |  |  |
| limit | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Spot_AudioSpot"></a>

### Sheet_Spot_AudioSpot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| path | [string](#string) |  |  |
| time_length | [float](#float) |  |  |
| str | [string](#string) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Spot_CharacterSpot"></a>

### Sheet_Spot_CharacterSpot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs2 | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_chs_t2 | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_jp2 | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| open | [uint32](#uint32) |  |  |
| init_skin | [uint32](#uint32) |  |  |
| full_fetter_skin | [uint32](#uint32) |  |  |
| hand | [uint32](#uint32) |  |  |
| favorite | [uint32](#uint32) |  |  |
| star_5_material | [string](#string) |  |  |
| star_5_cost | [uint32](#uint32) |  |  |
| can_marry | [uint32](#uint32) |  |  |
| exchange_item_id | [uint32](#uint32) |  |  |
| exchange_item_num | [int32](#int32) |  |  |
| emo | [string](#string) |  |  |
| sound | [uint32](#uint32) |  |  |
| sound_volume | [float](#float) |  |  |
| sex | [uint32](#uint32) |  |  |
| desc_stature_chs | [string](#string) |  |  |
| desc_stature_chs_t | [string](#string) |  |  |
| desc_stature_jp | [string](#string) |  |  |
| desc_stature_en | [string](#string) |  |  |
| desc_stature_kr | [string](#string) |  |  |
| desc_birth_chs | [string](#string) |  |  |
| desc_birth_chs_t | [string](#string) |  |  |
| desc_birth_jp | [string](#string) |  |  |
| desc_birth_en | [string](#string) |  |  |
| desc_birth_kr | [string](#string) |  |  |
| desc_age_chs | [string](#string) |  |  |
| desc_age_chs_t | [string](#string) |  |  |
| desc_age_jp | [string](#string) |  |  |
| desc_age_en | [string](#string) |  |  |
| desc_age_kr | [string](#string) |  |  |
| desc_bloodtype_chs | [string](#string) |  |  |
| desc_bloodtype_chs_t | [string](#string) |  |  |
| desc_bloodtype_jp | [string](#string) |  |  |
| desc_bloodtype_en | [string](#string) |  |  |
| desc_bloodtype_kr | [string](#string) |  |  |
| desc_cv_chs | [string](#string) |  |  |
| desc_cv_chs_t | [string](#string) |  |  |
| desc_cv_jp | [string](#string) |  |  |
| desc_cv_en | [string](#string) |  |  |
| desc_cv_kr | [string](#string) |  |  |
| desc_hobby_chs | [string](#string) |  |  |
| desc_hobby_chs_t | [string](#string) |  |  |
| desc_hobby_jp | [string](#string) |  |  |
| desc_hobby_en | [string](#string) |  |  |
| desc_hobby_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_item_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_item_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_item_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_item_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| desc_item_kr | [string](#string) |  |  |
| collaboration | [uint32](#uint32) |  |  |
| skin_lib | [uint32](#uint32) | repeated |  |
| ur | [uint32](#uint32) |  |  |
| ur_ron | [uint32](#uint32) |  |  |
| ur_liqi | [uint32](#uint32) |  |  |
| ur_cutin | [string](#string) |  |  |
| limited | [uint32](#uint32) |  |  |
| treasure_sp | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Spot_Event"></a>

### Sheet_Spot_Event



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| activity_id | [uint32](#uint32) |  |  |
| key_item_id | [uint32](#uint32) |  |  |
| key_amount | [uint32](#uint32) |  |  |
| unlock_task_id | [uint32](#uint32) |  |  |
| sort | [uint32](#uint32) |  |  |
| unlock_time | [string](#string) |  |  |
| content_path | [string](#string) |  |  |
| title_chs | [string](#string) |  |  |
| title_chs_t | [string](#string) |  |  |
| title_jp | [string](#string) |  |  |
| title_en | [string](#string) |  |  |
| title_kr | [string](#string) |  |  |
| subtitle_chs | [string](#string) |  |  |
| subtitle_chs_t | [string](#string) |  |  |
| subtitle_jp | [string](#string) |  |  |
| subtitle_en | [string](#string) |  |  |
| subtitle_kr | [string](#string) |  |  |
| content_chs | [string](#string) |  |  |
| content_chs_t | [string](#string) |  |  |
| content_jp | [string](#string) |  |  |
| content_en | [string](#string) |  |  |
| content_kr | [string](#string) |  |  |
| ending_id | [uint32](#uint32) | repeated |  |
| ending_res | [string](#string) |  |  |






<a name="lqc-Sheet_Spot_Rewards"></a>

### Sheet_Spot_Rewards



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| content_chs | [string](#string) |  |  |
| content_chs_t | [string](#string) |  |  |
| content_jp | [string](#string) |  |  |
| content_en | [string](#string) |  |  |
| content_kr | [string](#string) |  |  |
| reward | [string](#string) |  |  |






<a name="lqc-Sheet_Spot_SkinSpot"></a>

### Sheet_Spot_SkinSpot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| character_id | [uint32](#uint32) |  |  |
| lock_tips_chs | [string](#string) |  |  |
| lock_tips_chs_t | [string](#string) |  |  |
| lock_tips_jp | [string](#string) |  |  |
| lock_tips_en | [string](#string) |  |  |
| lock_tips_kr | [string](#string) |  |  |
| path | [string](#string) |  |  |
| exchange_item_id | [uint32](#uint32) |  |  |
| exchange_item_num | [int32](#int32) |  |  |
| direction | [uint32](#uint32) |  |  |
| no_reverse | [uint32](#uint32) |  |  |
| lock_reverse | [uint32](#uint32) |  |  |
| offset_x | [int32](#int32) |  |  |
| offset_y | [int32](#int32) |  |  |
| spot_scale | [string](#string) |  |  |
| effective_time | [string](#string) |  |  |
| lobby_offset | [string](#string) |  |  |
| liaoshe_offset | [string](#string) |  |  |
| shop_offset | [string](#string) |  |  |
| win_offset | [string](#string) |  |  |
| gameend_offset | [string](#string) |  |  |
| starup_offset | [string](#string) |  |  |
| treasure_offset | [string](#string) |  |  |
| ck_full_0_offset | [string](#string) |  |  |
| ck_full_1_offset | [string](#string) |  |  |
| ck_full_2_offset | [string](#string) |  |  |
| ck_full_3_offset | [string](#string) |  |  |
| ck_full_single_offset | [string](#string) |  |  |
| ck_half_0_offset | [string](#string) |  |  |
| ck_half_1_offset | [string](#string) |  |  |
| ck_half_2_offset | [string](#string) |  |  |
| ck_half_3_offset | [string](#string) |  |  |
| ck_half_single_offset | [string](#string) |  |  |
| smallhead_x | [int32](#int32) |  |  |
| smallhead_y | [int32](#int32) |  |  |
| smallhead_width | [int32](#int32) |  |  |
| full_x | [int32](#int32) |  |  |
| full_y | [int32](#int32) |  |  |
| full_width | [int32](#int32) |  |  |
| full_height | [int32](#int32) |  |  |
| half_x | [int32](#int32) |  |  |
| half_y | [int32](#int32) |  |  |
| half_width | [int32](#int32) |  |  |
| half_height | [int32](#int32) |  |  |
| spine_type | [int32](#int32) |  |  |
| spine_width | [int32](#int32) |  |  |
| spine_height | [int32](#int32) |  |  |
| pivot_x | [int32](#int32) |  |  |
| pivot_y | [int32](#int32) |  |  |
| idle | [string](#string) |  |  |
| greeting | [int32](#int32) |  |  |
| celebrate | [int32](#int32) |  |  |
| click | [int32](#int32) |  |  |
| greeting_init | [int32](#int32) |  |  |
| click2 | [int32](#int32) |  |  |
| celebrate_idle | [int32](#int32) |  |  |
| illust_data | [string](#string) |  |  |






<a name="lqc-Sheet_Spot_Spot"></a>

### Sheet_Spot_Spot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| unique_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| level_limit | [uint32](#uint32) |  |  |
| is_married | [uint32](#uint32) |  |  |
| lock_tips_chs | [string](#string) |  |  |
| lock_tips_chs_t | [string](#string) |  |  |
| lock_tips_jp | [string](#string) |  |  |
| lock_tips_en | [string](#string) |  |  |
| lock_tips_kr | [string](#string) |  |  |
| queque | [uint32](#uint32) |  |  |
| content_chs | [string](#string) |  |  |
| content_chs_t | [string](#string) |  |  |
| content_jp | [string](#string) |  |  |
| content_en | [string](#string) |  |  |
| content_kr | [string](#string) |  |  |
| content_path | [string](#string) |  |  |
| jieju | [uint32](#uint32) | repeated |  |






<a name="lqc-Sheet_Str_Event"></a>

### Sheet_Str_Event



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |
| chs | [string](#string) |  |  |
| chs_t | [string](#string) |  |  |
| jp | [string](#string) |  |  |
| en | [string](#string) |  |  |
| kr | [string](#string) |  |  |






<a name="lqc-Sheet_Str_Str"></a>

### Sheet_Str_Str



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |
| chs | [string](#string) |  |  |
| chs_t | [string](#string) |  |  |
| jp | [string](#string) |  |  |
| en | [string](#string) |  |  |
| kr | [string](#string) |  |  |






<a name="lqc-Sheet_Tournament_Tournaments"></a>

### Sheet_Tournament_Tournaments



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| game_ticket_id | [uint32](#uint32) |  |  |






<a name="lqc-Sheet_Tutorial_Init"></a>

### Sheet_Tutorial_Init



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| episode_id | [uint32](#uint32) |  |  |
| dora | [string](#string) |  |  |
| rival | [string](#string) |  |  |
| init_score | [string](#string) |  |  |
| paihe | [string](#string) |  |  |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| benchang | [uint32](#uint32) |  |  |
| first_position | [uint32](#uint32) |  |  |
| view_position | [uint32](#uint32) |  |  |
| start_shoupai | [string](#string) |  |  |
| start_ming | [string](#string) |  |  |
| end_shoupai | [string](#string) |  |  |
| end_ming | [string](#string) |  |  |
| end_yaku | [string](#string) |  |  |
| ura_dora | [string](#string) |  |  |
| end_fu | [uint32](#uint32) |  |  |
| hu_score | [uint32](#uint32) |  |  |
| flow_score | [string](#string) |  |  |






<a name="lqc-Sheet_Tutorial_Step"></a>

### Sheet_Tutorial_Step



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| episode_id | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |
| seat | [uint32](#uint32) |  |  |
| act_type | [uint32](#uint32) |  |  |
| act_param | [string](#string) |  |  |
| tingpai_param | [string](#string) |  |  |
| is_zhenting | [uint32](#uint32) |  |  |
| str_type | [uint32](#uint32) |  |  |
| str_id | [uint32](#uint32) |  |  |
| view_ui_hand | [uint32](#uint32) |  |  |
| pic_path | [string](#string) |  |  |
| button_show | [string](#string) |  |  |
| button_pai | [string](#string) |  |  |
| player_act | [uint32](#uint32) |  |  |
| player_param | [string](#string) |  |  |






<a name="lqc-Sheet_Vip_Vip"></a>

### Sheet_Vip_Vip



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| img | [string](#string) |  |  |
| desc_chs | [string](#string) |  |  |
| desc_chs_t | [string](#string) |  |  |
| desc_jp | [string](#string) |  |  |
| desc_en | [string](#string) |  |  |
| desc_kr | [string](#string) |  |  |
| charge | [uint32](#uint32) |  |  |
| gift_limit | [uint32](#uint32) |  |  |
| friend_added | [uint32](#uint32) |  |  |
| shop_free_refresh | [uint32](#uint32) |  |  |
| shop_refresh_limit | [uint32](#uint32) |  |  |
| buddy_bonus | [uint32](#uint32) |  |  |
| favourite_limit | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |
| rewards | [string](#string) | repeated |  |






<a name="lqc-Sheet_Voice_Event"></a>

### Sheet_Voice_Event



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| words_chs | [string](#string) |  |  |
| words_chs_t | [string](#string) |  |  |
| words_jp | [string](#string) |  |  |
| words_en | [string](#string) |  |  |
| words_kr | [string](#string) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |
| stage | [uint32](#uint32) |  |  |
| time_length | [float](#float) |  |  |
| path | [string](#string) |  |  |
| volume_fix | [float](#float) |  |  |






<a name="lqc-Sheet_Voice_Sound"></a>

### Sheet_Voice_Sound



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| name_chs | [string](#string) |  |  |
| name_chs_t | [string](#string) |  |  |
| name_jp | [string](#string) |  |  |
| name_en | [string](#string) |  |  |
| name_kr | [string](#string) |  |  |
| words_chs | [string](#string) |  |  |
| words_chs_t | [string](#string) |  |  |
| words_jp | [string](#string) |  |  |
| words_en | [string](#string) |  |  |
| words_kr | [string](#string) |  |  |
| category | [uint32](#uint32) |  |  |
| type | [string](#string) |  |  |
| level_limit | [uint32](#uint32) |  |  |
| bond_limit | [uint32](#uint32) |  |  |
| time_length | [float](#float) |  |  |
| path | [string](#string) |  |  |
| hide | [uint32](#uint32) |  |  |
| date_limit | [string](#string) |  |  |






<a name="lqc-Sheet_Voice_Spot"></a>

### Sheet_Voice_Spot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| character | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| path | [string](#string) |  |  |
| type_desc | [string](#string) |  |  |















<a name="liqi_struct-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## liqi_struct.proto



<a name="lq-ActionAnGangAddGang"></a>

### ActionAnGangAddGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| tiles | [string](#string) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| doras | [string](#string) | repeated |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |






<a name="lq-ActionBaBei"></a>

### ActionBaBei



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| doras | [string](#string) | repeated |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| moqie | [bool](#bool) |  |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |






<a name="lq-ActionChangeTile"></a>

### ActionChangeTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| in_tiles | [string](#string) | repeated |  |
| in_tile_states | [int32](#int32) | repeated |  |
| out_tiles | [string](#string) | repeated |  |
| out_tile_states | [int32](#int32) | repeated |  |
| doras | [string](#string) | repeated |  |
| tingpais0 | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| change_type | [uint32](#uint32) |  |  |






<a name="lq-ActionChiPengGang"></a>

### ActionChiPengGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| froms | [uint32](#uint32) | repeated |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tile_states | [uint32](#uint32) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-ActionDealTile"></a>

### ActionDealTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| left_tile_count | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| doras | [string](#string) | repeated |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| tile_index | [uint32](#uint32) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-ActionDiscardTile"></a>

### ActionDiscardTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| is_liqi | [bool](#bool) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| moqie | [bool](#bool) |  |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| doras | [string](#string) | repeated |  |
| is_wliqi | [bool](#bool) |  |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| revealed | [bool](#bool) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |
| liqi_type_beishuizhizhan | [uint32](#uint32) |  |  |






<a name="lq-ActionFillAwaitingTiles"></a>

### ActionFillAwaitingTiles



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| awaiting_tiles | [string](#string) | repeated |  |
| left_tile_count | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |






<a name="lq-ActionGangResult"></a>

### ActionGangResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gang_infos | [ChuanmaGang](#lq-ChuanmaGang) |  |  |






<a name="lq-ActionGangResultEnd"></a>

### ActionGangResultEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gang_infos | [ChuanmaGang](#lq-ChuanmaGang) |  |  |






<a name="lq-ActionHule"></a>

### ActionHule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuleInfo](#lq-HuleInfo) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| wait_timeout | [uint32](#uint32) |  |  |
| scores | [int32](#int32) | repeated |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| baopai | [int32](#int32) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-ActionHuleXueZhanEnd"></a>

### ActionHuleXueZhanEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuInfoXueZhanMid](#lq-HuInfoXueZhanMid) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| scores | [int32](#int32) | repeated |  |
| wait_timeout | [uint32](#uint32) |  |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-ActionHuleXueZhanMid"></a>

### ActionHuleXueZhanMid



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuInfoXueZhanMid](#lq-HuInfoXueZhanMid) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| scores | [int32](#int32) | repeated |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| zhenting | [bool](#bool) |  |  |






<a name="lq-ActionLiuJu"></a>

### ActionLiuJu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| seat | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| allplayertiles | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-ActionLockTile"></a>

### ActionLockTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| zhenting | [bool](#bool) |  |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| doras | [string](#string) | repeated |  |
| lock_state | [int32](#int32) |  |  |






<a name="lq-ActionMJStart"></a>

### ActionMJStart







<a name="lq-ActionNewCard"></a>

### ActionNewCard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field_spell | [uint32](#uint32) |  |  |






<a name="lq-ActionNewRound"></a>

### ActionNewRound



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| dora | [string](#string) |  |  |
| scores | [int32](#int32) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| liqibang | [uint32](#uint32) |  |  |
| tingpais0 | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| al | [bool](#bool) |  |  |
| md5 | [string](#string) |  |  |
| left_tile_count | [uint32](#uint32) |  |  |
| doras | [string](#string) | repeated |  |
| opens | [NewRoundOpenedTiles](#lq-NewRoundOpenedTiles) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| ju_count | [uint32](#uint32) |  |  |
| field_spell | [uint32](#uint32) |  |  |
| sha256 | [string](#string) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| saltSha256 | [string](#string) |  |  |
| xia_ke_shang | [XiaKeShangInfo](#lq-XiaKeShangInfo) |  |  |






<a name="lq-ActionNoTile"></a>

### ActionNoTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| liujumanguan | [bool](#bool) |  |  |
| players | [NoTilePlayerInfo](#lq-NoTilePlayerInfo) | repeated |  |
| scores | [NoTileScoreInfo](#lq-NoTileScoreInfo) | repeated |  |
| gameend | [bool](#bool) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-ActionPrototype"></a>

### ActionPrototype



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| step | [uint32](#uint32) |  |  |
| name | [string](#string) |  |  |
| data | [bytes](#bytes) |  |  |






<a name="lq-ActionRevealTile"></a>

### ActionRevealTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| is_liqi | [bool](#bool) |  |  |
| is_wliqi | [bool](#bool) |  |  |
| moqie | [bool](#bool) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| tile | [string](#string) |  |  |
| zhenting | [bool](#bool) |  |  |






<a name="lq-ActionSelectGap"></a>

### ActionSelectGap



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gap_types | [uint32](#uint32) | repeated |  |
| tingpais0 | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-ActionSubmit"></a>

### ActionSubmit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| submits | [SubmitInfo](#lq-SubmitInfo) | repeated |  |






<a name="lq-ActionTake"></a>

### ActionTake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| takes | [TakeInfo](#lq-TakeInfo) | repeated |  |
| tingpais0 | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-ActionUnveilTile"></a>

### ActionUnveilTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [int32](#int32) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-ChuanmaGang"></a>

### ChuanmaGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| scores | [int32](#int32) | repeated |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-FanInfo"></a>

### FanInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](#string) |  |  |
| val | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-GameAction"></a>

### GameAction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| passed | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| result | [bytes](#bytes) |  |  |
| user_input | [GameUserInput](#lq-GameUserInput) |  |  |
| user_event | [GameUserEvent](#lq-GameUserEvent) |  |  |
| game_event | [uint32](#uint32) |  |  |






<a name="lq-GameChiPengGang"></a>

### GameChiPengGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| index | [uint32](#uint32) |  |  |
| cancel_operation | [bool](#bool) |  |  |
| timeuse | [uint32](#uint32) |  |  |






<a name="lq-GameDetailRecords"></a>

### GameDetailRecords



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| records | [bytes](#bytes) | repeated |  |
| version | [uint32](#uint32) |  |  |
| actions | [GameAction](#lq-GameAction) | repeated |  |
| bar | [bytes](#bytes) |  |  |






<a name="lq-GameEnd"></a>

### GameEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scores | [int32](#int32) | repeated |  |






<a name="lq-GameSelfOperation"></a>

### GameSelfOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| index | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| cancel_operation | [bool](#bool) |  |  |
| moqie | [bool](#bool) |  |  |
| timeuse | [uint32](#uint32) |  |  |
| tile_state | [int32](#int32) |  |  |
| change_tiles | [string](#string) | repeated |  |
| tile_states | [int32](#int32) | repeated |  |
| gap_type | [uint32](#uint32) |  |  |
| auto_operation | [bool](#bool) |  |  |






<a name="lq-GameSnapshot"></a>

### GameSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| index_player | [uint32](#uint32) |  |  |
| left_tile_count | [uint32](#uint32) |  |  |
| hands | [string](#string) | repeated |  |
| doras | [string](#string) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| players | [GameSnapshot.PlayerSnapshot](#lq-GameSnapshot-PlayerSnapshot) | repeated |  |
| zhenting | [bool](#bool) |  |  |






<a name="lq-GameSnapshot-PlayerSnapshot"></a>

### GameSnapshot.PlayerSnapshot



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| score | [int32](#int32) |  |  |
| liqiposition | [int32](#int32) |  |  |
| tilenum | [uint32](#uint32) |  |  |
| qipais | [string](#string) | repeated |  |
| mings | [GameSnapshot.PlayerSnapshot.Fulu](#lq-GameSnapshot-PlayerSnapshot-Fulu) | repeated |  |






<a name="lq-GameSnapshot-PlayerSnapshot-Fulu"></a>

### GameSnapshot.PlayerSnapshot.Fulu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| tile | [string](#string) | repeated |  |
| from | [uint32](#uint32) | repeated |  |






<a name="lq-GameUserEvent"></a>

### GameUserEvent



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-GameUserInput"></a>

### GameUserInput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| emo | [uint32](#uint32) |  |  |
| operation | [GameSelfOperation](#lq-GameSelfOperation) |  |  |
| cpg | [GameChiPengGang](#lq-GameChiPengGang) |  |  |
| vote | [GameVoteGameEnd](#lq-GameVoteGameEnd) |  |  |






<a name="lq-GameVoteGameEnd"></a>

### GameVoteGameEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| yes | [bool](#bool) |  |  |






<a name="lq-HuInfoXueZhanMid"></a>

### HuInfoXueZhanMid



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| hand_count | [uint32](#uint32) |  |  |
| hand | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| hu_tile | [string](#string) |  |  |
| zimo | [bool](#bool) |  |  |
| yiman | [bool](#bool) |  |  |
| count | [uint32](#uint32) |  |  |
| fans | [FanInfo](#lq-FanInfo) | repeated |  |
| fu | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |






<a name="lq-HuleInfo"></a>

### HuleInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hand | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| hu_tile | [string](#string) |  |  |
| seat | [uint32](#uint32) |  |  |
| zimo | [bool](#bool) |  |  |
| qinjia | [bool](#bool) |  |  |
| liqi | [bool](#bool) |  |  |
| doras | [string](#string) | repeated |  |
| li_doras | [string](#string) | repeated |  |
| yiman | [bool](#bool) |  |  |
| count | [uint32](#uint32) |  |  |
| fans | [FanInfo](#lq-FanInfo) | repeated |  |
| fu | [uint32](#uint32) |  |  |
| title | [string](#string) |  |  |
| point_rong | [uint32](#uint32) |  |  |
| point_zimo_qin | [uint32](#uint32) |  |  |
| point_zimo_xian | [uint32](#uint32) |  |  |
| title_id | [uint32](#uint32) |  |  |
| point_sum | [uint32](#uint32) |  |  |
| dadian | [uint32](#uint32) |  |  |
| baopai | [uint32](#uint32) |  |  |
| baopai_seats | [uint32](#uint32) | repeated |  |
| lines | [string](#string) | repeated |  |
| tianming_bonus | [uint32](#uint32) |  |  |
| baida_changed | [string](#string) | repeated |  |
| hu_tile_baiDa_changed | [string](#string) |  |  |
| xia_ke_shang_coefficient | [uint32](#uint32) |  |  |






<a name="lq-HunZhiYiJiBuffInfo"></a>

### HunZhiYiJiBuffInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| continue_deal_count | [uint32](#uint32) |  |  |
| overload | [bool](#bool) |  |  |






<a name="lq-LiQiSuccess"></a>

### LiQiSuccess



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| score | [int32](#int32) |  |  |
| liqibang | [uint32](#uint32) |  |  |
| failed | [bool](#bool) |  |  |
| liqi_type_beishuizhizhan | [uint32](#uint32) |  |  |
| xia_ke_shang | [XiaKeShangInfo](#lq-XiaKeShangInfo) |  |  |






<a name="lq-MuyuInfo"></a>

### MuyuInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| count_max | [uint32](#uint32) |  |  |
| id | [uint32](#uint32) |  |  |






<a name="lq-NewRoundOpenedTiles"></a>

### NewRoundOpenedTiles



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| count | [uint32](#uint32) | repeated |  |






<a name="lq-NoTilePlayerInfo"></a>

### NoTilePlayerInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tingpai | [bool](#bool) |  |  |
| hand | [string](#string) | repeated |  |
| tings | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| already_hule | [bool](#bool) |  |  |






<a name="lq-NoTileScoreInfo"></a>

### NoTileScoreInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| hand | [string](#string) | repeated |  |
| ming | [string](#string) | repeated |  |
| doras | [string](#string) | repeated |  |
| score | [uint32](#uint32) |  |  |
| taxes | [int32](#int32) | repeated |  |
| lines | [string](#string) | repeated |  |






<a name="lq-OptionalOperation"></a>

### OptionalOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| combination | [string](#string) | repeated |  |
| change_tiles | [string](#string) | repeated |  |
| change_tile_states | [int32](#int32) | repeated |  |
| gap_type | [uint32](#uint32) |  |  |






<a name="lq-OptionalOperationList"></a>

### OptionalOperationList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| operation_list | [OptionalOperation](#lq-OptionalOperation) | repeated |  |
| time_add | [uint32](#uint32) |  |  |
| time_fixed | [uint32](#uint32) |  |  |






<a name="lq-PlayerLeaving"></a>

### PlayerLeaving



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |






<a name="lq-RecordAnGangAddGang"></a>

### RecordAnGangAddGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| tiles | [string](#string) |  |  |
| doras | [string](#string) | repeated |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |






<a name="lq-RecordBaBei"></a>

### RecordBaBei



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| doras | [string](#string) | repeated |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| moqie | [bool](#bool) |  |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |






<a name="lq-RecordChangeTile"></a>

### RecordChangeTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| doras | [string](#string) | repeated |  |
| tingpai | [RecordChangeTile.TingPai](#lq-RecordChangeTile-TingPai) | repeated |  |
| change_tile_infos | [RecordChangeTile.ChangeTile](#lq-RecordChangeTile-ChangeTile) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| change_type | [uint32](#uint32) |  |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |






<a name="lq-RecordChangeTile-ChangeTile"></a>

### RecordChangeTile.ChangeTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| in_tiles | [string](#string) | repeated |  |
| in_tile_states | [int32](#int32) | repeated |  |
| out_tiles | [string](#string) | repeated |  |
| out_tile_states | [int32](#int32) | repeated |  |






<a name="lq-RecordChangeTile-TingPai"></a>

### RecordChangeTile.TingPai



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |






<a name="lq-RecordChiPengGang"></a>

### RecordChiPengGang



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| froms | [uint32](#uint32) | repeated |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| zhenting | [bool](#bool) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| tile_states | [uint32](#uint32) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-RecordDealTile"></a>

### RecordDealTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| left_tile_count | [uint32](#uint32) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| doras | [string](#string) | repeated |  |
| zhenting | [bool](#bool) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| tile_index | [uint32](#uint32) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-RecordDiscardTile"></a>

### RecordDiscardTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| is_liqi | [bool](#bool) |  |  |
| moqie | [bool](#bool) |  |  |
| zhenting | [bool](#bool) | repeated |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| doras | [string](#string) | repeated |  |
| is_wliqi | [bool](#bool) |  |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| tile_state | [uint32](#uint32) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |
| liqi_type_beishuizhizhan | [uint32](#uint32) |  |  |






<a name="lq-RecordFillAwaitingTiles"></a>

### RecordFillAwaitingTiles



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| awaiting_tiles | [string](#string) | repeated |  |
| left_tile_count | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |






<a name="lq-RecordGangResult"></a>

### RecordGangResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gang_infos | [ChuanmaGang](#lq-ChuanmaGang) |  |  |






<a name="lq-RecordGangResultEnd"></a>

### RecordGangResultEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gang_infos | [ChuanmaGang](#lq-ChuanmaGang) |  |  |






<a name="lq-RecordHule"></a>

### RecordHule



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuleInfo](#lq-HuleInfo) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| wait_timeout | [uint32](#uint32) |  |  |
| scores | [int32](#int32) | repeated |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| baopai | [int32](#int32) |  |  |
| hun_zhi_yi_ji_info | [HunZhiYiJiBuffInfo](#lq-HunZhiYiJiBuffInfo) |  |  |






<a name="lq-RecordHuleXueZhanEnd"></a>

### RecordHuleXueZhanEnd



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuInfoXueZhanMid](#lq-HuInfoXueZhanMid) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| scores | [int32](#int32) | repeated |  |
| wait_timeout | [uint32](#uint32) |  |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-RecordHuleXueZhanMid"></a>

### RecordHuleXueZhanMid



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hules | [HuInfoXueZhanMid](#lq-HuInfoXueZhanMid) | repeated |  |
| old_scores | [int32](#int32) | repeated |  |
| delta_scores | [int32](#int32) | repeated |  |
| scores | [int32](#int32) | repeated |  |
| doras | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| zhenting | [bool](#bool) | repeated |  |






<a name="lq-RecordLiuJu"></a>

### RecordLiuJu



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| gameend | [GameEnd](#lq-GameEnd) |  |  |
| seat | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |
| liqi | [LiQiSuccess](#lq-LiQiSuccess) |  |  |
| allplayertiles | [string](#string) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-RecordLockTile"></a>

### RecordLockTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| tile | [string](#string) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| zhentings | [bool](#bool) | repeated |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| doras | [string](#string) | repeated |  |
| lock_state | [int32](#int32) |  |  |






<a name="lq-RecordNewCard"></a>

### RecordNewCard



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field_spell | [uint32](#uint32) |  |  |






<a name="lq-RecordNewRound"></a>

### RecordNewRound



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chang | [uint32](#uint32) |  |  |
| ju | [uint32](#uint32) |  |  |
| ben | [uint32](#uint32) |  |  |
| dora | [string](#string) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| tiles0 | [string](#string) | repeated |  |
| tiles1 | [string](#string) | repeated |  |
| tiles2 | [string](#string) | repeated |  |
| tiles3 | [string](#string) | repeated |  |
| tingpai | [RecordNewRound.TingPai](#lq-RecordNewRound-TingPai) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |
| md5 | [string](#string) |  |  |
| paishan | [string](#string) |  |  |
| left_tile_count | [uint32](#uint32) |  |  |
| doras | [string](#string) | repeated |  |
| opens | [NewRoundOpenedTiles](#lq-NewRoundOpenedTiles) | repeated |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| ju_count | [uint32](#uint32) |  |  |
| field_spell | [uint32](#uint32) |  |  |
| sha256 | [string](#string) |  |  |
| yongchang | [YongchangInfo](#lq-YongchangInfo) |  |  |
| saltSha256 | [string](#string) |  |  |
| salt | [string](#string) |  |  |
| xia_ke_shang | [XiaKeShangInfo](#lq-XiaKeShangInfo) |  |  |






<a name="lq-RecordNewRound-TingPai"></a>

### RecordNewRound.TingPai



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |






<a name="lq-RecordNoTile"></a>

### RecordNoTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| liujumanguan | [bool](#bool) |  |  |
| players | [NoTilePlayerInfo](#lq-NoTilePlayerInfo) | repeated |  |
| scores | [NoTileScoreInfo](#lq-NoTileScoreInfo) | repeated |  |
| gameend | [bool](#bool) |  |  |
| muyu | [MuyuInfo](#lq-MuyuInfo) |  |  |
| hules_history | [HuleInfo](#lq-HuleInfo) | repeated |  |






<a name="lq-RecordRevealTile"></a>

### RecordRevealTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| is_liqi | [bool](#bool) |  |  |
| is_wliqi | [bool](#bool) |  |  |
| moqie | [bool](#bool) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| operations | [OptionalOperationList](#lq-OptionalOperationList) | repeated |  |
| tingpais | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |
| tile | [string](#string) |  |  |
| zhenting | [bool](#bool) | repeated |  |






<a name="lq-RecordSelectGap"></a>

### RecordSelectGap



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gap_types | [uint32](#uint32) | repeated |  |
| tingpai | [RecordSelectGap.TingPai](#lq-RecordSelectGap-TingPai) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-RecordSelectGap-TingPai"></a>

### RecordSelectGap.TingPai



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |






<a name="lq-RecordSubmit"></a>

### RecordSubmit



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| submits | [SubmitInfo](#lq-SubmitInfo) | repeated |  |






<a name="lq-RecordTake"></a>

### RecordTake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| takes | [TakeInfo](#lq-TakeInfo) | repeated |  |
| tingpais0 | [TingPaiDiscardInfo](#lq-TingPaiDiscardInfo) | repeated |  |
| tingpai | [RecordTake.TingPai](#lq-RecordTake-TingPai) | repeated |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-RecordTake-TingPai"></a>

### RecordTake.TingPai



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| tingpais1 | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |






<a name="lq-RecordUnveilTile"></a>

### RecordUnveilTile



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [int32](#int32) |  |  |
| scores | [int32](#int32) | repeated |  |
| liqibang | [uint32](#uint32) |  |  |
| operation | [OptionalOperationList](#lq-OptionalOperationList) |  |  |






<a name="lq-SubmitGroup"></a>

### SubmitGroup



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |






<a name="lq-SubmitInfo"></a>

### SubmitInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| submit_seat | [uint32](#uint32) |  |  |
| groups | [SubmitGroup](#lq-SubmitGroup) | repeated |  |






<a name="lq-TakeInfo"></a>

### TakeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| take_seat | [uint32](#uint32) |  |  |
| from_seat | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| tiles | [string](#string) | repeated |  |






<a name="lq-TingPaiDiscardInfo"></a>

### TingPaiDiscardInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| zhenting | [bool](#bool) |  |  |
| infos | [TingPaiInfo](#lq-TingPaiInfo) | repeated |  |






<a name="lq-TingPaiInfo"></a>

### TingPaiInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| tile | [string](#string) |  |  |
| haveyi | [bool](#bool) |  |  |
| yiman | [bool](#bool) |  |  |
| count | [uint32](#uint32) |  |  |
| fu | [uint32](#uint32) |  |  |
| biao_dora_count | [uint32](#uint32) |  |  |
| yiman_zimo | [bool](#bool) |  |  |
| count_zimo | [uint32](#uint32) |  |  |
| fu_zimo | [uint32](#uint32) |  |  |






<a name="lq-XiaKeShangInfo"></a>

### XiaKeShangInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| score_coefficients | [uint32](#uint32) | repeated |  |






<a name="lq-YongchangInfo"></a>

### YongchangInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seat | [uint32](#uint32) |  |  |
| moqie_count | [uint32](#uint32) |  |  |
| moqie_bonus | [uint32](#uint32) |  |  |
| shouqie_count | [uint32](#uint32) |  |  |
| shouqie_bonus | [uint32](#uint32) |  |  |















<a name="notify_lobby-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## notify_lobby.proto



<a name="lq-NotifyAFKResult"></a>

### NotifyAFKResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [uint32](#uint32) |  |  |
| ban_end_time | [uint32](#uint32) |  |  |
| game_uuid | [string](#string) |  |  |






<a name="lq-NotifyAccountChallengeTaskUpdate"></a>

### NotifyAccountChallengeTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| level | [uint32](#uint32) |  |  |
| refresh_count | [uint32](#uint32) |  |  |
| match_count | [uint32](#uint32) |  |  |
| ticket_id | [uint32](#uint32) |  |  |
| rewarded_season | [uint32](#uint32) | repeated |  |






<a name="lq-NotifyAccountLogout"></a>

### NotifyAccountLogout







<a name="lq-NotifyAccountRandomTaskUpdate"></a>

### NotifyAccountRandomTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |






<a name="lq-NotifyAccountUpdate"></a>

### NotifyAccountUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| update | [AccountUpdate](#lq-AccountUpdate) |  |  |






<a name="lq-NotifyActivityChange"></a>

### NotifyActivityChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| new_activities | [Activity](#lq-Activity) | repeated |  |
| end_activities | [uint32](#uint32) | repeated |  |






<a name="lq-NotifyActivityPeriodTaskUpdate"></a>

### NotifyActivityPeriodTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |






<a name="lq-NotifyActivityPointV2"></a>

### NotifyActivityPointV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_points | [NotifyActivityPointV2.ActivityPoint](#lq-NotifyActivityPointV2-ActivityPoint) | repeated |  |






<a name="lq-NotifyActivityPointV2-ActivityPoint"></a>

### NotifyActivityPointV2.ActivityPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-NotifyActivityRewardV2"></a>

### NotifyActivityRewardV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_reward | [NotifyActivityRewardV2.ActivityReward](#lq-NotifyActivityRewardV2-ActivityReward) | repeated |  |






<a name="lq-NotifyActivityRewardV2-ActivityReward"></a>

### NotifyActivityRewardV2.ActivityReward



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-NotifyActivitySegmentTaskUpdate"></a>

### NotifyActivitySegmentTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [SegmentTaskProgress](#lq-SegmentTaskProgress) | repeated |  |






<a name="lq-NotifyActivityTaskUpdate"></a>

### NotifyActivityTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |






<a name="lq-NotifyActivityUpdate"></a>

### NotifyActivityUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| list | [NotifyActivityUpdate.FeedActivityData](#lq-NotifyActivityUpdate-FeedActivityData) | repeated |  |






<a name="lq-NotifyActivityUpdate-FeedActivityData"></a>

### NotifyActivityUpdate.FeedActivityData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activity_id | [uint32](#uint32) |  |  |
| feed_count | [uint32](#uint32) |  |  |
| friend_receive_data | [NotifyActivityUpdate.FeedActivityData.CountWithTimeData](#lq-NotifyActivityUpdate-FeedActivityData-CountWithTimeData) |  |  |
| friend_send_data | [NotifyActivityUpdate.FeedActivityData.CountWithTimeData](#lq-NotifyActivityUpdate-FeedActivityData-CountWithTimeData) |  |  |
| gift_inbox | [NotifyActivityUpdate.FeedActivityData.GiftBoxData](#lq-NotifyActivityUpdate-FeedActivityData-GiftBoxData) | repeated |  |






<a name="lq-NotifyActivityUpdate-FeedActivityData-CountWithTimeData"></a>

### NotifyActivityUpdate.FeedActivityData.CountWithTimeData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |
| last_update_time | [uint32](#uint32) |  |  |






<a name="lq-NotifyActivityUpdate-FeedActivityData-GiftBoxData"></a>

### NotifyActivityUpdate.FeedActivityData.GiftBoxData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| item_id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| from_account_id | [uint32](#uint32) |  |  |
| time | [uint32](#uint32) |  |  |
| received | [uint32](#uint32) |  |  |






<a name="lq-NotifyAnnouncementUpdate"></a>

### NotifyAnnouncementUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| update_list | [NotifyAnnouncementUpdate.AnnouncementUpdate](#lq-NotifyAnnouncementUpdate-AnnouncementUpdate) | repeated |  |






<a name="lq-NotifyAnnouncementUpdate-AnnouncementUpdate"></a>

### NotifyAnnouncementUpdate.AnnouncementUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| lang | [string](#string) |  |  |
| platform | [string](#string) |  |  |






<a name="lq-NotifyAnotherLogin"></a>

### NotifyAnotherLogin







<a name="lq-NotifyClientMessage"></a>

### NotifyClientMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sender | [PlayerBaseView](#lq-PlayerBaseView) |  |  |
| type | [uint32](#uint32) |  |  |
| content | [string](#string) |  |  |






<a name="lq-NotifyConnectionShutdown"></a>

### NotifyConnectionShutdown



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| reason | [uint32](#uint32) |  |  |
| close_at | [uint32](#uint32) |  |  |






<a name="lq-NotifyCustomContestAccountMsg"></a>

### NotifyCustomContestAccountMsg



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| account_id | [uint32](#uint32) |  |  |
| sender | [string](#string) |  |  |
| content | [string](#string) |  |  |
| verified | [uint32](#uint32) |  |  |






<a name="lq-NotifyCustomContestState"></a>

### NotifyCustomContestState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| state | [uint32](#uint32) |  |  |






<a name="lq-NotifyCustomContestSystemMsg"></a>

### NotifyCustomContestSystemMsg



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |
| game_start | [CustomizedContestGameStart](#lq-CustomizedContestGameStart) |  |  |
| game_end | [CustomizedContestGameEnd](#lq-CustomizedContestGameEnd) |  |  |






<a name="lq-NotifyCustomizedContestPlanCancel"></a>

### NotifyCustomizedContestPlanCancel



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| uuid | [string](#string) |  |  |






<a name="lq-NotifyCustomizedContestPlanReady"></a>

### NotifyCustomizedContestPlanReady



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_plan | [CustomizedContestGamePlan](#lq-CustomizedContestGamePlan) |  |  |






<a name="lq-NotifyCustomizedContestReady"></a>

### NotifyCustomizedContestReady



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| ready | [uint32](#uint32) |  |  |
| reason | [uint32](#uint32) |  |  |






<a name="lq-NotifyCustomizedContestRuleModify"></a>

### NotifyCustomizedContestRuleModify



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| unique_id | [uint32](#uint32) |  |  |
| auto_match | [uint32](#uint32) |  |  |






<a name="lq-NotifyDailyTaskUpdate"></a>

### NotifyDailyTaskUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| progresses | [TaskProgress](#lq-TaskProgress) | repeated |  |
| max_daily_task_count | [uint32](#uint32) |  |  |
| refresh_count | [uint32](#uint32) |  |  |






<a name="lq-NotifyDeleteMail"></a>

### NotifyDeleteMail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail_id_list | [uint32](#uint32) | repeated |  |






<a name="lq-NotifyFriendChange"></a>

### NotifyFriendChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| type | [uint32](#uint32) |  |  |
| friend | [Friend](#lq-Friend) |  |  |






<a name="lq-NotifyFriendStateChange"></a>

### NotifyFriendStateChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| active_state | [AccountActiveState](#lq-AccountActiveState) |  |  |






<a name="lq-NotifyFriendViewChange"></a>

### NotifyFriendViewChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_id | [uint32](#uint32) |  |  |
| base | [PlayerBaseView](#lq-PlayerBaseView) |  |  |






<a name="lq-NotifyGameFinishRewardV2"></a>

### NotifyGameFinishRewardV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mode_id | [uint32](#uint32) |  |  |
| level_change | [NotifyGameFinishRewardV2.LevelChange](#lq-NotifyGameFinishRewardV2-LevelChange) |  |  |
| match_chest | [NotifyGameFinishRewardV2.MatchChest](#lq-NotifyGameFinishRewardV2-MatchChest) |  |  |
| main_character | [NotifyGameFinishRewardV2.MainCharacter](#lq-NotifyGameFinishRewardV2-MainCharacter) |  |  |
| character_gift | [NotifyGameFinishRewardV2.CharacterGift](#lq-NotifyGameFinishRewardV2-CharacterGift) |  |  |
| badges | [BadgeAchieveProgress](#lq-BadgeAchieveProgress) | repeated |  |






<a name="lq-NotifyGameFinishRewardV2-CharacterGift"></a>

### NotifyGameFinishRewardV2.CharacterGift



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |
| add | [uint32](#uint32) |  |  |
| is_graded | [bool](#bool) |  |  |






<a name="lq-NotifyGameFinishRewardV2-LevelChange"></a>

### NotifyGameFinishRewardV2.LevelChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| origin | [AccountLevel](#lq-AccountLevel) |  |  |
| final | [AccountLevel](#lq-AccountLevel) |  |  |
| type | [uint32](#uint32) |  |  |






<a name="lq-NotifyGameFinishRewardV2-MainCharacter"></a>

### NotifyGameFinishRewardV2.MainCharacter



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| level | [uint32](#uint32) |  |  |
| exp | [uint32](#uint32) |  |  |
| add | [uint32](#uint32) |  |  |






<a name="lq-NotifyGameFinishRewardV2-MatchChest"></a>

### NotifyGameFinishRewardV2.MatchChest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chest_id | [uint32](#uint32) |  |  |
| origin | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |
| is_graded | [bool](#bool) |  |  |
| rewards | [RewardSlot](#lq-RewardSlot) | repeated |  |






<a name="lq-NotifyGiftSendRefresh"></a>

### NotifyGiftSendRefresh







<a name="lq-NotifyIntervalUpdate"></a>

### NotifyIntervalUpdate







<a name="lq-NotifyLeaderboardPointV2"></a>

### NotifyLeaderboardPointV2



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_points | [NotifyLeaderboardPointV2.LeaderboardPoint](#lq-NotifyLeaderboardPointV2-LeaderboardPoint) | repeated |  |






<a name="lq-NotifyLeaderboardPointV2-LeaderboardPoint"></a>

### NotifyLeaderboardPointV2.LeaderboardPoint



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| leaderboard_id | [uint32](#uint32) |  |  |
| point | [uint32](#uint32) |  |  |






<a name="lq-NotifyLoginQueueFinished"></a>

### NotifyLoginQueueFinished







<a name="lq-NotifyMaintainNotice"></a>

### NotifyMaintainNotice







<a name="lq-NotifyMatchFailed"></a>

### NotifyMatchFailed



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sid | [string](#string) |  |  |






<a name="lq-NotifyMatchGameStart"></a>

### NotifyMatchGameStart



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_url | [string](#string) |  |  |
| connect_token | [string](#string) |  |  |
| game_uuid | [string](#string) |  |  |
| match_mode_id | [uint32](#uint32) |  |  |
| location | [string](#string) |  |  |






<a name="lq-NotifyMatchTimeout"></a>

### NotifyMatchTimeout



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sid | [string](#string) |  |  |






<a name="lq-NotifyNewComment"></a>

### NotifyNewComment







<a name="lq-NotifyNewFriendApply"></a>

### NotifyNewFriendApply



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| apply_time | [uint32](#uint32) |  |  |
| removed_id | [uint32](#uint32) |  |  |






<a name="lq-NotifyNewMail"></a>

### NotifyNewMail



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mail | [Mail](#lq-Mail) |  |  |






<a name="lq-NotifyPayResult"></a>

### NotifyPayResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pay_result | [uint32](#uint32) |  |  |
| order_id | [string](#string) |  |  |
| goods_id | [uint32](#uint32) |  |  |
| new_month_ticket | [uint32](#uint32) |  |  |
| resource_modify | [NotifyPayResult.ResourceModify](#lq-NotifyPayResult-ResourceModify) | repeated |  |






<a name="lq-NotifyPayResult-ResourceModify"></a>

### NotifyPayResult.ResourceModify



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [uint32](#uint32) |  |  |
| count | [uint32](#uint32) |  |  |
| final | [uint32](#uint32) |  |  |






<a name="lq-NotifyReviveCoinUpdate"></a>

### NotifyReviveCoinUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| has_gained | [bool](#bool) |  |  |






<a name="lq-NotifyRollingNotice"></a>

### NotifyRollingNotice







<a name="lq-NotifyRoomGameStart"></a>

### NotifyRoomGameStart



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| game_url | [string](#string) |  |  |
| connect_token | [string](#string) |  |  |
| game_uuid | [string](#string) |  |  |
| location | [string](#string) |  |  |






<a name="lq-NotifyRoomKickOut"></a>

### NotifyRoomKickOut







<a name="lq-NotifyRoomPlayerDressing"></a>

### NotifyRoomPlayerDressing



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| dressing | [bool](#bool) |  |  |
| account_list | [NotifyRoomPlayerDressing.AccountDressingState](#lq-NotifyRoomPlayerDressing-AccountDressingState) |  |  |
| seq | [uint32](#uint32) |  |  |






<a name="lq-NotifyRoomPlayerDressing-AccountDressingState"></a>

### NotifyRoomPlayerDressing.AccountDressingState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| dressing | [bool](#bool) |  |  |






<a name="lq-NotifyRoomPlayerReady"></a>

### NotifyRoomPlayerReady



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| ready | [bool](#bool) |  |  |
| account_list | [NotifyRoomPlayerReady.AccountReadyState](#lq-NotifyRoomPlayerReady-AccountReadyState) |  |  |
| seq | [uint32](#uint32) |  |  |






<a name="lq-NotifyRoomPlayerReady-AccountReadyState"></a>

### NotifyRoomPlayerReady.AccountReadyState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| account_id | [uint32](#uint32) |  |  |
| ready | [bool](#bool) |  |  |






<a name="lq-NotifyRoomPlayerUpdate"></a>

### NotifyRoomPlayerUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| owner_id | [uint32](#uint32) |  |  |
| robot_count | [uint32](#uint32) |  |  |
| player_list | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| seq | [uint32](#uint32) |  |  |
| robots | [PlayerGameView](#lq-PlayerGameView) | repeated |  |
| positions | [uint32](#uint32) | repeated |  |






<a name="lq-NotifySeerReport"></a>

### NotifySeerReport



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| report | [SeerBrief](#lq-SeerBrief) |  |  |






<a name="lq-NotifyServerSetting"></a>

### NotifyServerSetting



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| settings | [ServerSettings](#lq-ServerSettings) |  |  |






<a name="lq-NotifyShopUpdate"></a>

### NotifyShopUpdate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| shop_info | [ShopInfo](#lq-ShopInfo) |  |  |






<a name="lq-NotifyVipLevelChange"></a>

### NotifyVipLevelChange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gift_limit | [uint32](#uint32) |  |  |
| friend_max_count | [uint32](#uint32) |  |  |
| zhp_free_refresh_limit | [uint32](#uint32) |  |  |
| zhp_cost_refresh_limit | [uint32](#uint32) |  |  |
| buddy_bonus | [float](#float) |  |  |
| record_collect_limit | [uint32](#uint32) |  |  |















<a name="services-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## services.proto









<a name="lq-FastTest"></a>

### FastTest


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| authGame | [ReqAuthGame](#lq-ReqAuthGame) | [ResAuthGame](#lq-ResAuthGame) |  |
| authObserve | [ReqAuthObserve](#lq-ReqAuthObserve) | [ResCommon](#lq-ResCommon) |  |
| broadcastInGame | [ReqBroadcastInGame](#lq-ReqBroadcastInGame) | [ResCommon](#lq-ResCommon) |  |
| checkNetworkDelay | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| clearLeaving | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| confirmNewRound | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| enterGame | [ReqCommon](#lq-ReqCommon) | [ResEnterGame](#lq-ResEnterGame) |  |
| fetchGamePlayerState | [ReqCommon](#lq-ReqCommon) | [ResGamePlayerState](#lq-ResGamePlayerState) |  |
| finishSyncGame | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| inputChiPengGang | [ReqChiPengGang](#lq-ReqChiPengGang) | [ResCommon](#lq-ResCommon) |  |
| inputGameGMCommand | [ReqGMCommandInGaming](#lq-ReqGMCommandInGaming) | [ResCommon](#lq-ResCommon) |  |
| inputOperation | [ReqSelfOperation](#lq-ReqSelfOperation) | [ResCommon](#lq-ResCommon) |  |
| startObserve | [ReqCommon](#lq-ReqCommon) | [ResStartObserve](#lq-ResStartObserve) |  |
| stopObserve | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| syncGame | [ReqSyncGame](#lq-ReqSyncGame) | [ResSyncGame](#lq-ResSyncGame) |  |
| terminateGame | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| voteGameEnd | [ReqVoteGameEnd](#lq-ReqVoteGameEnd) | [ResGameEndVote](#lq-ResGameEndVote) |  |


<a name="lq-Lobby"></a>

### Lobby


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| addCollectedGameRecord | [ReqAddCollectedGameRecord](#lq-ReqAddCollectedGameRecord) | [ResAddCollectedGameRecord](#lq-ResAddCollectedGameRecord) |  |
| addFinishedEnding | [ReqFinishedEnding](#lq-ReqFinishedEnding) | [ResCommon](#lq-ResCommon) |  |
| addRoomRobot | [ReqAddRoomRobot](#lq-ReqAddRoomRobot) | [ResCommon](#lq-ResCommon) |  |
| amuletActivityFetchBrief | [ReqAmuletActivityFetchBrief](#lq-ReqAmuletActivityFetchBrief) | [ResAmuletActivityFetchBrief](#lq-ResAmuletActivityFetchBrief) |  |
| amuletActivityGameOperate | [ReqAmuletActivityGameOperate](#lq-ReqAmuletActivityGameOperate) | [ResAmuletEventResponse](#lq-ResAmuletEventResponse) |  |
| amuletActivityGiveup | [ReqAmuletActivityGiveup](#lq-ReqAmuletActivityGiveup) | [ResCommon](#lq-ResCommon) |  |
| amuletActivityMaintainInfo | [ReqCommon](#lq-ReqCommon) | [ResAmuletActivityMaintainInfo](#lq-ResAmuletActivityMaintainInfo) |  |
| amuletActivityOperate | [ReqAmuletActivityOperate](#lq-ReqAmuletActivityOperate) | [ResAmuletEventResponse](#lq-ResAmuletEventResponse) |  |
| amuletActivitySelectBookEffect | [ReqAmuletActivitySelectBookEffect](#lq-ReqAmuletActivitySelectBookEffect) | [ResCommon](#lq-ResCommon) |  |
| amuletActivitySetSkillLevel | [ReqAmuletActivitySetSkillLevel](#lq-ReqAmuletActivitySetSkillLevel) | [ResCommon](#lq-ResCommon) |  |
| amuletActivityStartGame | [ReqAmuletActivityStartGame](#lq-ReqAmuletActivityStartGame) | [ResAmuletEventResponse](#lq-ResAmuletEventResponse) |  |
| applyFriend | [ReqApplyFriend](#lq-ReqApplyFriend) | [ResCommon](#lq-ResCommon) |  |
| bindAccount | [ReqBindAccount](#lq-ReqBindAccount) | [ResCommon](#lq-ResCommon) |  |
| bindEmail | [ReqBindEmail](#lq-ReqBindEmail) | [ResCommon](#lq-ResCommon) |  |
| bindOauth2 | [ReqBindOauth2](#lq-ReqBindOauth2) | [ResCommon](#lq-ResCommon) |  |
| bindPhoneNumber | [ReqBindPhoneNumber](#lq-ReqBindPhoneNumber) | [ResCommon](#lq-ResCommon) |  |
| bingoActivityReceiveReward | [ReqBingoActivityReceiveReward](#lq-ReqBingoActivityReceiveReward) | [ResBingoActivityReceiveReward](#lq-ResBingoActivityReceiveReward) |  |
| buyArenaTicket | [ReqBuyArenaTicket](#lq-ReqBuyArenaTicket) | [ResCommon](#lq-ResCommon) |  |
| buyFestivalProposal | [ReqBuyFestivalProposal](#lq-ReqBuyFestivalProposal) | [ResBuyFestivalProposal](#lq-ResBuyFestivalProposal) |  |
| buyFromChestShop | [ReqBuyFromChestShop](#lq-ReqBuyFromChestShop) | [ResBuyFromChestShop](#lq-ResBuyFromChestShop) |  |
| buyFromShop | [ReqBuyFromShop](#lq-ReqBuyFromShop) | [ResBuyFromShop](#lq-ResBuyFromShop) |  |
| buyFromZHP | [ReqBuyFromZHP](#lq-ReqBuyFromZHP) | [ResCommon](#lq-ResCommon) |  |
| buyInABMatch | [ReqBuyInABMatch](#lq-ReqBuyInABMatch) | [ResCommon](#lq-ResCommon) |  |
| buyShiLian | [ReqBuyShiLian](#lq-ReqBuyShiLian) | [ResCommon](#lq-ResCommon) |  |
| cancelDeleteAccount | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| cancelGooglePlayOrder | [ReqCancelGooglePlayOrder](#lq-ReqCancelGooglePlayOrder) | [ResCommon](#lq-ResCommon) |  |
| cancelMatch | [ReqCancelMatchQueue](#lq-ReqCancelMatchQueue) | [ResCommon](#lq-ResCommon) |  |
| cancelQueue | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| cancelUnifiedMatch | [ReqCancelUnifiedMatch](#lq-ReqCancelUnifiedMatch) | [ResCommon](#lq-ResCommon) |  |
| changeAvatar | [ReqChangeAvatar](#lq-ReqChangeAvatar) | [ResCommon](#lq-ResCommon) |  |
| changeCharacterSkin | [ReqChangeCharacterSkin](#lq-ReqChangeCharacterSkin) | [ResCommon](#lq-ResCommon) |  |
| changeCharacterView | [ReqChangeCharacterView](#lq-ReqChangeCharacterView) | [ResCommon](#lq-ResCommon) |  |
| changeCollectedGameRecordRemarks | [ReqChangeCollectedGameRecordRemarks](#lq-ReqChangeCollectedGameRecordRemarks) | [ResChangeCollectedGameRecordRemarks](#lq-ResChangeCollectedGameRecordRemarks) |  |
| changeCommonView | [ReqChangeCommonView](#lq-ReqChangeCommonView) | [ResCommon](#lq-ResCommon) |  |
| changeMainCharacter | [ReqChangeMainCharacter](#lq-ReqChangeMainCharacter) | [ResCommon](#lq-ResCommon) |  |
| checkPrivacy | [ReqCheckPrivacy](#lq-ReqCheckPrivacy) | [ResCommon](#lq-ResCommon) |  |
| clientMessage | [ReqClientMessage](#lq-ReqClientMessage) | [ResCommon](#lq-ResCommon) |  |
| combiningRecycleCraft | [ReqCombiningRecycleCraft](#lq-ReqCombiningRecycleCraft) | [ResCombiningRecycleCraft](#lq-ResCombiningRecycleCraft) |  |
| completeActivityFlipTask | [ReqCompleteActivityTask](#lq-ReqCompleteActivityTask) | [ResCommon](#lq-ResCommon) |  |
| completeActivityFlipTaskBatch | [ReqCompleteActivityFlipTaskBatch](#lq-ReqCompleteActivityFlipTaskBatch) | [ResCompleteActivityFlipTaskBatch](#lq-ResCompleteActivityFlipTaskBatch) |  |
| completeActivityTask | [ReqCompleteActivityTask](#lq-ReqCompleteActivityTask) | [ResCommon](#lq-ResCommon) |  |
| completeActivityTaskBatch | [ReqCompleteActivityTaskBatch](#lq-ReqCompleteActivityTaskBatch) | [ResCommon](#lq-ResCommon) |  |
| completePeriodActivityTask | [ReqCompleteActivityTask](#lq-ReqCompleteActivityTask) | [ResCommon](#lq-ResCommon) |  |
| completePeriodActivityTaskBatch | [ReqCompletePeriodActivityTaskBatch](#lq-ReqCompletePeriodActivityTaskBatch) | [ResCommon](#lq-ResCommon) |  |
| completeRandomActivityTask | [ReqCompleteActivityTask](#lq-ReqCompleteActivityTask) | [ResCommon](#lq-ResCommon) |  |
| completeRandomActivityTaskBatch | [ReqCompleteActivityTaskBatch](#lq-ReqCompleteActivityTaskBatch) | [ResCommon](#lq-ResCommon) |  |
| completeSegmentTaskReward | [ReqCompleteSegmentTaskReward](#lq-ReqCompleteSegmentTaskReward) | [ResCompleteSegmentTaskReward](#lq-ResCompleteSegmentTaskReward) |  |
| completeVillageTask | [ReqCompleteVillageTask](#lq-ReqCompleteVillageTask) | [ResCompleteVillageTask](#lq-ResCompleteVillageTask) |  |
| composeShard | [ReqComposeShard](#lq-ReqComposeShard) | [ResCommon](#lq-ResCommon) |  |
| createAlipayAppOrder | [ReqCreateAlipayAppOrder](#lq-ReqCreateAlipayAppOrder) | [ResCreateAlipayAppOrder](#lq-ResCreateAlipayAppOrder) |  |
| createAlipayOrder | [ReqCreateAlipayOrder](#lq-ReqCreateAlipayOrder) | [ResCreateAlipayOrder](#lq-ResCreateAlipayOrder) |  |
| createAlipayScanOrder | [ReqCreateAlipayScanOrder](#lq-ReqCreateAlipayScanOrder) | [ResCreateAlipayScanOrder](#lq-ResCreateAlipayScanOrder) |  |
| createBillingOrder | [ReqCreateBillingOrder](#lq-ReqCreateBillingOrder) | [ResCreateBillingOrder](#lq-ResCreateBillingOrder) |  |
| createCustomizedContest | [ReqCreateCustomizedContest](#lq-ReqCreateCustomizedContest) | [ResCreateCustomizedContest](#lq-ResCreateCustomizedContest) |  |
| createDMMOrder | [ReqCreateDMMOrder](#lq-ReqCreateDMMOrder) | [ResCreateDmmOrder](#lq-ResCreateDmmOrder) |  |
| createENAlipayOrder | [ReqCreateENAlipayOrder](#lq-ReqCreateENAlipayOrder) | [ResCreateENAlipayOrder](#lq-ResCreateENAlipayOrder) |  |
| createENJCBOrder | [ReqCreateENJCBOrder](#lq-ReqCreateENJCBOrder) | [ResCreateENJCBOrder](#lq-ResCreateENJCBOrder) |  |
| createENMasterCardOrder | [ReqCreateENMasterCardOrder](#lq-ReqCreateENMasterCardOrder) | [ResCreateENMasterCardOrder](#lq-ResCreateENMasterCardOrder) |  |
| createENPaypalOrder | [ReqCreateENPaypalOrder](#lq-ReqCreateENPaypalOrder) | [ResCreateENPaypalOrder](#lq-ResCreateENPaypalOrder) |  |
| createENVisaOrder | [ReqCreateENVisaOrder](#lq-ReqCreateENVisaOrder) | [ResCreateENVisaOrder](#lq-ResCreateENVisaOrder) |  |
| createEmailVerifyCode | [ReqCreateEmailVerifyCode](#lq-ReqCreateEmailVerifyCode) | [ResCommon](#lq-ResCommon) |  |
| createGameObserveAuth | [ReqCreateGameObserveAuth](#lq-ReqCreateGameObserveAuth) | [ResCreateGameObserveAuth](#lq-ResCreateGameObserveAuth) |  |
| createGamePlan | [ReqCreateGamePlan](#lq-ReqCreateGamePlan) | [ResCommon](#lq-ResCommon) |  |
| createIAPOrder | [ReqCreateIAPOrder](#lq-ReqCreateIAPOrder) | [ResCreateIAPOrder](#lq-ResCreateIAPOrder) |  |
| createJPAuOrder | [ReqCreateJPAuOrder](#lq-ReqCreateJPAuOrder) | [ResCreateJPAuOrder](#lq-ResCreateJPAuOrder) |  |
| createJPCreditCardOrder | [ReqCreateJPCreditCardOrder](#lq-ReqCreateJPCreditCardOrder) | [ResCreateJPCreditCardOrder](#lq-ResCreateJPCreditCardOrder) |  |
| createJPDocomoOrder | [ReqCreateJPDocomoOrder](#lq-ReqCreateJPDocomoOrder) | [ResCreateJPDocomoOrder](#lq-ResCreateJPDocomoOrder) |  |
| createJPGMOOrder | [ReqCreateJPGMOOrder](#lq-ReqCreateJPGMOOrder) | [ResCreateJPGMOOrder](#lq-ResCreateJPGMOOrder) |  |
| createJPPayPayOrder | [ReqCreateJPPayPayOrder](#lq-ReqCreateJPPayPayOrder) | [ResCreateJPPayPayOrder](#lq-ResCreateJPPayPayOrder) |  |
| createJPPaypalOrder | [ReqCreateJPPaypalOrder](#lq-ReqCreateJPPaypalOrder) | [ResCreateJPPaypalOrder](#lq-ResCreateJPPaypalOrder) |  |
| createJPSoftbankOrder | [ReqCreateJPSoftbankOrder](#lq-ReqCreateJPSoftbankOrder) | [ResCreateJPSoftbankOrder](#lq-ResCreateJPSoftbankOrder) |  |
| createJPWebMoneyOrder | [ReqCreateJPWebMoneyOrder](#lq-ReqCreateJPWebMoneyOrder) | [ResCreateJPWebMoneyOrder](#lq-ResCreateJPWebMoneyOrder) |  |
| createKRAlipayOrder | [ReqCreateKRAlipayOrder](#lq-ReqCreateKRAlipayOrder) | [ResCreateKRAlipayOrder](#lq-ResCreateKRAlipayOrder) |  |
| createKRJCBOrder | [ReqCreateKRJCBOrder](#lq-ReqCreateKRJCBOrder) | [ResCreateKRJCBOrder](#lq-ResCreateKRJCBOrder) |  |
| createKRMasterCardOrder | [ReqCreateKRMasterCardOrder](#lq-ReqCreateKRMasterCardOrder) | [ResCreateKRMasterCardOrder](#lq-ResCreateKRMasterCardOrder) |  |
| createKRPaypalOrder | [ReqCreateKRPaypalOrder](#lq-ReqCreateKRPaypalOrder) | [ResCreateKRPaypalOrder](#lq-ResCreateKRPaypalOrder) |  |
| createKRVisaOrder | [ReqCreateKRVisaOrder](#lq-ReqCreateKRVisaOrder) | [ResCreateKRVisaOrder](#lq-ResCreateKRVisaOrder) |  |
| createMyCardAndroidOrder | [ReqCreateMyCardOrder](#lq-ReqCreateMyCardOrder) | [ResCreateMyCardOrder](#lq-ResCreateMyCardOrder) |  |
| createMyCardWebOrder | [ReqCreateMyCardOrder](#lq-ReqCreateMyCardOrder) | [ResCreateMyCardOrder](#lq-ResCreateMyCardOrder) |  |
| createNickname | [ReqCreateNickname](#lq-ReqCreateNickname) | [ResCommon](#lq-ResCommon) |  |
| createPaypalOrder | [ReqCreatePaypalOrder](#lq-ReqCreatePaypalOrder) | [ResCreatePaypalOrder](#lq-ResCreatePaypalOrder) |  |
| createPhoneLoginBind | [ReqCreatePhoneLoginBind](#lq-ReqCreatePhoneLoginBind) | [ResCommon](#lq-ResCommon) |  |
| createPhoneVerifyCode | [ReqCreatePhoneVerifyCode](#lq-ReqCreatePhoneVerifyCode) | [ResCommon](#lq-ResCommon) |  |
| createRoom | [ReqCreateRoom](#lq-ReqCreateRoom) | [ResCreateRoom](#lq-ResCreateRoom) |  |
| createSeerReport | [ReqCreateSeerReport](#lq-ReqCreateSeerReport) | [ResCreateSeerReport](#lq-ResCreateSeerReport) |  |
| createSteamOrder | [ReqCreateSteamOrder](#lq-ReqCreateSteamOrder) | [ResCreateSteamOrder](#lq-ResCreateSteamOrder) |  |
| createWechatAppOrder | [ReqCreateWechatAppOrder](#lq-ReqCreateWechatAppOrder) | [ResCreateWechatAppOrder](#lq-ResCreateWechatAppOrder) |  |
| createWechatNativeOrder | [ReqCreateWechatNativeOrder](#lq-ReqCreateWechatNativeOrder) | [ResCreateWechatNativeOrder](#lq-ResCreateWechatNativeOrder) |  |
| createXsollaOrder | [ReqCreateXsollaOrder](#lq-ReqCreateXsollaOrder) | [ResCreateXsollaOrder](#lq-ResCreateXsollaOrder) |  |
| createXsollaV4Order | [ReqCreateXsollaOrder](#lq-ReqCreateXsollaOrder) | [ResCreateXsollaOrder](#lq-ResCreateXsollaOrder) |  |
| createYostarSDKOrder | [ReqCreateYostarOrder](#lq-ReqCreateYostarOrder) | [ResCreateYostarOrder](#lq-ResCreateYostarOrder) |  |
| createYostarV4SDKOrder | [ReqCreateYostarV4SDKOrder](#lq-ReqCreateYostarV4SDKOrder) | [ResCreateYostarV4SDKOrder](#lq-ResCreateYostarV4SDKOrder) |  |
| deleteAccount | [ReqCommon](#lq-ReqCommon) | [ResDeleteAccount](#lq-ResDeleteAccount) |  |
| deleteComment | [ReqDeleteComment](#lq-ReqDeleteComment) | [ResCommon](#lq-ResCommon) |  |
| deleteMail | [ReqDeleteMail](#lq-ReqDeleteMail) | [ResCommon](#lq-ResCommon) |  |
| deliverAA32Order | [ReqDeliverAA32Order](#lq-ReqDeliverAA32Order) | [ResCommon](#lq-ResCommon) |  |
| digMine | [ReqDigMine](#lq-ReqDigMine) | [ResDigMine](#lq-ResDigMine) |  |
| dmmPreLogin | [ReqDMMPreLogin](#lq-ReqDMMPreLogin) | [ResDMMPreLogin](#lq-ResDMMPreLogin) |  |
| doActivitySignIn | [ReqDoActivitySignIn](#lq-ReqDoActivitySignIn) | [ResDoActivitySignIn](#lq-ResDoActivitySignIn) |  |
| doDailySignIn | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| dressingStatus | [ReqRoomDressing](#lq-ReqRoomDressing) | [ResCommon](#lq-ResCommon) |  |
| emailLogin | [ReqEmailLogin](#lq-ReqEmailLogin) | [ResLogin](#lq-ResLogin) |  |
| enterArena | [ReqEnterArena](#lq-ReqEnterArena) | [ResCommon](#lq-ResCommon) |  |
| enterCustomizedContest | [ReqEnterCustomizedContest](#lq-ReqEnterCustomizedContest) | [ResEnterCustomizedContest](#lq-ResEnterCustomizedContest) |  |
| exchangeActivityItem | [ReqExchangeActivityItem](#lq-ReqExchangeActivityItem) | [ResExchangeActivityItem](#lq-ResExchangeActivityItem) |  |
| exchangeChestStone | [ReqExchangeCurrency](#lq-ReqExchangeCurrency) | [ResCommon](#lq-ResCommon) |  |
| exchangeCurrency | [ReqExchangeCurrency](#lq-ReqExchangeCurrency) | [ResCommon](#lq-ResCommon) |  |
| exchangeDiamond | [ReqExchangeCurrency](#lq-ReqExchangeCurrency) | [ResCommon](#lq-ResCommon) |  |
| fastLogin | [ReqFastLogin](#lq-ReqFastLogin) | [ResFastLogin](#lq-ResFastLogin) |  |
| feedActivityFeed | [ReqFeedActivityFeed](#lq-ReqFeedActivityFeed) | [ResFeedActivityFeed](#lq-ResFeedActivityFeed) |  |
| fetchABMatchInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchABMatch](#lq-ResFetchABMatch) |  |
| fetchAccountActivityData | [ReqCommon](#lq-ReqCommon) | [ResAccountActivityData](#lq-ResAccountActivityData) |  |
| fetchAccountChallengeRankInfo | [ReqAccountInfo](#lq-ReqAccountInfo) | [ResAccountChallengeRankInfo](#lq-ResAccountChallengeRankInfo) |  |
| fetchAccountCharacterInfo | [ReqCommon](#lq-ReqCommon) | [ResAccountCharacterInfo](#lq-ResAccountCharacterInfo) |  |
| fetchAccountGameHuRecords | [ReqFetchAccountGameHuRecords](#lq-ReqFetchAccountGameHuRecords) | [ResFetchAccountGameHuRecords](#lq-ResFetchAccountGameHuRecords) |  |
| fetchAccountInfo | [ReqAccountInfo](#lq-ReqAccountInfo) | [ResAccountInfo](#lq-ResAccountInfo) |  |
| fetchAccountInfoExtra | [ReqFetchAccountInfoExtra](#lq-ReqFetchAccountInfoExtra) | [ResFetchAccountInfoExtra](#lq-ResFetchAccountInfoExtra) |  |
| fetchAccountSettings | [ReqCommon](#lq-ReqCommon) | [ResAccountSettings](#lq-ResAccountSettings) |  |
| fetchAccountState | [ReqAccountList](#lq-ReqAccountList) | [ResAccountStates](#lq-ResAccountStates) |  |
| fetchAccountStatisticInfo | [ReqAccountStatisticInfo](#lq-ReqAccountStatisticInfo) | [ResAccountStatisticInfo](#lq-ResAccountStatisticInfo) |  |
| fetchAchievement | [ReqCommon](#lq-ReqCommon) | [ResAchievement](#lq-ResAchievement) |  |
| fetchAchievementRate | [ReqCommon](#lq-ReqCommon) | [ResFetchAchievementRate](#lq-ResFetchAchievementRate) |  |
| fetchActivityBuff | [ReqCommon](#lq-ReqCommon) | [ResActivityBuff](#lq-ResActivityBuff) |  |
| fetchActivityFlipInfo | [ReqFetchActivityFlipInfo](#lq-ReqFetchActivityFlipInfo) | [ResFetchActivityFlipInfo](#lq-ResFetchActivityFlipInfo) |  |
| fetchActivityInterval | [ReqCommon](#lq-ReqCommon) | [ResFetchActivityInterval](#lq-ResFetchActivityInterval) |  |
| fetchActivityList | [ReqCommon](#lq-ReqCommon) | [ResActivityList](#lq-ResActivityList) |  |
| fetchActivityRank | [ReqFetchActivityRank](#lq-ReqFetchActivityRank) | [ResFetchActivityRank](#lq-ResFetchActivityRank) |  |
| fetchAllCommonViews | [ReqCommon](#lq-ReqCommon) | [ResAllcommonViews](#lq-ResAllcommonViews) |  |
| fetchAmuletActivityData | [ReqFetchAmuletActivityData](#lq-ReqFetchAmuletActivityData) | [ResFetchAmuletActivityData](#lq-ResFetchAmuletActivityData) |  |
| fetchAnnouncement | [ReqFetchAnnouncement](#lq-ReqFetchAnnouncement) | [ResAnnouncement](#lq-ResAnnouncement) |  |
| fetchAnnualReportInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchAnnualReportInfo](#lq-ResFetchAnnualReportInfo) |  |
| fetchBagInfo | [ReqCommon](#lq-ReqCommon) | [ResBagInfo](#lq-ResBagInfo) |  |
| fetchBannerActivityData | [ReqFetchBannerActivityData](#lq-ReqFetchBannerActivityData) | [ResFetchBannerActivityData](#lq-ResFetchBannerActivityData) |  |
| fetchBingoActivityData | [ReqFetchBingoActivityData](#lq-ReqFetchBingoActivityData) | [ResFetchBingoActivityData](#lq-ResFetchBingoActivityData) |  |
| fetchChallengeInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchChallengeInfo](#lq-ResFetchChallengeInfo) |  |
| fetchChallengeLeaderboard | [ReqChallangeLeaderboard](#lq-ReqChallangeLeaderboard) | [ResChallengeLeaderboard](#lq-ResChallengeLeaderboard) |  |
| fetchChallengeSeason | [ReqCommon](#lq-ReqCommon) | [ResChallengeSeasonInfo](#lq-ResChallengeSeasonInfo) |  |
| fetchCharacterInfo | [ReqCommon](#lq-ReqCommon) | [ResCharacterInfo](#lq-ResCharacterInfo) |  |
| fetchClientValue | [ReqCommon](#lq-ReqCommon) | [ResClientValue](#lq-ResClientValue) |  |
| fetchCollectedGameRecordList | [ReqCommon](#lq-ReqCommon) | [ResCollectedGameRecordList](#lq-ResCollectedGameRecordList) |  |
| fetchCommentContent | [ReqFetchCommentContent](#lq-ReqFetchCommentContent) | [ResFetchCommentContent](#lq-ResFetchCommentContent) |  |
| fetchCommentList | [ReqFetchCommentList](#lq-ReqFetchCommentList) | [ResFetchCommentList](#lq-ResFetchCommentList) |  |
| fetchCommentSetting | [ReqCommon](#lq-ReqCommon) | [ResCommentSetting](#lq-ResCommentSetting) |  |
| fetchCommonView | [ReqCommon](#lq-ReqCommon) | [ResCommonView](#lq-ResCommonView) |  |
| fetchCommonViews | [ReqCommonViews](#lq-ReqCommonViews) | [ResCommonViews](#lq-ResCommonViews) |  |
| fetchConnectionInfo | [ReqCommon](#lq-ReqCommon) | [ResConnectionInfo](#lq-ResConnectionInfo) |  |
| fetchContestPlayerRank | [ReqFetchContestPlayerRank](#lq-ReqFetchContestPlayerRank) | [ResFetchContestPlayerRank](#lq-ResFetchContestPlayerRank) |  |
| fetchContestTeamMember | [ReqFetchContestTeamMember](#lq-ReqFetchContestTeamMember) | [ResFetchContestTeamMember](#lq-ResFetchContestTeamMember) |  |
| fetchContestTeamPlayerRank | [ReqFetchContestTeamPlayerRank](#lq-ReqFetchContestTeamPlayerRank) | [ResFetchContestPlayerRank](#lq-ResFetchContestPlayerRank) |  |
| fetchContestTeamRank | [ReqFetchContestTeamRank](#lq-ReqFetchContestTeamRank) | [ResFetchContestTeamRank](#lq-ResFetchContestTeamRank) |  |
| fetchCurrentMatchInfo | [ReqCurrentMatchInfo](#lq-ReqCurrentMatchInfo) | [ResCurrentMatchInfo](#lq-ResCurrentMatchInfo) |  |
| fetchCustomizedContestAuthInfo | [ReqFetchCustomizedContestAuthInfo](#lq-ReqFetchCustomizedContestAuthInfo) | [ResFetchCustomizedContestAuthInfo](#lq-ResFetchCustomizedContestAuthInfo) |  |
| fetchCustomizedContestByContestId | [ReqFetchCustomizedContestByContestId](#lq-ReqFetchCustomizedContestByContestId) | [ResFetchCustomizedContestByContestId](#lq-ResFetchCustomizedContestByContestId) |  |
| fetchCustomizedContestGameLiveList | [ReqFetchCustomizedContestGameLiveList](#lq-ReqFetchCustomizedContestGameLiveList) | [ResFetchCustomizedContestGameLiveList](#lq-ResFetchCustomizedContestGameLiveList) |  |
| fetchCustomizedContestGameRecords | [ReqFetchCustomizedContestGameRecords](#lq-ReqFetchCustomizedContestGameRecords) | [ResFetchCustomizedContestGameRecords](#lq-ResFetchCustomizedContestGameRecords) |  |
| fetchCustomizedContestList | [ReqFetchCustomizedContestList](#lq-ReqFetchCustomizedContestList) | [ResFetchCustomizedContestList](#lq-ResFetchCustomizedContestList) |  |
| fetchCustomizedContestOnlineInfo | [ReqFetchCustomizedContestOnlineInfo](#lq-ReqFetchCustomizedContestOnlineInfo) | [ResFetchCustomizedContestOnlineInfo](#lq-ResFetchCustomizedContestOnlineInfo) |  |
| fetchDailySignActivityData | [ReqFetchDailySignActivityData](#lq-ReqFetchDailySignActivityData) | [ResFetchDailySignActivityData](#lq-ResFetchDailySignActivityData) |  |
| fetchDailySignInInfo | [ReqCommon](#lq-ReqCommon) | [ResDailySignInInfo](#lq-ResDailySignInInfo) |  |
| fetchDailyTask | [ReqCommon](#lq-ReqCommon) | [ResDailyTask](#lq-ResDailyTask) |  |
| fetchFriendApplyList | [ReqCommon](#lq-ReqCommon) | [ResFriendApplyList](#lq-ResFriendApplyList) |  |
| fetchFriendGiftActivityData | [ReqFetchFriendGiftActivityData](#lq-ReqFetchFriendGiftActivityData) | [ResFetchFriendGiftActivityData](#lq-ResFetchFriendGiftActivityData) |  |
| fetchFriendList | [ReqCommon](#lq-ReqCommon) | [ResFriendList](#lq-ResFriendList) |  |
| fetchGameLiveInfo | [ReqGameLiveInfo](#lq-ReqGameLiveInfo) | [ResGameLiveInfo](#lq-ResGameLiveInfo) |  |
| fetchGameLiveLeftSegment | [ReqGameLiveLeftSegment](#lq-ReqGameLiveLeftSegment) | [ResGameLiveLeftSegment](#lq-ResGameLiveLeftSegment) |  |
| fetchGameLiveList | [ReqGameLiveList](#lq-ReqGameLiveList) | [ResGameLiveList](#lq-ResGameLiveList) |  |
| fetchGamePointRank | [ReqGamePointRank](#lq-ReqGamePointRank) | [ResGamePointRank](#lq-ResGamePointRank) |  |
| fetchGameRecord | [ReqGameRecord](#lq-ReqGameRecord) | [ResGameRecord](#lq-ResGameRecord) |  |
| fetchGameRecordList | [ReqGameRecordList](#lq-ReqGameRecordList) | [ResGameRecordList](#lq-ResGameRecordList) |  |
| fetchGameRecordListV2 | [ReqGameRecordListV2](#lq-ReqGameRecordListV2) | [ResGameRecordListV2](#lq-ResGameRecordListV2) |  |
| fetchGameRecordsDetail | [ReqGameRecordsDetail](#lq-ReqGameRecordsDetail) | [ResGameRecordsDetail](#lq-ResGameRecordsDetail) |  |
| fetchGameRecordsDetailV2 | [ReqGameRecordsDetailV2](#lq-ReqGameRecordsDetailV2) | [ResGameRecordsDetailV2](#lq-ResGameRecordsDetailV2) |  |
| fetchGamingInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchGamingInfo](#lq-ResFetchGamingInfo) |  |
| fetchIDCardInfo | [ReqCommon](#lq-ReqCommon) | [ResIDCardInfo](#lq-ResIDCardInfo) |  |
| fetchInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchInfo](#lq-ResFetchInfo) |  |
| fetchJPCommonCreditCardOrder | [ReqFetchJPCommonCreditCardOrder](#lq-ReqFetchJPCommonCreditCardOrder) | [ResFetchJPCommonCreditCardOrder](#lq-ResFetchJPCommonCreditCardOrder) |  |
| fetchLastPrivacy | [ReqFetchLastPrivacy](#lq-ReqFetchLastPrivacy) | [ResFetchLastPrivacy](#lq-ResFetchLastPrivacy) |  |
| fetchLevelLeaderboard | [ReqLevelLeaderboard](#lq-ReqLevelLeaderboard) | [ResLevelLeaderboard](#lq-ResLevelLeaderboard) |  |
| fetchMailInfo | [ReqCommon](#lq-ReqCommon) | [ResMailInfo](#lq-ResMailInfo) |  |
| fetchMaintainNotice | [ReqCommon](#lq-ReqCommon) | [ResFetchMaintainNotice](#lq-ResFetchMaintainNotice) |  |
| fetchManagerCustomizedContest | [ReqFetchManagerCustomizedContest](#lq-ReqFetchManagerCustomizedContest) | [ResFetchManagerCustomizedContest](#lq-ResFetchManagerCustomizedContest) |  |
| fetchManagerCustomizedContestList | [ReqFetchmanagerCustomizedContestList](#lq-ReqFetchmanagerCustomizedContestList) | [ResFetchManagerCustomizedContestList](#lq-ResFetchManagerCustomizedContestList) |  |
| fetchMisc | [ReqCommon](#lq-ReqCommon) | [ResMisc](#lq-ResMisc) |  |
| fetchModNicknameTime | [ReqCommon](#lq-ReqCommon) | [ResModNicknameTime](#lq-ResModNicknameTime) |  |
| fetchMonthTicketInfo | [ReqCommon](#lq-ReqCommon) | [ResMonthTicketInfo](#lq-ResMonthTicketInfo) |  |
| fetchMultiAccountBrief | [ReqMultiAccountId](#lq-ReqMultiAccountId) | [ResMultiAccountBrief](#lq-ResMultiAccountBrief) |  |
| fetchMutiChallengeLevel | [ReqMutiChallengeLevel](#lq-ReqMutiChallengeLevel) | [ResMutiChallengeLevel](#lq-ResMutiChallengeLevel) |  |
| fetchNextGameRecordList | [ReqNextGameRecordList](#lq-ReqNextGameRecordList) | [ResNextGameRecordList](#lq-ResNextGameRecordList) |  |
| fetchOBToken | [ReqFetchOBToken](#lq-ReqFetchOBToken) | [ResFetchOBToken](#lq-ResFetchOBToken) |  |
| fetchOauth2Info | [ReqFetchOauth2](#lq-ReqFetchOauth2) | [ResFetchOauth2](#lq-ResFetchOauth2) |  |
| fetchPhoneLoginBind | [ReqCommon](#lq-ReqCommon) | [ResFetchPhoneLoginBind](#lq-ResFetchPhoneLoginBind) |  |
| fetchPlatformProducts | [ReqPlatformBillingProducts](#lq-ReqPlatformBillingProducts) | [ResPlatformBillingProducts](#lq-ResPlatformBillingProducts) |  |
| fetchProgressRewardActivityInfo | [ReqFetchProgressRewardActivityInfo](#lq-ReqFetchProgressRewardActivityInfo) | [ResFetchProgressRewardActivityInfo](#lq-ResFetchProgressRewardActivityInfo) |  |
| fetchQuestionnaireDetail | [ReqFetchQuestionnaireDetail](#lq-ReqFetchQuestionnaireDetail) | [ResFetchQuestionnaireDetail](#lq-ResFetchQuestionnaireDetail) |  |
| fetchQuestionnaireList | [ReqFetchQuestionnaireList](#lq-ReqFetchQuestionnaireList) | [ResFetchQuestionnaireList](#lq-ResFetchQuestionnaireList) |  |
| fetchQueueInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchQueueInfo](#lq-ResFetchQueueInfo) |  |
| fetchRPGBattleHistory | [ReqFetchRPGBattleHistory](#lq-ReqFetchRPGBattleHistory) | [ResFetchRPGBattleHistory](#lq-ResFetchRPGBattleHistory) |  |
| fetchRPGBattleHistoryV2 | [ReqFetchRPGBattleHistory](#lq-ReqFetchRPGBattleHistory) | [ResFetchRPGBattleHistoryV2](#lq-ResFetchRPGBattleHistoryV2) |  |
| fetchRandomCharacter | [ReqCommon](#lq-ReqCommon) | [ResRandomCharacter](#lq-ResRandomCharacter) |  |
| fetchRankPointLeaderboard | [ReqFetchRankPointLeaderboard](#lq-ReqFetchRankPointLeaderboard) | [ResFetchRankPointLeaderboard](#lq-ResFetchRankPointLeaderboard) |  |
| fetchReadyPlayerList | [ReqFetchReadyPlayerList](#lq-ReqFetchReadyPlayerList) | [ResFetchReadyPlayerList](#lq-ResFetchReadyPlayerList) |  |
| fetchRecentFriend | [ReqCommon](#lq-ReqCommon) | [ResFetchrecentFriend](#lq-ResFetchrecentFriend) |  |
| fetchRefundOrder | [ReqCommon](#lq-ReqCommon) | [ResFetchRefundOrder](#lq-ResFetchRefundOrder) |  |
| fetchReviveCoinInfo | [ReqCommon](#lq-ReqCommon) | [ResReviveCoinInfo](#lq-ResReviveCoinInfo) |  |
| fetchRollingNotice | [ReqFetchRollingNotice](#lq-ReqFetchRollingNotice) | [ResFetchRollingNotice](#lq-ResFetchRollingNotice) |  |
| fetchRoom | [ReqCommon](#lq-ReqCommon) | [ResSelfRoom](#lq-ResSelfRoom) |  |
| fetchSeerInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchSeerInfo](#lq-ResFetchSeerInfo) |  |
| fetchSeerReport | [ReqFetchSeerReport](#lq-ReqFetchSeerReport) | [ResFetchSeerReport](#lq-ResFetchSeerReport) |  |
| fetchSeerReportList | [ReqCommon](#lq-ReqCommon) | [ResFetchSeerReportList](#lq-ResFetchSeerReportList) |  |
| fetchSelfGamePointRank | [ReqGamePointRank](#lq-ReqGamePointRank) | [ResFetchSelfGamePointRank](#lq-ResFetchSelfGamePointRank) |  |
| fetchServerMaintenanceInfo | [ReqCommon](#lq-ReqCommon) | [ResFetchServerMaintenanceInfo](#lq-ResFetchServerMaintenanceInfo) |  |
| fetchServerSettings | [ReqCommon](#lq-ReqCommon) | [ResServerSettings](#lq-ResServerSettings) |  |
| fetchServerTime | [ReqCommon](#lq-ReqCommon) | [ResServerTime](#lq-ResServerTime) |  |
| fetchShopInfo | [ReqCommon](#lq-ReqCommon) | [ResShopInfo](#lq-ResShopInfo) |  |
| fetchShopInterval | [ReqCommon](#lq-ReqCommon) | [ResFetchShopInterval](#lq-ResFetchShopInterval) |  |
| fetchSimulationGameRank | [ReqFetchSimulationGameRank](#lq-ReqFetchSimulationGameRank) | [ResFetchSimulationGameRank](#lq-ResFetchSimulationGameRank) |  |
| fetchSimulationGameRecord | [ReqFetchSimulationGameRecord](#lq-ReqFetchSimulationGameRecord) | [ResFetchSimulationGameRecord](#lq-ResFetchSimulationGameRecord) |  |
| fetchTitleList | [ReqCommon](#lq-ReqCommon) | [ResTitleList](#lq-ResTitleList) |  |
| fetchVipReward | [ReqCommon](#lq-ReqCommon) | [ResVipReward](#lq-ResVipReward) |  |
| fetchVoteActivity | [ReqFetchVoteActivity](#lq-ReqFetchVoteActivity) | [ResFetchVoteActivity](#lq-ResFetchVoteActivity) |  |
| finishCombiningOrder | [ReqFinishCombiningOrder](#lq-ReqFinishCombiningOrder) | [ResFinishCombiningOrder](#lq-ResFinishCombiningOrder) |  |
| followCustomizedContest | [ReqTargetCustomizedContest](#lq-ReqTargetCustomizedContest) | [ResCommon](#lq-ResCommon) |  |
| forceCompleteChallengeTask | [ReqForceCompleteChallengeTask](#lq-ReqForceCompleteChallengeTask) | [ResCommon](#lq-ResCommon) |  |
| gainAccumulatedPointActivityReward | [ReqGainAccumulatedPointActivityReward](#lq-ReqGainAccumulatedPointActivityReward) | [ResCommon](#lq-ResCommon) |  |
| gainMultiPointActivityReward | [ReqGainMultiPointActivityReward](#lq-ReqGainMultiPointActivityReward) | [ResCommon](#lq-ResCommon) |  |
| gainRankPointReward | [ReqGainRankPointReward](#lq-ReqGainRankPointReward) | [ResCommon](#lq-ResCommon) |  |
| gainReviveCoin | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| gainVipReward | [ReqGainVipReward](#lq-ReqGainVipReward) | [ResCommon](#lq-ResCommon) |  |
| gameMasterCommand | [ReqGMCommand](#lq-ReqGMCommand) | [ResCommon](#lq-ResCommon) |  |
| generateAnnualReportToken | [ReqGenerateAnnualReportToken](#lq-ReqGenerateAnnualReportToken) | [ResGenerateAnnualReportToken](#lq-ResGenerateAnnualReportToken) |  |
| generateCombiningCraft | [ReqGenerateCombiningCraft](#lq-ReqGenerateCombiningCraft) | [ResGenerateCombiningCraft](#lq-ResGenerateCombiningCraft) |  |
| generateContestManagerLoginCode | [ReqCommon](#lq-ReqCommon) | [ResGenerateContestManagerLoginCode](#lq-ResGenerateContestManagerLoginCode) |  |
| getFriendVillageData | [ReqGetFriendVillageData](#lq-ReqGetFriendVillageData) | [ResGetFriendVillageData](#lq-ResGetFriendVillageData) |  |
| goNextShiLian | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| handleFriendApply | [ReqHandleFriendApply](#lq-ReqHandleFriendApply) | [ResCommon](#lq-ResCommon) |  |
| heatbeat | [ReqHeatBeat](#lq-ReqHeatBeat) | [ResCommon](#lq-ResCommon) |  |
| islandActivityBuy | [ReqIslandActivityBuy](#lq-ReqIslandActivityBuy) | [ResCommon](#lq-ResCommon) |  |
| islandActivityMove | [ReqIslandActivityMove](#lq-ReqIslandActivityMove) | [ResCommon](#lq-ResCommon) |  |
| islandActivitySell | [ReqIslandActivitySell](#lq-ReqIslandActivitySell) | [ResCommon](#lq-ResCommon) |  |
| islandActivityTidyBag | [ReqIslandActivityTidyBag](#lq-ReqIslandActivityTidyBag) | [ResCommon](#lq-ResCommon) |  |
| islandActivityUnlockBagGrid | [ReqIslandActivityUnlockBagGrid](#lq-ReqIslandActivityUnlockBagGrid) | [ResCommon](#lq-ResCommon) |  |
| joinCustomizedContestChatRoom | [ReqJoinCustomizedContestChatRoom](#lq-ReqJoinCustomizedContestChatRoom) | [ResJoinCustomizedContestChatRoom](#lq-ResJoinCustomizedContestChatRoom) |  |
| joinRoom | [ReqJoinRoom](#lq-ReqJoinRoom) | [ResJoinRoom](#lq-ResJoinRoom) |  |
| leaveComment | [ReqLeaveComment](#lq-ReqLeaveComment) | [ResCommon](#lq-ResCommon) |  |
| leaveCustomizedContest | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| leaveCustomizedContestChatRoom | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| leaveRoom | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| likeSNS | [ReqLikeSNS](#lq-ReqLikeSNS) | [ResLikeSNS](#lq-ResLikeSNS) |  |
| logReport | [ReqLogReport](#lq-ReqLogReport) | [ResCommon](#lq-ResCommon) |  |
| login | [ReqLogin](#lq-ReqLogin) | [ResLogin](#lq-ResLogin) |  |
| loginBeat | [ReqLoginBeat](#lq-ReqLoginBeat) | [ResCommon](#lq-ResCommon) |  |
| loginSuccess | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| logout | [ReqLogout](#lq-ReqLogout) | [ResLogout](#lq-ResLogout) |  |
| marathonActivityFinishRace | [ReqMarathonActivityFinishRace](#lq-ReqMarathonActivityFinishRace) | [ResMarathonActivityFinishRace](#lq-ResMarathonActivityFinishRace) |  |
| marathonActivityStartRace | [ReqMarathonActivityStartRace](#lq-ReqMarathonActivityStartRace) | [ResMarathonActivityStartRace](#lq-ResMarathonActivityStartRace) |  |
| matchGame | [ReqJoinMatchQueue](#lq-ReqJoinMatchQueue) | [ResCommon](#lq-ResCommon) |  |
| matchShiLian | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| mmoActivityDebugSetTeamCandidate | [ReqMMOActivityDebugSetTeamCandidate](#lq-ReqMMOActivityDebugSetTeamCandidate) | [ResMMOActivityDebugSetTeamCandidate](#lq-ResMMOActivityDebugSetTeamCandidate) |  |
| mmoActivityEquipFusion | [ReqMMOActivityEquipFusion](#lq-ReqMMOActivityEquipFusion) | [ResMMOActivityEquipFusion](#lq-ResMMOActivityEquipFusion) |  |
| mmoActivityFetchData | [ReqMMOActivityFetchData](#lq-ReqMMOActivityFetchData) | [ResMMOActivityFetchData](#lq-ResMMOActivityFetchData) |  |
| mmoActivityFinishBattle | [ReqMMOActivityFinishBattle](#lq-ReqMMOActivityFinishBattle) | [ResMMOActivityFinishBattle](#lq-ResMMOActivityFinishBattle) |  |
| mmoActivityReceiveSupportReward | [ReqMMOActivityReceiveSupportReward](#lq-ReqMMOActivityReceiveSupportReward) | [ResMMOActivityReceiveSupportReward](#lq-ResMMOActivityReceiveSupportReward) |  |
| mmoActivitySetCharacter | [ReqMMOActivitySetCharacter](#lq-ReqMMOActivitySetCharacter) | [ResMMOActivitySetCharacter](#lq-ResMMOActivitySetCharacter) |  |
| mmoActivitySetEquip | [ReqMMOActivitySetEquip](#lq-ReqMMOActivitySetEquip) | [ResMMOActivitySetEquip](#lq-ResMMOActivitySetEquip) |  |
| mmoActivitySetTeamMember | [ReqMMOActivitySetTeamMember](#lq-ReqMMOActivitySetTeamMember) | [ResMMOActivitySetTeamMember](#lq-ResMMOActivitySetTeamMember) |  |
| mmoActivityStartBattle | [ReqMMOActivityStartBattle](#lq-ReqMMOActivityStartBattle) | [ResMMOActivityStartBattle](#lq-ResMMOActivityStartBattle) |  |
| mmoActivityUpdateFriendList | [ReqMMOActivityUpdatehFriendList](#lq-ReqMMOActivityUpdatehFriendList) | [ResMMOActivityUpdatehFriendList](#lq-ResMMOActivityUpdatehFriendList) |  |
| modifyBirthday | [ReqModifyBirthday](#lq-ReqModifyBirthday) | [ResCommon](#lq-ResCommon) |  |
| modifyNickname | [ReqModifyNickname](#lq-ReqModifyNickname) | [ResCommon](#lq-ResCommon) |  |
| modifyPassword | [ReqModifyPassword](#lq-ReqModifyPassword) | [ResCommon](#lq-ResCommon) |  |
| modifyRoom | [ReqModifyRoom](#lq-ReqModifyRoom) | [ResCommon](#lq-ResCommon) |  |
| modifySignature | [ReqModifySignature](#lq-ReqModifySignature) | [ResCommon](#lq-ResCommon) |  |
| moveCombiningCraft | [ReqMoveCombiningCraft](#lq-ReqMoveCombiningCraft) | [ResMoveCombiningCraft](#lq-ResMoveCombiningCraft) |  |
| nextRoundVillage | [ReqNextRoundVillage](#lq-ReqNextRoundVillage) | [ResNextRoundVillage](#lq-ResNextRoundVillage) |  |
| oauth2Auth | [ReqOauth2Auth](#lq-ReqOauth2Auth) | [ResOauth2Auth](#lq-ResOauth2Auth) |  |
| oauth2Check | [ReqOauth2Check](#lq-ReqOauth2Check) | [ResOauth2Check](#lq-ResOauth2Check) |  |
| oauth2Login | [ReqOauth2Login](#lq-ReqOauth2Login) | [ResLogin](#lq-ResLogin) |  |
| oauth2Signup | [ReqOauth2Signup](#lq-ReqOauth2Signup) | [ResOauth2Signup](#lq-ResOauth2Signup) |  |
| openAllRewardItem | [ReqOpenAllRewardItem](#lq-ReqOpenAllRewardItem) | [ResOpenAllRewardItem](#lq-ResOpenAllRewardItem) |  |
| openChest | [ReqOpenChest](#lq-ReqOpenChest) | [ResOpenChest](#lq-ResOpenChest) |  |
| openGacha | [ReqOpenGacha](#lq-ReqOpenGacha) | [ResOpenGacha](#lq-ResOpenGacha) |  |
| openManualItem | [ReqOpenManualItem](#lq-ReqOpenManualItem) | [ResCommon](#lq-ResCommon) |  |
| openPreChestItem | [ReqOpenPreChestItem](#lq-ReqOpenPreChestItem) | [ResOpenPreChestItem](#lq-ResOpenPreChestItem) |  |
| openRandomRewardItem | [ReqOpenRandomRewardItem](#lq-ReqOpenRandomRewardItem) | [ResOpenRandomRewardItem](#lq-ResOpenRandomRewardItem) |  |
| openidCheck | [ReqOpenidCheck](#lq-ReqOpenidCheck) | [ResOauth2Check](#lq-ResOauth2Check) |  |
| payMonthTicket | [ReqCommon](#lq-ReqCommon) | [ResPayMonthTicket](#lq-ResPayMonthTicket) |  |
| prepareLogin | [ReqPrepareLogin](#lq-ReqPrepareLogin) | [ResCommon](#lq-ResCommon) |  |
| progressRewardActivityReceive | [ReqProgressRewardActivityReceive](#lq-ReqProgressRewardActivityReceive) | [ResProgressRewardActivityReceive](#lq-ResProgressRewardActivityReceive) |  |
| questCrewActivityFeed | [ReqQuestCrewActivityFeed](#lq-ReqQuestCrewActivityFeed) | [ResQuestCrewActivityFeed](#lq-ResQuestCrewActivityFeed) |  |
| questCrewActivityHire | [ReqQuestCrewActivityHire](#lq-ReqQuestCrewActivityHire) | [ResQuestCrewActivityHire](#lq-ResQuestCrewActivityHire) |  |
| questCrewActivityRefreshMarket | [ReqQuestCrewActivityRefreshMarket](#lq-ReqQuestCrewActivityRefreshMarket) | [ResQuestCrewActivityRefreshMarket](#lq-ResQuestCrewActivityRefreshMarket) |  |
| questCrewActivityStartQuest | [ReqQuestCrewActivityStartQuest](#lq-ReqQuestCrewActivityStartQuest) | [ResQuestCrewActivityStartQuest](#lq-ResQuestCrewActivityStartQuest) |  |
| quitABMatch | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| readAnnouncement | [ReqReadAnnouncement](#lq-ReqReadAnnouncement) | [ResCommon](#lq-ResCommon) |  |
| readGameRecord | [ReqGameRecord](#lq-ReqGameRecord) | [ResCommon](#lq-ResCommon) |  |
| readMail | [ReqReadMail](#lq-ReqReadMail) | [ResCommon](#lq-ResCommon) |  |
| readSNS | [ReqReadSNS](#lq-ReqReadSNS) | [ResReadSNS](#lq-ResReadSNS) |  |
| readyPlay | [ReqRoomReady](#lq-ReqRoomReady) | [ResCommon](#lq-ResCommon) |  |
| receiveABMatchReward | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| receiveAchievementGroupReward | [ReqReceiveAchievementGroupReward](#lq-ReqReceiveAchievementGroupReward) | [ResReceiveAchievementGroupReward](#lq-ResReceiveAchievementGroupReward) |  |
| receiveAchievementReward | [ReqReceiveAchievementReward](#lq-ReqReceiveAchievementReward) | [ResReceiveAchievementReward](#lq-ResReceiveAchievementReward) |  |
| receiveActivityFlipTask | [ReqReceiveActivityFlipTask](#lq-ReqReceiveActivityFlipTask) | [ResReceiveActivityFlipTask](#lq-ResReceiveActivityFlipTask) |  |
| receiveActivityFlipTaskBatch | [ReqReceiveActivityFlipTaskBatch](#lq-ReqReceiveActivityFlipTaskBatch) | [ResReceiveActivityFlipTaskBatch](#lq-ResReceiveActivityFlipTaskBatch) |  |
| receiveActivityGift | [ReqReceiveActivityGift](#lq-ReqReceiveActivityGift) | [ResCommon](#lq-ResCommon) |  |
| receiveActivitySpotReward | [ReqReceiveActivitySpotReward](#lq-ReqReceiveActivitySpotReward) | [ResReceiveActivitySpotReward](#lq-ResReceiveActivitySpotReward) |  |
| receiveAllActivityGift | [ReqReceiveAllActivityGift](#lq-ReqReceiveAllActivityGift) | [ResReceiveAllActivityGift](#lq-ResReceiveAllActivityGift) |  |
| receiveArenaReward | [ReqArenaReward](#lq-ReqArenaReward) | [ResArenaReward](#lq-ResArenaReward) |  |
| receiveChallengeRankReward | [ReqReceiveChallengeRankReward](#lq-ReqReceiveChallengeRankReward) | [ResReceiveChallengeRankReward](#lq-ResReceiveChallengeRankReward) |  |
| receiveCharacterRewards | [ReqReceiveCharacterRewards](#lq-ReqReceiveCharacterRewards) | [ResReceiveCharacterRewards](#lq-ResReceiveCharacterRewards) |  |
| receiveEndingReward | [ReqFinishedEnding](#lq-ReqFinishedEnding) | [ResCommon](#lq-ResCommon) |  |
| receiveRPGReward | [ReqReceiveRPGReward](#lq-ReqReceiveRPGReward) | [ResReceiveRPGRewards](#lq-ResReceiveRPGRewards) |  |
| receiveRPGRewards | [ReqReceiveRPGRewards](#lq-ReqReceiveRPGRewards) | [ResReceiveRPGRewards](#lq-ResReceiveRPGRewards) |  |
| receiveUpgradeActivityReward | [ReqReceiveUpgradeActivityReward](#lq-ReqReceiveUpgradeActivityReward) | [ResReceiveUpgradeActivityReward](#lq-ResReceiveUpgradeActivityReward) |  |
| receiveVersionReward | [ReqCommon](#lq-ReqCommon) | [ResCommon](#lq-ResCommon) |  |
| receiveVillageBuildingReward | [ReqReceiveVillageBuildingReward](#lq-ReqReceiveVillageBuildingReward) | [ResReceiveVillageBuildingReward](#lq-ResReceiveVillageBuildingReward) |  |
| receiveVillageTripReward | [ReqReceiveVillageTripReward](#lq-ReqReceiveVillageTripReward) | [ResReceiveVillageTripReward](#lq-ResReceiveVillageTripReward) |  |
| recoverCombiningRecycle | [ReqRecoverCombiningRecycle](#lq-ReqRecoverCombiningRecycle) | [ResRecoverCombiningRecycle](#lq-ResRecoverCombiningRecycle) |  |
| refreshChallenge | [ReqCommon](#lq-ReqCommon) | [ResRefreshChallenge](#lq-ResRefreshChallenge) |  |
| refreshDailyTask | [ReqRefreshDailyTask](#lq-ReqRefreshDailyTask) | [ResRefreshDailyTask](#lq-ResRefreshDailyTask) |  |
| refreshGameObserveAuth | [ReqRefreshGameObserveAuth](#lq-ReqRefreshGameObserveAuth) | [ResRefreshGameObserveAuth](#lq-ResRefreshGameObserveAuth) |  |
| refreshZHPShop | [ReqReshZHPShop](#lq-ReqReshZHPShop) | [ResRefreshZHPShop](#lq-ResRefreshZHPShop) |  |
| remarkFriend | [ReqRemarkFriend](#lq-ReqRemarkFriend) | [ResCommon](#lq-ResCommon) |  |
| removeCollectedGameRecord | [ReqRemoveCollectedGameRecord](#lq-ReqRemoveCollectedGameRecord) | [ResRemoveCollectedGameRecord](#lq-ResRemoveCollectedGameRecord) |  |
| removeFriend | [ReqRemoveFriend](#lq-ReqRemoveFriend) | [ResCommon](#lq-ResCommon) |  |
| replySNS | [ReqReplySNS](#lq-ReqReplySNS) | [ResReplySNS](#lq-ResReplySNS) |  |
| resolveFestivalActivityEvent | [ReqResolveFestivalActivityEvent](#lq-ReqResolveFestivalActivityEvent) | [ResResolveFestivalActivityEvent](#lq-ResResolveFestivalActivityEvent) |  |
| resolveFestivalActivityProposal | [ReqResolveFestivalActivityProposal](#lq-ReqResolveFestivalActivityProposal) | [ResResolveFestivalActivityProposal](#lq-ResResolveFestivalActivityProposal) |  |
| richmanAcitivitySpecialMove | [ReqRichmanSpecialMove](#lq-ReqRichmanSpecialMove) | [ResRichmanNextMove](#lq-ResRichmanNextMove) |  |
| richmanActivityChestInfo | [ReqRichmanChestInfo](#lq-ReqRichmanChestInfo) | [ResRichmanChestInfo](#lq-ResRichmanChestInfo) |  |
| richmanActivityNextMove | [ReqRichmanNextMove](#lq-ReqRichmanNextMove) | [ResRichmanNextMove](#lq-ResRichmanNextMove) |  |
| roomKickPlayer | [ReqRoomKickPlayer](#lq-ReqRoomKickPlayer) | [ResCommon](#lq-ResCommon) |  |
| saveCommonViews | [ReqSaveCommonViews](#lq-ReqSaveCommonViews) | [ResCommon](#lq-ResCommon) |  |
| sayChatMessage | [ReqSayChatMessage](#lq-ReqSayChatMessage) | [ResCommon](#lq-ResCommon) |  |
| searchAccountByEid | [ReqSearchAccountByEidLobby](#lq-ReqSearchAccountByEidLobby) | [ResSearchAccountbyEidLobby](#lq-ResSearchAccountbyEidLobby) |  |
| searchAccountById | [ReqSearchAccountById](#lq-ReqSearchAccountById) | [ResSearchAccountById](#lq-ResSearchAccountById) |  |
| searchAccountByPattern | [ReqSearchAccountByPattern](#lq-ReqSearchAccountByPattern) | [ResSearchAccountByPattern](#lq-ResSearchAccountByPattern) |  |
| selectChestChooseGroupActivity | [ReqSelectChestChooseGroupActivity](#lq-ReqSelectChestChooseGroupActivity) | [ResCommon](#lq-ResCommon) |  |
| selectChestChooseUpActivity | [ReqSelectChestChooseUp](#lq-ReqSelectChestChooseUp) | [ResCommon](#lq-ResCommon) |  |
| sellItem | [ReqSellItem](#lq-ReqSellItem) | [ResCommon](#lq-ResCommon) |  |
| sendActivityGiftToFriend | [ReqSendActivityGiftToFriend](#lq-ReqSendActivityGiftToFriend) | [ResSendActivityGiftToFriend](#lq-ResSendActivityGiftToFriend) |  |
| sendClientMessage | [ReqSendClientMessage](#lq-ReqSendClientMessage) | [ResCommon](#lq-ResCommon) |  |
| sendGiftToCharacter | [ReqSendGiftToCharacter](#lq-ReqSendGiftToCharacter) | [ResSendGiftToCharacter](#lq-ResSendGiftToCharacter) |  |
| setAccountFavoriteHu | [ReqSetAccountFavoriteHu](#lq-ReqSetAccountFavoriteHu) | [ResCommon](#lq-ResCommon) |  |
| setActivityBuff | [ReqSetActivityBuff](#lq-ReqSetActivityBuff) | [ResActivityBuff](#lq-ResActivityBuff) |  |
| setFriendRoomRandomBotChar | [ReqSetFriendRoomRandomBotChar](#lq-ReqSetFriendRoomRandomBotChar) | [ResCommon](#lq-ResCommon) |  |
| setHiddenCharacter | [ReqSetHiddenCharacter](#lq-ReqSetHiddenCharacter) | [ResSetHiddenCharacter](#lq-ResSetHiddenCharacter) |  |
| setLoadingImage | [ReqSetLoadingImage](#lq-ReqSetLoadingImage) | [ResCommon](#lq-ResCommon) |  |
| setRandomCharacter | [ReqRandomCharacter](#lq-ReqRandomCharacter) | [ResCommon](#lq-ResCommon) |  |
| setVerifiedHidden | [ReqSetVerifiedHidden](#lq-ReqSetVerifiedHidden) | [ResCommon](#lq-ResCommon) |  |
| setVillageWorker | [ReqSetVillageWorker](#lq-ReqSetVillageWorker) | [ResSetVillageWorker](#lq-ResSetVillageWorker) |  |
| shootActivityAttackEnemies | [ReqShootActivityAttackEnemies](#lq-ReqShootActivityAttackEnemies) | [ResShootActivityAttackEnemies](#lq-ResShootActivityAttackEnemies) |  |
| shopPurchase | [ReqShopPurchase](#lq-ReqShopPurchase) | [ResShopPurchase](#lq-ResShopPurchase) |  |
| signup | [ReqSignupAccount](#lq-ReqSignupAccount) | [ResSignupAccount](#lq-ResSignupAccount) |  |
| signupCustomizedContest | [ReqSignupCustomizedContest](#lq-ReqSignupCustomizedContest) | [ResSignupCustomizedContest](#lq-ResSignupCustomizedContest) |  |
| simV2ActivityEndMatch | [ReqSimV2ActivityEndMatch](#lq-ReqSimV2ActivityEndMatch) | [ResSimV2ActivityEndMatch](#lq-ResSimV2ActivityEndMatch) |  |
| simV2ActivityFetchInfo | [ReqSimV2ActivityFetchInfo](#lq-ReqSimV2ActivityFetchInfo) | [ResSimV2ActivityFetchInfo](#lq-ResSimV2ActivityFetchInfo) |  |
| simV2ActivityGiveUp | [ReqSimV2ActivityGiveUp](#lq-ReqSimV2ActivityGiveUp) | [ResCommon](#lq-ResCommon) |  |
| simV2ActivitySelectEvent | [ReqSimV2ActivitySelectEvent](#lq-ReqSimV2ActivitySelectEvent) | [ResSimV2ActivitySelectEvent](#lq-ResSimV2ActivitySelectEvent) |  |
| simV2ActivitySetUpgrade | [ReqSimV2ActivitySetUpgrade](#lq-ReqSimV2ActivitySetUpgrade) | [ResCommon](#lq-ResCommon) |  |
| simV2ActivityStartMatch | [ReqSimV2ActivityStartMatch](#lq-ReqSimV2ActivityStartMatch) | [ResSimV2ActivityStartMatch](#lq-ResSimV2ActivityStartMatch) |  |
| simV2ActivityStartSeason | [ReqSimV2ActivityStartSeason](#lq-ReqSimV2ActivityStartSeason) | [ResSimV2ActivityStartSeason](#lq-ResSimV2ActivityStartSeason) |  |
| simV2ActivityTrain | [ReqSimV2ActivityTrain](#lq-ReqSimV2ActivityTrain) | [ResSimV2ActivityTrain](#lq-ResSimV2ActivityTrain) |  |
| simulationActivityTrain | [ReqSimulationActivityTrain](#lq-ReqSimulationActivityTrain) | [ResSimulationActivityTrain](#lq-ResSimulationActivityTrain) |  |
| snowballActivityFinishBattle | [ReqSnowballActivityFinishBattle](#lq-ReqSnowballActivityFinishBattle) | [ResSnowballActivityFinishBattle](#lq-ResSnowballActivityFinishBattle) |  |
| snowballActivityReceiveReward | [ReqSnowballActivityReceiveReward](#lq-ReqSnowballActivityReceiveReward) | [ResSnowballActivityReceiveReward](#lq-ResSnowballActivityReceiveReward) |  |
| snowballActivityStartBattle | [ReqSnowballActivityStartBattle](#lq-ReqSnowballActivityStartBattle) | [ResSnowballActivityStartBattle](#lq-ResSnowballActivityStartBattle) |  |
| snowballActivityUpgrade | [ReqSnowballActivityUpgrade](#lq-ReqSnowballActivityUpgrade) | [ResSnowballActivityUpgrade](#lq-ResSnowballActivityUpgrade) |  |
| solveGooglePayOrderV3 | [ReqSolveGooglePlayOrderV3](#lq-ReqSolveGooglePlayOrderV3) | [ResCommon](#lq-ResCommon) |  |
| solveGooglePlayOrder | [ReqSolveGooglePlayOrder](#lq-ReqSolveGooglePlayOrder) | [ResCommon](#lq-ResCommon) |  |
| startCustomizedContest | [ReqStartCustomizedContest](#lq-ReqStartCustomizedContest) | [ResCommon](#lq-ResCommon) |  |
| startRoom | [ReqRoomStart](#lq-ReqRoomStart) | [ResCommon](#lq-ResCommon) |  |
| startSimulationActivityGame | [ReqStartSimulationActivityGame](#lq-ReqStartSimulationActivityGame) | [ResStartSimulationActivityGame](#lq-ResStartSimulationActivityGame) |  |
| startUnifiedMatch | [ReqStartUnifiedMatch](#lq-ReqStartUnifiedMatch) | [ResCommon](#lq-ResCommon) |  |
| startVillageTrip | [ReqStartVillageTrip](#lq-ReqStartVillageTrip) | [ResCommon](#lq-ResCommon) |  |
| stopCustomizedContest | [ReqStopCustomizedContest](#lq-ReqStopCustomizedContest) | [ResCommon](#lq-ResCommon) |  |
| storyActivityReceiveAllFinishReward | [ReqStoryActivityReceiveAllFinishReward](#lq-ReqStoryActivityReceiveAllFinishReward) | [ResStoryReward](#lq-ResStoryReward) |  |
| storyActivityReceiveEndingReward | [ReqStoryActivityReceiveEndingReward](#lq-ReqStoryActivityReceiveEndingReward) | [ResStoryReward](#lq-ResStoryReward) |  |
| storyActivityReceiveFinishReward | [ReqStoryActivityReceiveFinishReward](#lq-ReqStoryActivityReceiveFinishReward) | [ResStoryReward](#lq-ResStoryReward) |  |
| storyActivityUnlock | [ReqStoryActivityUnlock](#lq-ReqStoryActivityUnlock) | [ResCommon](#lq-ResCommon) |  |
| storyActivityUnlockEnding | [ReqStoryActivityUnlockEnding](#lq-ReqStoryActivityUnlockEnding) | [ResCommon](#lq-ResCommon) |  |
| storyActivityUnlockEndingAndReceive | [ReqStoryActivityUnlockEndingAndReceive](#lq-ReqStoryActivityUnlockEndingAndReceive) | [ResStoryActivityUnlockEndingAndReceive](#lq-ResStoryActivityUnlockEndingAndReceive) |  |
| submitQuestionnaire | [ReqSubmitQuestionnaire](#lq-ReqSubmitQuestionnaire) | [ResCommon](#lq-ResCommon) |  |
| takeAttachmentFromMail | [ReqTakeAttachment](#lq-ReqTakeAttachment) | [ResCommon](#lq-ResCommon) |  |
| taskRequest | [ReqTaskRequest](#lq-ReqTaskRequest) | [ResCommon](#lq-ResCommon) |  |
| unbindPhoneNumber | [ReqUnbindPhoneNumber](#lq-ReqUnbindPhoneNumber) | [ResCommon](#lq-ResCommon) |  |
| unfollowCustomizedContest | [ReqTargetCustomizedContest](#lq-ReqTargetCustomizedContest) | [ResCommon](#lq-ResCommon) |  |
| unlockActivitySpot | [ReqUnlockActivitySpot](#lq-ReqUnlockActivitySpot) | [ResCommon](#lq-ResCommon) |  |
| unlockActivitySpotEnding | [ReqUnlockActivitySpotEnding](#lq-ReqUnlockActivitySpotEnding) | [ResCommon](#lq-ResCommon) |  |
| updateAccountSettings | [ReqUpdateAccountSettings](#lq-ReqUpdateAccountSettings) | [ResCommon](#lq-ResCommon) |  |
| updateCharacterSort | [ReqUpdateCharacterSort](#lq-ReqUpdateCharacterSort) | [ResCommon](#lq-ResCommon) |  |
| updateClientValue | [ReqUpdateClientValue](#lq-ReqUpdateClientValue) | [ResCommon](#lq-ResCommon) |  |
| updateCommentSetting | [ReqUpdateCommentSetting](#lq-ReqUpdateCommentSetting) | [ResCommon](#lq-ResCommon) |  |
| updateIDCardInfo | [ReqUpdateIDCardInfo](#lq-ReqUpdateIDCardInfo) | [ResCommon](#lq-ResCommon) |  |
| updateManagerCustomizedContest | [ReqUpdateManagerCustomizedContest](#lq-ReqUpdateManagerCustomizedContest) | [ResCommon](#lq-ResCommon) |  |
| updateReadComment | [ReqUpdateReadComment](#lq-ReqUpdateReadComment) | [ResCommon](#lq-ResCommon) |  |
| upgradeActivityBuff | [ReqUpgradeActivityBuff](#lq-ReqUpgradeActivityBuff) | [ResActivityBuff](#lq-ResActivityBuff) |  |
| upgradeActivityLevel | [ReqUpgradeActivityLevel](#lq-ReqUpgradeActivityLevel) | [ResUpgradeActivityLevel](#lq-ResUpgradeActivityLevel) |  |
| upgradeChallenge | [ReqCommon](#lq-ReqCommon) | [ResUpgradeChallenge](#lq-ResUpgradeChallenge) |  |
| upgradeCharacter | [ReqUpgradeCharacter](#lq-ReqUpgradeCharacter) | [ResUpgradeCharacter](#lq-ResUpgradeCharacter) |  |
| upgradeVillageBuilding | [ReqUpgradeVillageBuilding](#lq-ReqUpgradeVillageBuilding) | [ResCommon](#lq-ResCommon) |  |
| useBagItem | [ReqUseBagItem](#lq-ReqUseBagItem) | [ResCommon](#lq-ResCommon) |  |
| useCommonView | [ReqUseCommonView](#lq-ReqUseCommonView) | [ResCommon](#lq-ResCommon) |  |
| useGiftCode | [ReqUseGiftCode](#lq-ReqUseGiftCode) | [ResUseGiftCode](#lq-ResUseGiftCode) |  |
| useSpecialGiftCode | [ReqUseGiftCode](#lq-ReqUseGiftCode) | [ResUseSpecialGiftCode](#lq-ResUseSpecialGiftCode) |  |
| useTitle | [ReqUseTitle](#lq-ReqUseTitle) | [ResCommon](#lq-ResCommon) |  |
| userComplain | [ReqUserComplain](#lq-ReqUserComplain) | [ResCommon](#lq-ResCommon) |  |
| verfifyCodeForSecure | [ReqVerifyCodeForSecure](#lq-ReqVerifyCodeForSecure) | [ResVerfiyCodeForSecure](#lq-ResVerfiyCodeForSecure) |  |
| verificationIAPOrder | [ReqVerificationIAPOrder](#lq-ReqVerificationIAPOrder) | [ResVerificationIAPOrder](#lq-ResVerificationIAPOrder) |  |
| verifyMyCardOrder | [ReqVerifyMyCardOrder](#lq-ReqVerifyMyCardOrder) | [ResCommon](#lq-ResCommon) |  |
| verifySteamOrder | [ReqVerifySteamOrder](#lq-ReqVerifySteamOrder) | [ResCommon](#lq-ResCommon) |  |
| voteActivity | [ReqVoteActivity](#lq-ReqVoteActivity) | [ResVoteActivity](#lq-ResVoteActivity) |  |
| yostarDeleteAccount | [ReqYostarDeleteAccount](#lq-ReqYostarDeleteAccount) | [ResYostarDeleteAccount](#lq-ResYostarDeleteAccount) |  |


<a name="lq-Route"></a>

### Route


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| heartbeat | [ReqHeartbeat](#lq-ReqHeartbeat) | [ResHeartbeat](#lq-ResHeartbeat) |  |
| requestConnection | [ReqRequestConnection](#lq-ReqRequestConnection) | [ResRequestConnection](#lq-ResRequestConnection) |  |
| requestRouteChange | [ReqRequestRouteChange](#lq-ReqRequestRouteChange) | [ResRequestRouteChange](#lq-ResRequestRouteChange) |  |





## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

