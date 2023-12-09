<svelte:head>
	<title>Wortmeldungen {data.meetingNr}. NR-Sitzung ({data.legislature} GP) | parli-info.org</title>
</svelte:head>

<script>
	import LicenseHint from '../../../../components/LicenseHint.svelte';
	import TopicAccordion from './TopicAccordion.svelte';
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Wortmeldungen der {data.meetingNr}. NR-Sitzung ({data.legislature} GP)
	</h1>
</div>

<LicenseHint/>

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
