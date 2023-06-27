<script>
	import TopicAccordion from './TopicAccordion.svelte';
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div class="py-4 space-y-2">
	{#each data.topics as topic}
		<TopicAccordion {topic} topNr={data.speechesByTopic[topic][0]?.topNr} speeches={data.speechesByTopic[topic]} />
	{/each}
</div>
