<script>
	import { LogarithmicScale } from 'chart.js';

	/** @type {import('./$types').PageData} */
	export let data;

	let availableChatBubbleColors = [
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
	let uniqueColorForNameDict = {}

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
	<!-- {JSON.stringify(data)} -->
	{#each data.speech as speech, i}
		{#if speech.type == 1}
			{#if speech?.subtype == "applause"}
			<div class="flex justify-center items-center">
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Beifall">
					👏🏻 {speech?.nameOfSpeaker}
					</div>
				</div>
			</div>
			{:else if speech?.subtype == "cheerfulness"}
			<div class="flex justify-center items-center">
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Heiterkeit">
					😅 {speech?.nameOfSpeaker}
					</div>
				</div>
			</div>
			{:else if speech?.subtype == "interjectionWithoutQuote"}
			<div class="flex justify-center items-center">
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Zwischenruf">
					🗣️ {speech?.nameOfSpeaker}
					</div>
				</div>
			</div>
			{:else}
				<div class="flex justify-center items-center">
					<div class="badge-accent rounded-lg px-3 py-1">{speech?.data}</div>
					<!-- {JSON.stringify(speech)} -->
				</div>
			{/if}
		{:else if speech.type == 3}
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
					<!-- {JSON.stringify(speech)} -->
					{#each speech?.data as text, j}
						{text}
						<!-- do newlines only if there are further elements -->
						{#if j !== speech?.data?.length - 1}
							<br /> <br />
						{/if}
					{/each}			
				</div>				
			</div>
		{/if}
	{/each}
</div>
