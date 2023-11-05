<svelte:head>
	<title>Wortmeldung | parli-info.org</title>
</svelte:head>

<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div class="py-4 space-y-2">
	{#each data.speech as speech, i}
		<!-- <TopicAccordion {topic} topNr={data.speechesByTopic[topic][0]?.topNr} speeches={data.speechesByTopic[topic]} checked={i==0} />	 -->
	<!-- {topic.data} <br><br><br> -->

	{#if speech.type == "info"}
	<div class="flex justify-center items-center">

		<div class="badge badge-accent">{speech.text}</div>
	</div>
	{:else}
	<div class="chat chat-start">
		<div class="chat-header">
		  {speech.nameOfSpeaker ?? ""}
		  {#if speech?.startTime !== undefined}			
		  <time class="text-xs opacity-50">{speech.startTime}</time>
		  {/if}
		</div>
		<div class="chat-bubble">
		{#each speech?.text as text, j}
				{text} 
				<!-- do newlines only if there are further elements -->
				{#if (j !== speech?.text?.length -1)}
				<br> <br>
				{/if}
		{/each}
	</div>	
	  </div>
{/if}
	{/each}


</div>
