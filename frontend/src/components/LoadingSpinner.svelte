<script>
    import { onDestroy } from "svelte";

    let show = false;
    const timeoutId = setTimeout(()=>show=true, 400);
    onDestroy(()=>clearTimeout(timeoutId));
</script>

{#if show}
    <div class="flex flex-col items-center my-auto">
        <span class="loading loading-spinner loading-lg text-primary"></span>
        <p>Wird geladen ...</p>
    </div>	
{/if}
