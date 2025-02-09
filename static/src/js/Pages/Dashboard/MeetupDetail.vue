<script setup>
import WorkspaceLayout from '@/layouts/WorkspaceLayout.vue';

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
  meetup: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj && "date" in obj
  },
});
</script>

<template>
  <WorkspaceLayout :workspace="workspace">
    <div class="flex gap-x-4">
      <div class="w-32 aspect-square bg-gray-50 rounded-xl">
      </div>
      <div>
        <p class="font-black"> {{ meetup.name }}</p>
        <p>Date: {{ meetup.date }}</p>
      </div>
    </div>
  </WorkspaceLayout>
</template>
