<script>
    export let speech = null;
    export let availableChatBubbleColors;
    export let uniqueColorForNameDict;

    const getChatBubbleColor = (speechSubtype, name) => {
		switch(speechSubtype) {
			case "remarksFromPresident": return "chat-bubble-primary";	
			case "speechByMainSpeaker": return "chat-bubble-neutral";		
			case "interjection": 
				if (name in uniqueColorForNameDict) {
					return uniqueColorForNameDict[name];
				} else {
					let color = availableChatBubbleColors.pop();
					uniqueColorForNameDict[name] = color;
					return color;
				}
		}
	};
</script>

<div class="chat {speech?.subtype == "speechByMainSpeaker" ? "chat-start" : "chat-end"}">
    <div class="chat-header">
        {speech?.nameOfSpeaker ?? ''}										  
        {#if speech?.time}
            <time class="text-xs opacity-50">{speech?.time}</time>
        {/if}
        {#if speech?.description}
        <time class="text-xs opacity-50">{speech?.description}</time>
    {/if}
    </div>
    <div class="chat-bubble {getChatBubbleColor(speech?.subtype, speech?.nameOfSpeaker)}">
        {#each speech?.data as text, j}
            {text}
            <!-- do newlines only if there are further elements -->
            {#if j !== speech?.data?.length - 1}
                <br /> <br />
            {/if}
        {/each}			
    </div>				
</div>