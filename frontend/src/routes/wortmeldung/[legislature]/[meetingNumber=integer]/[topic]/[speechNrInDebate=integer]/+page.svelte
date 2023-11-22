<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	<title>Wortmeldung | parli-info.org</title>
</svelte:head>

<div class="py-4 space-y-2 container">
	{#each data.speech as speech, i}
		{#if speech.type == 'info'}
			<div class="flex justify-center items-center">
				<div class="badge-accent rounded-lg px-3 py-1">{speech.text}</div>
			</div>
		{:else}
			<div class="chat chat-start">
				<div class="chat-header">
					{speech.nameOfSpeaker ?? ''}
					{#if speech?.startTime !== undefined}
						<time class="text-xs opacity-50">{speech.startTime}</time>
					{/if}
				</div>
				<div class="chat-bubble">
					{#each speech?.text as text, j}
						{text}
						<!-- do newlines only if there are further elements -->
						{#if j !== speech?.text?.length - 1}
							<br /> <br />
						{/if}
					{/each}
				</div>
			</div>
		{/if}
	{/each}
</div>
