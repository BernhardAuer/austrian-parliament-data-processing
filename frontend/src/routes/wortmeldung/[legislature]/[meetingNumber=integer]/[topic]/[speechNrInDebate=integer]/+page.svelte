<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	<title>Wortmeldung | parli-info.org</title>
</svelte:head>

<div class="mx-auto">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Wortmeldung
	</h1>
	<h2 class="text-2xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		{data.topic}
	</h2>
	<h3 class="text-xl font-normal leading-normal mt-0 mb-2 break-words">
		{data.meetingNumber}. NR-Sitzung / {data.legislature} GP
	</h3>
</div>

<div class="mx-auto py-4 space-y-2 max-w-3xl">
	{#each data.speech as speech, i}
		{#if speech.type == 'info'}
			<div class="flex justify-center items-center">
				<div class="badge-accent rounded-lg px-3 py-1">{speech.text}</div>
			</div>
		{:else if speech?.text?.length > 0}
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
