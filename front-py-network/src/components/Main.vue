<template>
    <div class="content">
      <div class="graphs row">
        <ResizableScreen class="col-md-6 col-12 mt-3" widthProp="100%" heightProp="300px" title="MAC use"/>
        <ResizableScreen class="col-md-6 col-12 mt-3" widthProp="100%" heightProp="300px" title="Network use"/>
      </div>
      <b-modal centered size="xl" id="my-modal">
          <template v-slot:default>
            <div>
              <ResizableScreen class="col-12 mt-3" widthProp="100%" heightProp="80%" title="Network use"/>
            </div>
          </template>
      </b-modal>
    </div>
</template>

<script>
  import ResizableScreen from '@/tools/ResizableScreen'
  export default {
    name: 'main',
    components: {
      'ResizableScreen': ResizableScreen
    }
  }

</script>


