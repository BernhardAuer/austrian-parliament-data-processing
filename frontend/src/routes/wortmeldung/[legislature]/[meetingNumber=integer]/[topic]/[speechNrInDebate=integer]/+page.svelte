<script>
	import InfoBadge from './InfoBadge.svelte';
import ChatBubble from './ChatBubble.svelte';

	/** @type {import('./$types').PageData} */
	export let data;

	const availableChatBubbleColors = [
		"bg-sky-100",
		"bg-red-300",
		"bg-slate-400",
	 	"bg-orange-100", 
	 	"bg-amber-100",
		"bg-lime-100",
		"bg-teal-100",
		"bg-blue-100",
		"bg-pink-100",
		"bg-stone-100",
	]
	const uniqueColorForNameDict = {}
	
</script>

<svelte:head>
	<title>Wortmeldung {data.nameOfSpeaker ?? ""} zu {data.topic} ({data.meetingNumber}/{data.legislature} GP) | parli-info.org</title>
</svelte:head>

<div class="mx-auto">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Wortmeldung {data.nameOfSpeaker ?? ""}
	</h1>
	<h2 class="text-2xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		{data.topic}
	</h2>
	<h3 class="text-xl font-normal leading-normal mt-0 mb-2 break-words">
		{data.meetingNumber}. NR-Sitzung / {data.legislature} GP
	</h3>
</div>

<div class="mx-auto py-4 space-y-2 max-w-3xl">
	{#each data.speech as speech}
		{#if speech.type == 1}
			<InfoBadge speech = {speech}/>
		{:else if speech.type == 3}
			<ChatBubble speech = {speech} uniqueColorForNameDict={uniqueColorForNameDict} availableChatBubbleColors={availableChatBubbleColors}/>
		{/if}
	{/each}
</div>
