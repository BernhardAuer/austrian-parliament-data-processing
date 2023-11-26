<svelte:head>
	<title>Wortmeldungen | parli-info.org</title>
</svelte:head>

<script>
	import TopicAccordion from './TopicAccordion.svelte';
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div class="py-4 space-y-2">
	{#each data.topics as topic}
		<TopicAccordion 
		legislature={data.legislature} 
		meetingNr={data.meetingNr} 
		topic={topic} 
		topNr={data.speechesByTopic[topic][0]?.topNr} 
		speeches={data.speechesByTopic[topic]} 
		selectedTopic={data.selectedTopic} />	
	{/each}
</div>
