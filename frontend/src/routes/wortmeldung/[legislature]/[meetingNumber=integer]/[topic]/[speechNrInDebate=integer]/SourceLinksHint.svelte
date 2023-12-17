<script>
    export let videoUrl = "";
    export let speechUrl = "";
</script>

<div role="alert" class="alert shadow-lg ">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="stroke-info shrink-0 w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
    <div>
        <h3 class="font-bold">Quellenhinweis</h3>
        <div class="text-xs">
            <a class="link" href={videoUrl}>Originalvideo</a> /
            <a class="link" href={speechUrl}>Originaltext</a>
        </div>
    </div>
</div>