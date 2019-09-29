def channel_approve():
    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:
        pass
