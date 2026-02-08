import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:tflite_v2/tflite_v2.dart';

late List<CameraDescription> _cameras;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  _cameras = await availableCameras();
  runApp(const FixLensApp());
}

class FixLensApp extends StatelessWidget {
  const FixLensApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(home: const VisionScreen());
}

class VisionScreen extends StatefulWidget {
  const VisionScreen({super.key});
  @override
  State<VisionScreen> createState() => _VisionScreenState();
}

class _VisionScreenState extends State<VisionScreen> {
  CameraController? controller;
  bool isBusy = false;

  @override
  void initState() {
    super.initState();
    initCamera();
    loadModel();
  }

  // LOAD YOUR BICYCLE BRAIN
  loadModel() async {
    await Tflite.loadModel(
      model: "assets/best_int8.tflite",
      labels: "assets/labels.txt", // Note: Ensure you have a labels file too!
    );
  }

  initCamera() {
    controller = CameraController(_cameras[0], ResolutionPreset.medium);
    controller?.initialize().then((_) {
      if (!mounted) return;
      // Start the live stream!
      controller?.startImageStream((image) {
        if (!isBusy) {
          isBusy = true;
          runModelOnFrame(image);
        }
      });
      setState(() {});
    });
  }

  runModelOnFrame(CameraImage img) async {
    // This is where the AI "looks" at each frame
    var recognitions = await Tflite.detectObjectOnFrame(
      bytesList: img.planes.map((plane) => plane.bytes).toList(),
      model: "YOLO",
      imageHeight: img.height,
      imageWidth: img.width,
      threshold: 0.4,
    );
    
    print(recognitions); // Watch your terminal for detected bike parts!
    isBusy = false;
  }

  @override
  Widget build(BuildContext context) {
    if (controller == null || !controller!.value.isInitialized) return Container();
    return Scaffold(
      body: CameraPreview(controller!),
    );
  }
}